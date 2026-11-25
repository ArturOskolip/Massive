import heapq
import math
from collections import Counter

# Вузол дерева Хаффмана
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # Для порівняння вузлів у черзі з пріоритетом
    def __lt__(self, other):
        return self.freq < other.freq

# Рекурсивний обхід дерева для отримання кодів (ліворуч = 0, праворуч = 1)
def get_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node is not None:
        if node.char is not None: # Якщо це лист (символ)
            codes[node.char] = prefix if prefix else "0"
        get_codes(node.left, prefix + "0", codes)
        get_codes(node.right, prefix + "1", codes)
    return codes

# Головна функція кодування
def huffman_encode(text):
    # 1. Рахуємо частоту кожного символу
    freqs = Counter(text)
    
    # 2. Створюємо список вузлів (чергу з пріоритетом)
    heap = [Node(char, freq) for char, freq in freqs.items()]
    heapq.heapify(heap)
    
    # 3. Об'єднуємо два найменші вузли, поки не залишиться одне дерево
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)
        
    # 4. Отримуємо таблицю кодів та кодуємо текст
    codes = get_codes(heap[0])
    encoded_text = "".join(codes[ch] for ch in text)
    return encoded_text, codes

# --- ПЕРЕВІРКА РОБОТИ ---
text = "абабагаламага" # Можна замінити на будь-яку іншу фразу
encoded, codes = huffman_encode(text)

# Розрахунок довжини для рівномірного коду
unique_chars = len(set(text))
bits_per_char = math.ceil(math.log2(unique_chars)) if unique_chars > 1 else 1
uniform_length = len(text) * bits_per_char

print(f"Початковий текст: {text}")
print("Таблиця кодів:", codes)
print(f"Закодований рядок: {encoded}")
print("-" * 40)
print(f"Довжина за Хаффманом: {len(encoded)} біт")
print(f"Довжина рівномірним кодом: {uniform_length} біт (по {bits_per_char} біт на символ)")
print(f"Економія: {uniform_length - len(encoded)} біт")
