import threading
import time
def formula1(x):
  return x**2 - x**2 + x * 4 - x * 5 + x + x
def formula2(x):
  return x + x
def formula3(result1, result2):
  return result1 + result2
def run_calculations(iterations):
  start_time = time.time()
  thread1 = threading.Thread(target=calculate_formula1, args=(iterations,))
  thread2 = threading.Thread(target=calculate_formula2, args=(iterations,))
  thread1.start()
  thread2.start()
  thread1.join()
  thread2.join()
  result3 = formula3(result1, result2)
  end_time = time.time()
  duration = end_time - start_time
  print(f"Длительность для {iterations}: {duration:.4f} секунд")

def calculate_formula1(iterations):
  global result1, formula1_time
  start_time = time.time()
  result1 = 0
  for i in range(iterations):
    result1 += formula1(i)
  formula1_time = time.time() - start_time
def calculate_formula2(iterations):
  global result2, formula2_time
  start_time = time.time()
  result2 = 0
  for i in range(iterations):
    result2 += formula2(i)
  formula2_time = time.time() - start_time

run_calculations(10000)
run_calculations(100000)