import random

# --- Підготовка ---
def gen_mat(r, c, a, b):
    return [[random.randint(a, b) for _ in range(c)] for _ in range(r)]

def print_mat(m, title=""):
    print(f"\n{title}")
    if not m or not m[0]: return print("[Порожня]")
    print("\t" + "\t".join(f"Стовп {j+1}" for j in range(len(m[0]))))
    for i, r in enumerate(m):
        row_str = " | ".join(f"{x:6.2f}" if isinstance(x, float) else f"{x:<6}" for x in r)
        print(f"Рядок {i+1}\t{row_str}")

# --- Основні завдання ---
# 1. Відняти середнє арифметичне рядка
def task1(m):
    return [[round(x - sum(r)/len(r), 2) for x in r] for r in m]

# 2. Циклічний зсув на k вправо та вгору
def task2(m, k):
    if not m: return m
    kr, ku = k % len(m[0]), k % len(m)
    shifted_right = [r[-kr:] + r[:-kr] for r in m] if kr else [r[:] for r in m]
    return shifted_right[ku:] + shifted_right[:ku] if ku else shifted_right

# 3. Видалити рядки та стовпці з максимумом
def task3(m):
    mx = max(x for r in m for x in r)
    bad_r = {i for i, r in enumerate(m) if mx in r}
    bad_c = {j for r in m for j, x in enumerate(r) if x == mx}
    cleaned = [[x for j, x in enumerate(r) if j not in bad_c] 
               for i, r in enumerate(m) if i not in bad_r]
    return cleaned, mx

# 4. Обертання на 90° за стрілкою in-place (квадратна матриця)
def task4(m):
    n = len(m)
    for i in range(n):
        for j in range(i + 1, n):
            m[i][j], m[j][i] = m[j][i], m[i][j]
        m[i].reverse()

# --- Додаткове завдання: 3D Розклад [Групи][Дні][Пари] ---
DAYS = ["Пн", "Вт", "Ср", "Чт", "Пт"]

def task_schedule():
    subjects = ["Мат", "Фіз", "Прог", "Вільне вікно"]
    # 3 групи x 5 днів x 4 пари
    sch = [[[random.choice(subjects) for _ in range(4)] for _ in range(5)] for _ in range(3)]
    
    # Штучне створення вікна і потоку для демонстрації
    sch[0][2] = ["Мат", "Вільне вікно", "Фіз", "Вільне вікно"]
    sch[0][1][0] = sch[1][1][0] = "Філософія"

    print("\n=== 3D РОЗКЛАД ===")
    # 1. Найбільше навантаження (Група 1)
    busiest = max(range(5), key=lambda d: sum(1 for p in sch[0][d] if p != "Вільне вікно"))
    print(f"1. Найзавантаженіший день (Група 1): {DAYS[busiest]}")

    # 2. Пошук вікон
    print("2. Дні з «вікнами»:")
    for g in range(3):
        for d in range(5):
            act = [i for i, p in enumerate(sch[g][d]) if p != "Вільне вікно"]
            if len(act) > 1 and (max(act) - min(act) + 1 > len(act)):
                print(f"   - Гр {g+1}, {DAYS[d]}: {sch[g][d]}")

    # 3. Перевірка на потокові заняття
    print("3. Потокові заняття:")
    for d in range(5):
        for p in range(4):
            pairs = [sch[g][d][p] for g in range(3)]
            for item in set(pairs):
                if item != "Вільне вікно" and pairs.count(item) > 1:
                    print(f"   - {DAYS[d]}, Пара {p+1}: {item}")

# --- Запуск ---
if __name__ == "__main__":
    matrix = gen_mat(4, 5, 10, 50)
    print_mat(matrix, "Початкова матриця:")
    
    print_mat(task1(matrix), "1. Віднімання середнього рядка:")
    print_mat(task2(matrix, 2), "2. Зсув на 2 вправо та вгору:")
    
    m_clean, mx_val = task3(matrix)
    print(f"\n3. Максимум = {mx_val}")
    print_mat(m_clean, "   Після видалення Max рядків/стовпчиків:")
    
    sq_matrix = gen_mat(4, 4, 1, 9)
    print_mat(sq_matrix, "4. Квадратна матриця 4x4:")
    task4(sq_matrix)
    print_mat(sq_matrix, "   Після обертання на 90° in-place:")
    
    task_schedule()
