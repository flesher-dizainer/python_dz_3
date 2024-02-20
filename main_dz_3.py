def zadanie1():
    a = float(input('input a: '))
    b = float(input('input b: '))
    c = float(input('input c: '))
    d = int(input('введите желаемую операцию:\n1 - сумма чисел\n2 - произведение чисел\n'))
    if d == 1:
        print('сумма чисел = '+str(a+b+c))
    elif d == 2:
        print('произведение чисел = ' + str(a * b * c))
    else:
        print('Выбрана неверная операция')

def zadanie2():
    a = float(input('input a: '))
    b = float(input('input b: '))
    c = float(input('input c: '))
    d = int(input('введите желаемую операцию:\n1 - максимум из трёх\n2 - минимум из трёх\n3 - среднее арифметическое\n'))
    if d == 1:
        if a > b and a > c:
            print('Максимальное число = '+str(a))
        elif b > a and b > c:
            print('Максимальное число = ' + str(b))
        elif c > a and c > b:
            print('Максимальное число = ' + str(c))
    elif d == 2:
        if a < b and a < c:
            print('Минимальное число = '+str(a))
        elif b < a and b < c:
            print('Минимальное число = ' + str(b))
        elif c < a and c < b:
            print('Минимальное число = ' + str(c))
    elif d == 3:
            print('Среднее арифметическое число = '+str((a+b+c)/3))
    else:
        print('Выбрана неверная операция')

def zadanie3():
    a = float(input('Введите количество метров: '))
    d = int(input('введите желаемую операцию перевода метров в:\n1 - милли\n2 - дюймы\n3 - ярды\n'))
    if d == 1:
        print('милли = '+str(a * 0.000621371))
    elif d == 2:
        print('дюймы = ' + str(a * 39.3701))
    elif d == 3:
        print('ярды = ' + str(a * 1.09361))
    else:
        print('Выбрана неверная операция')


def main():
    print('Задание 1')
    zadanie1()
    print('Задание 2')
    zadanie2()
    print('Задание 3')
    zadanie3()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
