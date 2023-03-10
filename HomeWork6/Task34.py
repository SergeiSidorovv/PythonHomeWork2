# Задача 32: Определить индексы элементов массива (списка),
#  значения которых принадлежат заданному диапазону
#  (т.е. не меньше заданного минимума и не больше заданного максимума)
# Пример ввод [1,2,3,4,-5] ,5,15
# вывод: [1,2,3,4]
import random

min_number = int(input("Введите минимальное число в массиве: "))
max_number = int(input("Введите максимальное число в массиве: "))
new_list = [random.randint(0, 10) for _ in range(10)]
print(new_list)


def numbers_list(new_list, min_number, max_number):
    num_list = []
    for item in new_list:
        if item > min_number and item < max_number:
            num_list.append(item)
    return num_list


print(numbers_list(new_list, min_number, max_number))
