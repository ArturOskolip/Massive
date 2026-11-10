
class Node:
    """Клас, що описує окремий вузол бінарного дерева."""

    def __init__(self, data):
        self.data = data  # Значення елемента
        self.left = None  # Посилання на ліву дитину (менші елементи)
        self.right = None  # Посилання на праву дитину (більші або рівні елементи)


class BinarySearchTree:
    """Клас для управління Бінарним Деревом Пошуку."""

    def __init__(self):
        self.root = None  # Корінь дерева
        self._count = 0  # Загальна кількість елементів

    def insert(self, value) -> None:
        """1. Додає новий елемент у дерево."""

        def _insert_recursive(node: Node, val) -> Node:
            if node is None:
                return Node(val)
            if val < node.data:
                node.left = _insert_recursive(node.left, val)
            else:
                node.right = _insert_recursive(node.right, val)
            return node

        self.root = _insert_recursive(self.root, value)
        self._count += 1

    def contains(self, value) -> bool:
        """2. Перевіряє наявність елемента в дереві (пошук)."""
        current = self.root
        while current:
            if value == current.data:
                return True
            elif value < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def find_min(self):
        """3. Знаходить та повертає найменший елемент."""
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        """4. Знаходить та повертає найбільший елемент."""
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def delete(self, value) -> bool:
        """5. Видаляє елемент з дерева із збереженням його структури."""
        deleted = False

        def _min_node(node: Node) -> Node:
            current = node
            while current.left:
                current = current.left
            return current

        def _delete_recursive(node: Node, val) -> Node:
            nonlocal deleted
            if node is None:
                return None

            if val < node.data:
                node.left = _delete_recursive(node.left, val)
            elif val > node.data:
                node.right = _delete_recursive(node.right, val)
            else:
                deleted = True
                # Випадок 1 та 2: 0 або 1 дитина
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # Випадок 3: 2 дитини — шукаємо найменший вузол у правому піддереві
                temp = _min_node(node.right)
                node.data = temp.data
                node.right = _delete_recursive(node.right, temp.data)

            return node

        self.root = _delete_recursive(self.root, value)
        if deleted:
            self._count -= 1
        return deleted

    def count(self) -> int:
        """6. Повертає загальну кількість елементів у дереві."""
        return self._count

    def get_all_elements(self) -> list:
        """7. Повертає відсортований список усіх елементів (In-order traversal)."""
        elements = []

        def _in_order(node: Node):
            if node:
                _in_order(node.left)
                elements.append(node.data)
                _in_order(node.right)

        _in_order(self.root)
        return elements


# === Демонстрація роботи та тестування ===
if __name__ == "__main__":
    bst = BinarySearchTree()

    print("1. Додавання елементів у дерево: [3, 1, 9, 1, 7, 10, 6, 8]")
    values = [3, 1, 9, 1, 7, 10, 6, 8]
    for v in values:
        bst.insert(v)

    print("Всі елементи (впорядковані):", bst.get_all_elements())
    print("Кількість елементів (count()):", bst.count())

    print("\n2. Пошук елементів (contains()):")
    print("Чи є елемент 7?:", bst.contains(7))
    print("Чи є елемент 15?:", bst.contains(15))

    print("\n3. Знаходження мінімуму та максимуму:")
    print("Найменший елемент (find_min()):", bst.find_min())
    print("Найбільший елемент (find_max()):", bst.find_max())

    print("\n4. Видалення вузла з двома нащадками (видаляємо 3):")
    bst.delete(3)
    print("Елементи після видалення 3:", bst.get_all_elements())
    print("Нова кількість елементів:", bst.count())
