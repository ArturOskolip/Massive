class Node:
    """Клас, що описує окремий вузол черги."""

    def __init__(self, data, next_node=None):
        self.data = data  # Значення елемента
        self.next = next_node  # Посилання на наступний вузол


class Queue:
    """Клас для управління структурою даних 'Черга' (FIFO)."""

    def __init__(self):
        self._head = None  # Вказівник на початок черги (звідси видаляємо)
        self._tail = None  # Вказівник на кінець черги (сюди додаємо)
        self._size = 0  # Лічильник елементів

    def enqueue(self, item) -> None:
        """Додає новий елемент у кінець черги (Tail)."""
        new_node = Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Видаляє та повертає елемент з початку черги (Head)."""
        if self.is_empty():
            raise IndexError("Черга порожня! Неможливо виконати dequeue().")

        data = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return data

    def peek(self):
        """Повертає елемент з початку черги без його видалення."""
        if self.is_empty():
            raise IndexError("Черга порожня! Неможливо виконати peek().")
        return self._head.data

    def is_empty(self) -> bool:
        """Перевіряє, чи порожня черга."""
        return self._head is None

    def count(self) -> int:
        """Повертає кількість елементів у черзі."""
        return self._size

    def size(self) -> int:
        """Синонім для count(): повертає кількість елементів у черзі."""
        return self.count()

    def to_string(self) -> str:
        """Повертає текстове представлення елементів черги від Head до Tail."""
        elements = []
        current = self._head
        while current:
            elements.append(str(current.data))
            current = current.next
        return "Head -> [" + " -> ".join(elements) + "] <- Tail"

    def __str__(self) -> str:
        return self.to_string()


# === Демонстрація роботи та тестування ===
if __name__ == "__main__":
    queue = Queue()

    print("1. Додавання елементів (enqueue): 12, 25, 8")
    queue.enqueue(12)
    queue.enqueue(25)
    queue.enqueue(8)

    print("Поточна черга:", queue.to_string())
    print("Розмір (size()):", queue.size())
    print("Кількість (count()):", queue.count())

    print("\n2. Перегляд першого елемента (peek):", queue.peek())
    print("Черга після peek():", queue.to_string())

    print("\n3. Видалення елементів за принципом FIFO (dequeue):")
    popped_item = queue.dequeue()
    print(f"Вилучено елемент: {popped_item}")
    print("Черга після dequeue():", queue.to_string())
    print("Новий розмір (size()):", queue.size())

    print("\n4. Послідовне вилучення решти елементів:")
    print("Вилучено:", queue.dequeue())
    print("Вилучено:", queue.dequeue())
    print("Чи порожня черга після видалення всіх елементів?:", queue.is_empty())
