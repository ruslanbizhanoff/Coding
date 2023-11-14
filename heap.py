from collections import Counter

def split(text, chair):
    while len(text) > 1 and text[0] != []:
        freq_left = []
        freq_right = []
        for i in range(len(text)):
            # Рекурсивное деление пополам
            if type(text[i]) == list:
                split(text[i], chair)
            else:
                # Деление на левую и правую ветви
                if sum(freq_left) <= sum(freq_right):
                    freq1, ch1 = text[len(freq_left)]
                    chair[str(ch1)] += "0"
                    freq_left.append(freq1)
                else:
                    freq2, ch2 = text[-len(freq_right)-1]
                    freq_right.append(freq2)
                    chair[str(ch2)] += "1"
        h = [text[:len(freq_left)], text[len(freq_left):]]
        return split(h, chair)
    return chair

def heap(s):
    text = []
    if len(Counter(s)) == 1:
        chair = {ch: "0" for ch, freq in Counter(s).most_common()}
    else:
        chair = {ch: "" for ch, freq in Counter(s).most_common()}
    for ch, freq in Counter(s).most_common():
        text.append((freq, ch))
    return split(text, chair)
def main():
    s = input()
    code = heap(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

if __name__ == "__main__":
    main()