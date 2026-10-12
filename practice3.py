import random


# 1. Генерація масиву
def generate_array(length, min_val, max_val):
  return [random.randint(min_val, max_val) for _ in range(length)]


# 2. Форматоване виведення масиву
def print_array(arr):
  formatted = ','.join([f'[cell - {i},value - {v}]' for i, v in enumerate(arr)])
  result = '{' + formatted + '}'
  print(result)
  return result


# 3. Bubble sort (Бульбашкове сортування)
def bubble_sort(arr, ascending=True):
  a = arr.copy()
  n = len(a)
  for i in range(n):
    for j in range(0, n - i - 1):
      if (ascending and a[j] > a[j + 1]) or (
          not ascending and a[j] < a[j + 1]
      ):
        a[j], a[j + 1] = a[j + 1], a[j]
  return a


# 4. Insertion sort (Сортування вставками)
def insertion_sort(arr, ascending=True):
  a = arr.copy()
  for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and (
        (ascending and a[j] > key) or (not ascending and a[j] < key)
    ):
      a[j + 1] = a[j]
      j -= 1
    a[j + 1] = key
  return a


# 5. Selection sort (Сортування вибором)
def selection_sort(arr, ascending=True):
  a = arr.copy()
  n = len(a)
  for i in range(n):
    target_idx = i
    for j in range(i + 1, n):
      if (ascending and a[j] < a[target_idx]) or (
          not ascending and a[j] > a[target_idx]
      ):
        target_idx = j
    a[i], a[target_idx] = a[target_idx], a[i]
  return a


# --- Демонстрація роботи ---
if __name__ == '__main__':
  random.seed(42)  # Для відтворюваності результату
  arr = generate_array(6, 1, 20)

  print('Початковий несоратований масив:')
  print_array(arr)

  print('\n--- Bubble Sort ---')
  print('Прямий порядок (true):')
  print_array(bubble_sort(arr, True))
  print('Зворотний порядок (false):')
  print_array(bubble_sort(arr, False))

  print('\n--- Insertion Sort ---')
  print('Прямий порядок (true):')
  print_array(insertion_sort(arr, True))
  print('Зворотний порядок (false):')
  print_array(insertion_sort(arr, False))

  print('\n--- Selection Sort ---')
  print('Прямий порядок (true):')
  print_array(selection_sort(arr, True))
  print('Зворотний порядок (false):')
  print_array(selection_sort(arr, False))
