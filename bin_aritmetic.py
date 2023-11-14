# Функция перевода числа из десятичной системы счисления в двоичную
from sympy import *
def _10_bin(num_10, n=128):
    num = abs(int(num_10))
    frac = N(f'{abs(num_10)} - {num}', 40)
    num_bin = ""
    if num_10 == 0:
        return "0." + "0"*128
    if num_10 == 1:
        return "1." + "0"*128
    if num == 0:
        num_bin += "0"

    while num // 2 != 0 or num % 2 != 0:
        num_bin += f"{(num % 2)}"
        num = num // 2

    if num_10 < 0:
        num_bin += "-"
    num_bin = num_bin[::-1]
    frac_bin = ""
    if frac != 0:
        num_bin += '.'
        while len(frac_bin) < n:
            frac = frac * 2
            if frac >= 1:
                frac_bin += "1"
                frac = frac - 1
            else:
                frac_bin += "0"
    else:
        return num_bin
    num_bin += frac_bin
    return num_bin

# Функция перевода числа из двоичной системы счисления в десятичную
def bin_10(num_bin):
    num_bin = N(f'{num_bin}', 128)
    num_int = 0
    num_frac = N('0', 40)
    k = 1
    if num_bin < 0:
        k = -1
        num_bin = abs(num_bin)
    i = len(str(int(num_bin)))
    for sym in str(int(num_bin)):
        num_int += int(sym) * 2**(i - 1)
        i = i - 1
    for sym in str(num_bin)[len(str(int(num_bin))) + 1:]:
        i = i - 1
        if sym == '1':
            num_frac += N(f'{2**(i)}', 40)
    num = N(f'({num_int} + {num_frac})', 40) * k
    return str(num)

# Функция арифметических операций в двоичной системе счисления
def bin_arithmetic(num1 = '0', num2 = '0'):
    if num1 == "" or num2 == "":
        return print('Ошибка! В качестве аргументов num1 и num2 возможно указаны пустые строки "".')
    bin_dif = float(bin_10(num1)) - float(bin_10(num2))
    return _10_bin(bin_dif)