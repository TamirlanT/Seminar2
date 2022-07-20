# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число-->  '))
def Mult(n):
    result = []

    for i in range(1, n+1):
        if i > 1:
            result.append(result[-1] * i)
        else:
            result.append(i)
    return result


print(Mult(N))