import random
import time

# 1. Функція генерації випадкових чисел від -10 000 до 10 000
def generate_array(size):
    return [random.randint(-10000, 10000) for _ in range(size)]

# Спосіб 1: Сортування (тут вбудоване; якщо викладач вимагає саме "просте" 

def method1_sort(arr):
    arr_copy = arr.copy()
    arr_copy.sort(reverse=True)
    return arr_copy[5] # 6-й елемент (індекс 5)

# Спосіб 2: Масив з 6 найбільших елементів
def method2_top6(arr):
    top6 = [-999999] * 6
    for num in arr:
        if num > top6[5]: # Порівнюємо з найменшим із шістки
            top6[5] = num
            top6.sort(reverse=True) # Тримаємо шістку відсортованою
    return top6[5]

# Спосіб 3: 6 разів шукаємо максимум і "витираємо" його
def method3_six_max(arr):
    arr_copy = arr.copy()
    max_val = -999999
    for _ in range(6):
        max_val = max(arr_copy)
        max_idx = arr_copy.index(max_val)
        arr_copy[max_idx] = -999999 # Замінюємо на найменше можливе
    return max_val

# --- ТЕСТУВАННЯ ТА ВИВІД РЕЗУЛЬТАТІВ ---
sizes = [10_000, 100_000, 1_000_000, 10_000_000, 100_000_000]
methods = [method1_sort, method2_top6, method3_six_max]

print(f"{'Розмір':<12} | {'Спосіб 1 (Сорт.)':<22} | {'Спосіб 2 (Масив)':<22} | {'Спосіб 3 (Макс.)':<22}")
print("-" * 85)

for size in sizes:
    row_results = []
    base_arr = generate_array(size) # Генеруємо масив один раз для розміру
    
    for method in methods:
        times = []
        for _ in range(3): # 3 запуски для середнього часу
            start = time.perf_counter()
            method(base_arr)
            end = time.perf_counter()
            ms = round((end - start) * 1000) # Переводимо в мілісекунди
            times.append(ms)
            
        avg_time = round(sum(times) / 3)
        formatted = f"{avg_time} ({times[0]} {times[1]} {times[2]})"
        row_results.append(formatted)
        
    print(f"{size:<12} | {row_results[0]:<22} | {row_results[1]:<22} | {row_results[2]:<22}")
