import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\79090\OneDrive\Рабочий стол\Учеба\Python для инженерии данных\Pandas\Electronic_sales_Sep2023-Sep2024.csv')
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], errors='coerce')
print(df.info())
#доход по типу доставки
shipping_type = df[['Shipping Type', 'Total Price', 'Add-on Total']].groupby('Shipping Type').sum()
shipping_type['Shipping income Total'] = shipping_type['Total Price'] + shipping_type['Add-on Total']
print(shipping_type.head(10))

#доход по типу продукта
product_type = df[['Product Type', 'Total Price']].groupby('Product Type').sum()
print(product_type.head(10))

#доход по дополнительным услугам за каждый месяц
adds_on_by_month = df[['Purchase Date', 'Add-on Total']]
#print(adds_on_by_month['Purchase Date'].dt.month())
print(adds_on_by_month.head(5))



