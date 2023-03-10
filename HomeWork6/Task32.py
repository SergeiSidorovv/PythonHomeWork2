# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Пример ввод: 7, 2, 5
# вывод: 7,9,11,13,15

start_num = int(input("Введите число с которого начинается перебор: "))
step = int(input("Введите шаг: "))
count_numbers = int(input("Введите количество чисел: "))


def fill_list(start_num, step, count_numbers):
    new_array = [start_num]
    for i in range(count_numbers-1):
        new_array.append(start_num + step)
        start_num = start_num + step
    return new_array


print(fill_list(start_num, step, count_numbers))
