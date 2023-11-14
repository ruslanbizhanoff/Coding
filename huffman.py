from collections import Counter, namedtuple
import heapq
import os
class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"
def huffman(text):
    h = []
    for ch, freq in Counter(text).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, count, root)] = h
        root.walk(code, "")
    return code

def decode_huffman(encoded, code):
    _code = {str(acc): ch for ch, acc in code.items()}
    bit = ""
    encode = ""
    for _bit in encoded:
        bit += _bit
        if _code.get(bit) != None:
            encode += _code[bit]
            bit = ""
    return encode

def main():
    with open('Война и мир - том 1.txt', 'r') as file:
        text = "".join(_ for _ in file.readlines())
    code = huffman(text)
    encoded = "".join(code[ch] for ch in text)
    print("Число битов до сжатия: ", len(text)*8)
    print("Число битов после сжатия: ", len(encoded))
    print("Словарь: ")
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))

    print('Кодирование Хаффмана: ')
    #print(encoded)

    decode = decode_huffman(encoded, code)
    with open('decode_huffman.bin', 'wb') as file:
        file.write(encoded.encode())


    print("Декодирование: ")
    #print(decode)
    file_size = os.path.getsize('Война и мир - том 1.txt')
    print(file_size*8)
    print("Коэффициент сжатия: ", file_size*8 / len(encoded))

if __name__ == "__main__":
    main()