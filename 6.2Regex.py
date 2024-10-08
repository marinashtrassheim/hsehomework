import re
some_string = 'Напишите функцию функцию, которая будет будет будет будет\nудалять все все все все последовательные повторы слов из из из из заданной\nстроки строки при помощи регулярных выражений'
def remove_repetition(text):
  return re.sub(r'\b(\w+)(\s+\1)+\b', r'\1', text)
result = remove_repetition(some_string)
print(result)

