class Node:
    """Клас, що описує окремий вузол стеку."""

    def __init__(self, data, next_node=None):
        self.data = data  # Значення елемента
        self.next = next_node  # Посилання на попередній вузол


class Stack:
    """Клас для управління структурою даних 'Стек'."""

    def __init__(self):
        self._top = None  # Вказівник на вершину стеку (спочатку None)
        self._size = 0  # Лічильник елементів

    def push(self, item) -> None:
        """Вставляє об'єкт на вершину стеку."""
        new_node = Node(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """Повертає елемент з вершини стеку та видаляє його."""
        if self.is_empty():
            raise IndexError("Стек порожній! Неможливо виконати pop().")
        popped_value = self._top.data
        self._top = self._top.next  # Зміщуємо вершину на наступний вузол
        self._size -= 1
        return popped_value

    def peek(self):
        """Повертає елемент з вершини стеку без видалення."""
        if self.is_empty():
            raise IndexError("Стек порожній! Неможливо виконати peek().")
        return self._top.data

    def clear(self) -> None:
        """Видаляє всі елементи зі стеку."""
        self._top = None
        self._size = 0

    def count(self) -> int:
        """Повертає кількість елементів у стеку."""
        return self._size

    def size(self) -> int:
        """Синонім для count(): повертає кількість елементів у стеку."""
        return self.count()

    def is_empty(self) -> bool:
        """Перевіряє, чи порожній стек."""
        return self._top is None

    def to_string(self) -> str:
        """Виводить всі елементи стеку без їх видалення."""
        elements = []
        current = self._top
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Top -> [" + ", ".join(elements) + "]"

    def __str__(self) -> str:
        return self.to_string()


# === Демонстрація роботи та тестування ===
if __name__ == "__main__":
    stack = Stack()

    print("1. Додавання елементів (push): 11, 22, 33")
    stack.push(11)
    stack.push(22)
    stack.push(33)

    print("Поточний стек:", stack.to_string())
    print("Розмір (size()):", stack.size())
    print("Кількість (count()):", stack.count())

    print("\n2. Перегляд вершини (peek):", stack.peek())
    print("Стек після peek():", stack.to_string())

    print("\n3. Видалення вершини (pop):", stack.pop())
    print("Стек після pop():", stack.to_string())
    print("Новий розмір (size()):", stack.size())

    print("\n4. Очищення стеку (clear())")
    stack.clear()
    print("Чи порожній стек після clear():", stack.is_empty())
    print("Розмір після clear():", stack.size())
