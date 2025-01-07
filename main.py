from postgresdb.models import Base
from postgresdb.db_config import engine
from data_generation.generator import generate_data

if __name__ == "__main__":
    # Создание модели данных
    Base.metadata.create_all(engine)
    print("Схема базы данных создана")

    # Генерация данных
    generate_data()
