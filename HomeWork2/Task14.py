# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input("Введите целое число: "))

n = 1

nums_degree_two = []
while (n < num):
    nums_degree_two.append(str(n))
    n = n * 2

print(" ".join(nums_degree_two))
