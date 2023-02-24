# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
#  Петя помогает Кате по математике.
#  Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
#  Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 - 2,2
# 5,6 - 2,3

sum_num = int(input("Введите сумму чисел: "))
multiplication_num = int(input("Введите произведение чисел: "))

first_number = 0
second_number = 0

for i in range(0, sum_num+1):
    if multiplication_num == i * (sum_num - i):
        first_number = i
        second_number = sum_num - i

if first_number == 0 and second_number == 0:
    print("Числа которые назвал Петя не могут быть произведением и суммой")
else:
    print(first_number, second_number)
