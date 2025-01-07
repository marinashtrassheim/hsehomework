-- Создание таблицы Customers
CREATE TABLE "Customers" (
    "customer_id" SERIAL PRIMARY KEY,
    "full_name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(255) UNIQUE NOT NULL,
    "created_at" TIMESTAMP NOT NULL,
);


-- Создание таблицы Products
CREATE TABLE "Products" (
    "product_id" SERIAL PRIMARY KEY,
    "name" VARCHAR(100) NOT NULL,
    "description" TEXT,
    "category_id" INT REFERENCES "ProductCategories"("category_id") ON DELETE CASCADE,
    "price" NUMERIC(10, 2) NOT NULL CHECK ("price" >= 0),
    "stock_quantity" INT NOT NULL CHECK ("stock_quantity" >= 0),
    "creation_date" TIMESTAMP DEFAULT NOW()
);

-- Создание таблицы Orders
CREATE TABLE "Orders" (
    "order_id" SERIAL PRIMARY KEY,
    "user_id" INT REFERENCES "Users"("user_id") ON DELETE CASCADE,
    "order_date" TIMESTAMP NOT NULL,
    "total_amount" NUMERIC(10, 2) NOT NULL CHECK ("total_amount" >= 0),
    "status" VARCHAR(20) NOT NULL CHECK ("status" IN ('Pending', 'Completed', 'Canceled', 'Processing', 'Shipped', 'Delivered', 'Returned', 'Failed')),
    "delivery_date" TIMESTAMP
);

-- Создание таблицы OrderDetails
CREATE TABLE "OrderDetails" (
    "order_detail_id" SERIAL PRIMARY KEY,
    "order_id" INT REFERENCES "Orders"("order_id") ON DELETE CASCADE,
    "product_id" INT REFERENCES "Products"("product_id") ON DELETE CASCADE,
    "quantity" INT NOT NULL CHECK ("quantity" > 0),
    "price_per_unit" NUMERIC(10, 2) NOT NULL CHECK ("price_per_unit" >= 0),
    "total_price" NUMERIC(10, 2) NOT NULL CHECK ("total_price" >= 0)
);
