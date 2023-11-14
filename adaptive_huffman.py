from collections import Counter, namedtuple
import heapq

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc + self.char

def huffman(text):
    h = []
    for ch, freq in Counter(text).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        print(h)
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
        print(h)
    code = {}
    if h:
        [(_freq, count, root)] = h
        root.walk(code, "")
    return code
def main():
    text = input()
    code = huffman(text)
    #encoded = "".join(code[ch] for ch in text)
    #print(len(code), len(encoded))
    print(code)
    #for ch in sorted(code):
    #    print("{}: {}".format(ch, code[ch]))
    #print(encoded)

if __name__ == "__main__":
    main()