# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input("Введите количество монеток: "))

array_coins = [randint(0, 1) for i in range(n)]

count_eagles = 0
count_tails = 0
for i in range(0, n):
    if array_coins[i] == 0:
        count_tails += 1
    else:
        count_eagles += 1

if count_eagles <= count_tails:
    print(count_eagles)
else:
    print(count_tails)
print(array_coins)
