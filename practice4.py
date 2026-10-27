# Від 1 до n

def task1(n):
    if n > 0:
        task1(n - 1)
        print(n, end=" ")
# Від A до B

def task2(a, b):
    print(a, end=" ")
    if a < b:
        task2(a + 1, b)
    elif a > b:
        task2(a - 1, b)
# Точна степінь двійки

def task3(n):
    if n == 1:
        return "YES"
    if n <= 0 or n % 2 != 0:
        return "NO"
    return task3(n // 2)
# Сума цифр числа

def task4(n):
    if n == 0:
        return 0
    return n % 10 + task4(n // 10)
# Цифри числа справа наліво

def task5(n):
    if n > 0:
        print(n % 10, end=" ")
        task5(n // 10)
# Цифри числа зліва направо

def task6(n):
    if n > 0:
        task6(n // 10)
        print(n % 10, end=" ")
