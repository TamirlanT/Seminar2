number = float(input('Введите вещественное число"0.00": '))

def SumDigits(n):
    digits = int(str(n).replace('.', ''))

    sum = 0
    while digits != 0:
        sum += digits % 10
        digits //= 10
    return sum

print(SumDigits(number))