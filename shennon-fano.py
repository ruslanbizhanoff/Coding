from collections import Counter
import os

def shennon_fano(text, chair):
    while len(text) > 1 and text[0] != []:
        freq_left = []
        freq_right = []
        for i in range(len(text)):
            # Рекурсивное деление пополам
            if type(text[i]) == list:
                shennon_fano(text[i], chair)
            else:
                # Деление на левую и правую ветви
                if sum(freq_left) <= sum(freq_right):
                    freq1, ch1 = text[len(freq_left)]
                    chair[ch1] += "0"
                    freq_left.append(freq1)
                else:
                    freq2, ch2 = text[-len(freq_right)-1]
                    freq_right.append(freq2)
                    chair[ch2] += "1"
        h = [text[:len(freq_left)], text[len(freq_left):]]
        return shennon_fano(h, chair)
    return chair

def heap(s):
    text = []
    if len(Counter(s)) == 1:
        chair = {ch: "0" for ch, freq in Counter(s).most_common()}
    else:
        chair = {ch: "" for ch, freq in Counter(s).most_common()}
    for ch, freq in Counter(s).most_common():
        text.append((freq, ch))
    return shennon_fano(text, chair)

def decode_shennon_fano(encoded, code):
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
    with open('Война и мир - том 2.txt', 'r') as file:
        s = "".join(_ for _ in file.readlines())

    code = heap(s)
    encoded = "".join(code[ch] for ch in s)
    print("Число битов до сжатия: ", len(s))
    print("Число битов после сжатия: ", len(encoded))
    print("Словарь: ")
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))

    #print('Кодирование Шеннона-Фано: ')
    #print(encoded)

    decode = decode_shennon_fano(encoded, code)

    print("Декодирование: ")
    with open('shennon_fano_decode.txt', 'w') as file:
        file.write(encoded)
    file_size = os.path.getsize('Война и мир - том 2.txt')
    print(file_size)
    print("Коэффициент сжатия: ", file_size*8 / len(encoded))

if __name__ == "__main__":
    main()