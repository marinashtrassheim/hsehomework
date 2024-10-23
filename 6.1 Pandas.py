import pandas as pd

df = pd.read_csv(r'C:\Users\79090\OneDrive\Рабочий стол\Учеба\Python для инженерии данных\Pandas\Electronic_sales_Sep2023-Sep2024.csv')

#предпочитаемый метод оплаты
payment_method = df[['Customer ID', 'Payment Method']].groupby('Customer ID')
print(payment_method.head(5))

#общие траты
user_spent = (df[['Customer ID', 'Total Price', 'Add-on Total']].groupby('Customer ID').sum())
user_spent['Total spent'] = user_spent['Total Price'] + user_spent['Add-on Total']
print(user_spent.head(5))

#кол-во денег, потраченное на доп услуги или аксессуары
user_spent_adds_on = (df[['Customer ID', 'Add-on Total']].groupby('Customer ID').sum())
print(user_spent_adds_on.head(5))
