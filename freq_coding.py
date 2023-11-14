''' Функция подсчитывающая частотность каждого символа '''
def freq_alphabet(filename):
        rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        freq_array = {ch: 0 for ch in rus_alphabet}
        with open(f"{filename}") as file:
                for line in file:
                        for letter in line.lower():
                                if freq_array.get(letter) != None:
                                        freq_array[letter] += 1
        print(freq_array)
        return freq_array

''' 
Функция перводит текст согласно словарю (alph_in - старый алфавит, alph_out - новый алфавит).
На выходе получаем переведенный текст.
'''
def transfer_alph(text, alph_in, alph_out):
        _alph_in = alph_in.lower() + alph_in.upper()
        _alph_out = alph_out.lower() + alph_out.upper()
        transfer = {_alph_in[i]: _alph_out[i] for i in range(len(_alph_in))}
        translate = ""
        for letter in text:
                if transfer.get(letter) != None:
                        translate += transfer[letter]
                else:
                        translate += letter
        return translate


def simple_coding(translate, filename, alph1, alph2):
        t = open(f'{translate}', "w+")
        with open(f'{filename}', "r") as file:
                for line in file:
                        t.writelines(transfer_alph(line, alph1, alph2))

def sc_randline(filename, alph1, alph2):
        import random
        file = open(f'{filename}', 'r')
        #max_line = sum(1 for line in file)
        lines = file.readlines()
        sum_lines = len(lines)
        #print(lines)
        num_line = random.randint(0, sum_lines)
        return print(transfer_alph(lines[num_line], alph1, alph2), 'Номер строки: ', num_line)

def main():
        freq_1 = freq_alphabet('Война и мир - том 1.txt')
        freq_1 = [(letter, freq) for letter, freq in freq_1.items()]
        freq_1.sort(key=lambda k: k[1], reverse=True)
        alph1 = "".join(freq_1[i][0] for i in range(len(freq_1)))
        print(alph1)
        # Можно придумать рандомный шифр
        transfer = 'йцукенгшщзхъфывапролджэячсмитьбю'

        simple_coding('translate.txt', 'Война и мир - том 2.txt', alph1, transfer)

        freq_2 = freq_alphabet('translate.txt')
        freq_2 = [(letter, freq) for letter, freq in freq_2.items()]
        freq_2.sort(key=lambda k: k[1], reverse=True)
        alph2 = "".join(freq_2[i][0] for i in range(len(freq_2)))
        print(alph2)

        sc_randline('translate.txt', alph2, alph1)

if __name__ == "__main__":
        main()