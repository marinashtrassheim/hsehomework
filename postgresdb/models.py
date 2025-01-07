from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric, CheckConstraint, Text, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

# Покупатель
class Customer(Base):
    __tablename__ = 'Customers'

    customer_id = Column(Integer, primary_key=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.now)

    # Связь с заказами
    orders = relationship("Order", back_populates="customer_id")



# Товар
class Product(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    stock_quantity = Column(Integer, default=0)
    creation_date = Column(DateTime, default=datetime.now)

    # Связь с деталями заказа
    order_details = relationship("OrderDetail", back_populates="product")


# Заказ
class Order(Base):
    __tablename__ = "Orders"

    order_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("Customers.customer_id"), nullable=False)
    order_date = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=True)
    status = Column(String, nullable=False)
    delivery_date = Column(DateTime, nullable=True)

    __table_args__ = (
        CheckConstraint(
            "status IN ('Completed', 'Canceled', 'Processing')",
            name="Orders_status_check"
        ),
    )

    customer = relationship("Customer", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order")


# Модель деталей заказа
class OrderDetail(Base):
    __tablename__ = "OrderDetails"

    order_detail_id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("Orders.order_id"), nullable=False)
    product_id = Column(Integer, ForeignKey("Products.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_details")
    product = relationship("Product")

