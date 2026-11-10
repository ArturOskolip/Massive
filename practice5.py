import random
import sys
import time

# Збільшуємо ліміт рекурсії для роботи з великими масивами
sys.setrecursionlimit(200000)


def quick_sort(arr: list[float], ascending: bool = True) -> None:
    """Головна функція сортування QuickSort з декомпозицією."""
    if len(arr) <= 1:
        return
    _quick_sort_recursive(arr, 0, len(arr) - 1, ascending)


def _quick_sort_recursive(
    arr: list[float], low: int, high: int, ascending: bool
) -> None:
    """Рекурсивна частина алгоритму."""
    if low < high:
        pivot_index = _partition(arr, low, high, ascending)
        _quick_sort_recursive(arr, low, pivot_index - 1, ascending)
        _quick_sort_recursive(arr, pivot_index + 1, high, ascending)


def _partition(
    arr: list[float], low: int, high: int, ascending: bool
) -> int:
    """Розподіл масиву відносно опорного елемента (півоти)."""
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # Перевірка напрямку сортування
        condition = arr[j] <= pivot if ascending else arr[j] >= pivot
        if condition:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def is_sorted(arr: list[float], ascending: bool = True) -> bool:
    """Перевірка впорядкованості масиву. Повертає True або False."""
    for i in range(len(arr) - 1):
        if ascending and arr[i] > arr[i + 1]:
            return False
        if not ascending and arr[i] < arr[i + 1]:
            return False
    return True


# Тестування та вимірювання часу
if __name__ == "__main__":
    sizes = [1000, 10000, 100000]

    print(
        f"{'Кількість':<12} | {'Напрямок':<12} | {'Час (мс)':<12} | {'Відсортовано':<12}"
    )
    print("-" * 55)

    for size in sizes:
        base_array = [random.uniform(-500.0, 500.0) for _ in range(size)]

        # Тест за зростанням
        arr_asc = base_array.copy()
        t0 = time.perf_counter()
        quick_sort(arr_asc, ascending=True)
        t1 = time.perf_counter()
        time_asc = (t1 - t0) * 1000
        valid_asc = is_sorted(arr_asc, ascending=True)

        print(
            f"{size:<12} | {'Зростання':<12} | {time_asc:<12.2f} | {str(valid_asc):<12}"
        )

        # Тест за спаданням
        arr_desc = base_array.copy()
        t0 = time.perf_counter()
        quick_sort(arr_desc, ascending=False)
        t1 = time.perf_counter()
        time_desc = (t1 - t0) * 1000
        valid_desc = is_sorted(arr_desc, ascending=False)

        print(
            f"{size:<12} | {'Спадання':<12} | {time_desc:<12.2f} | {str(valid_desc):<12}"
        )
