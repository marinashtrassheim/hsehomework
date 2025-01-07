from faker import Faker
import random
from postgresdb.models import Customer, Product, Order, OrderDetail
from postgresdb_schemas.customer import CustomerCreate
from postgresdb_schemas.product import ProductCreate
from postgresdb_schemas.orders import OrderCreate, OrderDetailCreate
from postgresdb.db_config import get_session
from sqlalchemy.orm import Session
from sqlalchemy import text
from datetime import timedelta
from data_generation.config import DATA_GENERATION_CONFIG

def clear_database(session):
    """Очистка всех данных из базы перед генерацией."""
    session.execute(text("TRUNCATE TABLE \"OrderDetails\" CASCADE;"))
    session.execute(text("TRUNCATE TABLE \"Orders\" CASCADE;"))
    session.execute(text("TRUNCATE TABLE \"Products\" CASCADE;"))
    session.execute(text("TRUNCATE TABLE \"Customers\" CASCADE;"))
    session.commit()
    print("Процесс окончен")


def generate_data():
    """Функция генерации тестовых данных"""
    fake = Faker()
    session: Session = get_session()

    try:
        # Очистка БД
        clear_database(session)

        # Создание покупателей
        generated_emails = set()
        user_registration_dates = {}  # Словарь для хранения дат регистрации пользователей

        for _ in range(DATA_GENERATION_CONFIG["customer_count"]):
            while True:
                email = fake.email()
                if email not in generated_emails:
                    generated_emails.add(email)
                    break

            registration_date = fake.date_time_between(start_date='-1y', end_date='now')  # Случайная дата регистрации

            customer_data = {
                "full_name": fake.first_name(),
                "email": email,
                "registration_date": registration_date,
              }

            customer = CustomerCreate(**customer_data)
            customer = Customer(**customer_data.model_dump())
            session.add(customer)
            session.flush()

            # Сохраняем дату регистрации
            user_registration_dates[user.user_id] = registration_date

        session.commit()


        # Генерация товаров
        print("Генерация товаров...")
        for _ in range(DATA_GENERATION_CONFIG["products_count"]):
            group = random.choice(list(expanded_categories.keys()))
            subcategory_id = random.choice(category_ids[group]["subcategories"])
            product_data = {
                "name": fake.word(),
                "description": fake.text(max_nb_chars=200),
                "category_id": subcategory_id,
                "price": round(random.uniform(10, 1000), 2),
                "stock_quantity": random.randint(0, 100),
            }
            product_schema = ProductCreate(**product_data)
            product = Product(**product_schema.model_dump())
            session.add(product)

        session.commit()

        # Получение существующих user_id и product_id
        user_ids = [row[0] for row in session.execute(text("SELECT user_id FROM \"Users\"")).fetchall()]
        product_ids = [row[0] for row in session.execute(text("SELECT product_id FROM \"Products\"")).fetchall()]

        # Генерация заказов и деталей заказов
        print("Генерация заказов...")
        order_statuses = [
            "Pending",     # В ожидании
            "Completed",   # Завершен
            "Canceled",    # Отменен
            "Processing",  # В обработке
            "Shipped",     # Отправлен
            "Delivered",   # Доставлен
            "Returned",    # Возвращен
            "Failed",      # Неудачный
        ]

        for _ in range(DATA_GENERATION_CONFIG["orders_count"]):
            user_id = random.choice(user_ids)
            registration_date = user_registration_dates[user_id]

            # Дата заказа должна быть после даты регистрации
            order_date = fake.date_time_between(start_date=registration_date, end_date='now')
            delivery_date = fake.date_time_between(start_date=order_date, end_date=order_date + timedelta(days=30))

            total_amount = 0  # Инициализация общей суммы заказа

            # Генерация деталей заказа
            order_details = []
            for _ in range(random.randint(DATA_GENERATION_CONFIG["order_details_min"], DATA_GENERATION_CONFIG["order_details_max"])):
                product_id = random.choice(product_ids)
                quantity = random.randint(1, 5)
                price_per_unit = round(random.uniform(10, 1000), 2)
                total_price = quantity * price_per_unit
                total_amount += total_price

                order_details.append({
                    "product_id": product_id,
                    "quantity": quantity,
                    "price_per_unit": price_per_unit,
                    "total_price": round(total_price,2),
                })

            order_data = {
                "user_id": user_id,
                "order_date": order_date,
                "status": random.choice(order_statuses),
                "delivery_date": delivery_date,
                "total_amount": round(total_amount,2)
            }

            order_schema = OrderCreate(**order_data)
            order = Order(**order_schema.model_dump())
            session.add(order)
            session.flush()

            # Добавление деталей заказа в базу
            for detail in order_details:
                order_detail_schema = OrderDetailCreate(**detail)
                order_detail = OrderDetail(order_id=order.order_id, **order_detail_schema.model_dump())
                session.add(order_detail)

        session.commit()



    except Exception as e:
        print(f"Ошибка генерации данных: {e}")
        session.rollback()
    finally:
        session.close()