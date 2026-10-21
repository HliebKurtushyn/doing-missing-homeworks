from collections import Counter
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    if not text:
        return None
    frequency = Counter(text)
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return codes
    if node.char is not None:
        codes[node.char] = current_code
        return codes
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

def huffman_encode(text):
    if not text:
        return "", None
    root = build_huffman_tree(text)
    codes = generate_codes(root)
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text, root

def huffman_decode(encoded_text, root):
    if not root or not encoded_text:
        return ""
    decoded_chars = []
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            decoded_chars.append(current.char)
            current = root
    return "".join(decoded_chars)

sample_text = "тестовий рядок для алгоритму хаффмана"
encoded, tree = huffman_encode(sample_text)
decoded = huffman_decode(encoded, tree)

print("Закодовано:", encoded)
print("Декодовано:", decoded)