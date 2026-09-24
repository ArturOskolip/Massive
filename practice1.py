import random



def generate_random_array(length: int, min_val: int, max_val: int) -> list[int]:
    """Генерує масив випадкових цілих чисел заданої довжини в заданому діапазоні."""
    return [random.randint(min_val, max_val) for _ in range(length)]




# 1. Порахувати кількість та суму парних елементів у заданому діапазоні індексів
def task1_count_and_sum_even_in_range(
    arr: list[int], start_idx: int, end_idx: int
) -> tuple[int, int]:
    start = max(0, start_idx)
    end = min(len(arr) - 1, end_idx)

    count = 0
    total_sum = 0
    for i in range(start, end + 1):
        if arr[i] % 2 == 0:
            count += 1
            total_sum += arr[i]

    return count, total_sum


# 2. Середнє арифметичне та кількість елементів, більших за нього
def task2_analyze_average(arr: list[int]) -> tuple[float, int]:
    if not arr:
        return 0.0, 0

    avg = sum(arr) / len(arr)
    count_greater = sum(1 for x in arr if x > avg)
    return avg, count_greater


# 3. Попарна сума двох масивів однакової довжини
def task3_pairwise_sum(arr1: list[int], arr2: list[int]) -> list[int]:
    if len(arr1) != len(arr2):
        raise ValueError("Масиви повинні бути однакової довжини!")

    return [a + b for a, b in zip(arr1, arr2)]


# 4. Конкатенація двох масивів
def task4_concat_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    return arr1 + arr2


# 5. Поміняти місцями перший максимум та перший мінімум
def task5_swap_min_max(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr[:]

    res = arr[:]
    min_idx = res.index(min(res))
    max_idx = res.index(max(res))

    res[min_idx], res[max_idx] = res[max_idx], res[min_idx]
    return res


# 6. Поділити масив на додатні та від’ємні (0 не враховується)
def task6_split_positive_negative(
    arr: list[int],
) -> tuple[list[int], list[int]]:
    positives = [x for x in arr if x > 0]
    negatives = [x for x in arr if x < 0]
    return positives, negatives


# 7. Видалити дублікати максимума та мінімума (залишаються перші входження)
def task7_remove_min_max_duplicates(arr: list[int]) -> list[int]:
    if not arr:
        return []

    min_val = min(arr)
    max_val = max(arr)

    min_found = False
    max_found = False
    result = []

    for item in arr:
        if item == min_val:
            if not min_found:
                result.append(item)
                min_found = True
        elif item == max_val:
            if not max_found:
                result.append(item)
                max_found = True
        else:
            result.append(item)

    return result


# 8. Елементи двох масивів у межах між значеннями їх середніх арифметичних
def task8_between_averages(arr1: list[int], arr2: list[int]) -> list[int]:
    avg1 = sum(arr1) / len(arr1) if arr1 else 0
    avg2 = sum(arr2) / len(arr2) if arr2 else 0

    lower_bound = min(avg1, avg2)
    upper_bound = max(avg1, avg2)

    return [x for x in (arr1 + arr2) if lower_bound <= x <= upper_bound]



 ДОДАТКОВЕ ЗАВДАННЯ: ІГРОВИЙ ІНВЕНТАР

EMPTY_SLOT = "Empty"


def add_item(inventory: list[str], item: str) -> bool:
    """Додає предмет у першу вільну комірку."""
    for i in range(len(inventory)):
        if inventory[i] == EMPTY_SLOT:
            inventory[i] = item
            print(f"Предмет '{item}' додано в слот {i}.")
            return True
    print(f"Інвентар повний! Неможливо додати '{item}'.")
    return False


def remove_item(inventory: list[str], item: str) -> bool:
    """Видаляє предмет за запитом гравця."""
    for i in range(len(inventory)):
        if inventory[i] == item:
            inventory[i] = EMPTY_SLOT
            print(f"Предмет '{item}' видалено зі слота {i}.")
            return True
    print(f"Предмет '{item}' не знайдено в інвентарі.")
    return False


def compact_inventory(inventory: list[str]) -> None:
    """Зміщує всі предмети на початок масиву, порожні слоти опиняються в кінці."""
    non_empty = [x for x in inventory if x != EMPTY_SLOT]
    empty_slots = [EMPTY_SLOT] * (len(inventory) - len(non_empty))
    inventory[:] = non_empty + empty_slots


def print_inventory(inventory: list[str]) -> None:
    print("Стан інвентарю: [" + " | ".join(inventory) + "]")


def run_inventory_simulation():
    inventory = [EMPTY_SLOT] * 10
    print_inventory(inventory)

    add_item(inventory, "Health Potion")
    add_item(inventory, "Iron Sword")
    add_item(inventory, "Shield")
    add_item(inventory, "Mana Potion")
    print_inventory(inventory)

    print("\n--> Видаляємо 'Iron Sword':")
    remove_item(inventory, "Iron Sword")
    print_inventory(inventory)

    print("\n--> Ущільнюємо інвентар:")
    compact_inventory(inventory)
    print_inventory(inventory)


# ==========================================
# ГОЛОВНА ФУНКЦІЯ
# ==========================================
def main():
    print("=== ОСНОВНІ ЗАВДАННЯ ===")

    # Підготовка
    main_array = generate_random_array(15, -20, 20)
    print(f"Згенерований масив: {main_array}")

    # Завдання 1
    even_count, even_sum = task1_count_and_sum_even_in_range(main_array, 2, 8)
    print(
        f"\n1. Кількість парних елементів (індекси 2..8): {even_count}, Сума: {even_sum}"
    )

    # Завдання 2
    avg, greater_count = task2_analyze_average(main_array)
    print(
        f"2. Середнє арифметичне: {avg:.2f}, Елементів більших за середнє: {greater_count}"
    )

    # Завдання 3
    arr_a = generate_random_array(5, 1, 10)
    arr_b = generate_random_array(5, 1, 10)
    pairwise = task3_pairwise_sum(arr_a, arr_b)
    print(f"\n3. Масив A: {arr_a}")
    print(f"   Масив B: {arr_b}")
    print(f"   Попарна сума: {pairwise}")

    # Завдання 4
    arr_c = generate_random_array(3, 1, 10)
    arr_d = generate_random_array(5, 10, 20)
    concatenated = task4_concat_arrays(arr_c, arr_d)
    print(f"\n4. Конкатенація {arr_c} та {arr_d}:")
    print(f"   Результат: {concatenated}")

    # Завдання 5
    swapped = task5_swap_min_max(main_array)
    print(f"\n5. Початковий масив: {main_array}")
    print(f"   Після обміну Min/Max: {swapped}")

    # Завдання 6
    pos, neg = task6_split_positive_negative(main_array)
    print(f"\n6. Додатні елементи: {pos}")
    print(f"   Від'ємні елементи: {neg}")

    # Завдання 7
    sample_dupes = [10, -5, 3, 10, 2, -5, 10]
    cleaned = task7_remove_min_max_duplicates(sample_dupes)
    print(f"\n7. Масив з дублікатами: {sample_dupes}")
    print(f"   Без дублікатів Min і Max: {cleaned}")

    # Завдання 8
    first_arr = generate_random_array(8, 0, 50)
    second_arr = generate_random_array(8, 0, 50)
    bounded = task8_between_averages(first_arr, second_arr)
    avg1 = sum(first_arr) / len(first_arr)
    avg2 = sum(second_arr) / len(second_arr)
    print(f"\n8. Масив 1: {first_arr} (Avg: {avg1:.2f})")
    print(f"   Масив 2: {second_arr} (Avg: {avg2:.2f})")
    print(f"   Елементи в межах середніх: {bounded}")

    # Додаткове завдання
    print("\n=== ДОДАТКОВЕ ЗАВДАННЯ: ІГРОВИЙ ІНВЕНТАР ===")
    run_inventory_simulation()


if __name__ == "__main__":
    main()
