import re
#Для теста берем номер на АНГЛИЙСКОМ ЯЗЫКЕ
def is_valid_transport_number(number):
  pattern = r"[ABEKMHOPCTYX]{1}\d{3}[ABEKMHOPCTYX]{2}\d{2,3}"
  match = re.match(pattern, number)
  return bool(match)
# Пример использования
number1 = "A222BC96"
number2 = "123ABC456"
print(f"Номер '{number1}' - {'валидный' if is_valid_transport_number(number1) else 'невалидный'}")
print(f"Номер '{number2}' - {'валидный' if is_valid_transport_number(number2) else 'невалидный'}")

