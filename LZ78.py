from collections import Counter
from bin_aritmetic import _10_bin, bin_10
import time
''' Функция создающая первый интервал '''
def interval_sym(text):
    interval = {}
    freq_right = 0
    # Сортировка по алфавиту
    for ch, freq in sorted(Counter(text).items()):
        interval[ch] = [1, freq_right/len(Counter(text)), (freq_right + 1)/len(Counter(text))]
        freq_right += 1
    return interval
''' Функция увеличения веса для символа и последующее изменение интрвала '''
def weight(dict, sym):
    dict[sym][0] += 1
    left = 0
    sum_sym = 0
    for ch, freq in dict.items():
        sum_sym += freq[0]
    for ch, freq in sorted(dict.items()):
        dict[ch][1], dict[ch][2] = left/sum_sym, (left+freq[0])/sum_sym
        left += freq[0]
    return dict
''' Функция определяющая минимальную длину бинарного кода для последнего символа в тексте '''
def minlen_code(bin_code_left, bin_code_right):
    bin_code_mid = '0.'
    while bin_10(bin_code_mid) >= bin_10(bin_code_right) or bin_10(bin_code_mid) <= bin_10(bin_code_left):
        if bin_10(bin_code_mid + '1') >= bin_10(bin_code_right):
            bin_code_mid += '0'
        else:
            bin_code_mid += '1'
    return bin_code_mid

''' Адаптивное арифметическое кодирование  '''
def encode(text):
    interval = interval_sym(text)
    code = [0, 1]
    out = ""
    pos = 0
    if len(Counter(text)) == 1:
        return '0.1'
    for sym in text:
        pos += 1
        i = 0
        left_num, right_num = code
        code[0] = code[0] + (right_num - left_num) * interval[sym][1]
        code[1] = left_num + (right_num - left_num) * interval[sym][2]
        bin_code = [_10_bin(code[0]), _10_bin(code[1])]

        interval = weight(interval, sym)

        # Нахождение общих битов для левой и правой границ интервала и последующий их вывод
        if bin_code[1][0] == '1':
            bin_ = '0.'
        else:
            while bin_code[0][:i] == bin_code[1][:i]:
                bin_ = (bin_code[0][:i])
                i += 1

        code[0] = code[0] - float(bin_10(bin_))
        code[1] = code[1] - float(bin_10(bin_))

        # Масштабирование следующего интервала
        code[0] = code[0] * 2**(len(bin_[2:]))
        code[1] = code[1] * 2 ** (len(bin_[2:]))

        out += bin_[2:]
        print(pos)
        if pos == len(text):
            out += minlen_code(bin_code[0], bin_code[1])[2:]
    return out
#def decode(code, text):
#    interval = interval_sym(text)
#    decode_text = ""
#    for sym in interval:
#        if float(bin_10(code)) > interval[sym][1] and float(bin_10(code)) < interval[sym][2]:
#            decode_text += sym
#
#    return decode_text

def main():
    time1 = time.time()
    with open('test.txt', 'r') as file:
        text = "".join(_ for _ in file.readlines())

    encoded = encode(text)
    print(encoded)
    print("Коэффициент сжатия: ")
    print(len(text)*8 / len(encoded))
    time2 = time.time()
    print('Скорость кодирования', len(text)*8, 'бит:')
    print(len(text)*8/(time2 - time1))

    #print(decode('0.1', text))
if __name__ == '__main__':
    main()