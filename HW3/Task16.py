'''Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1'''

number = int(input("Размер массива: "))

lst = input('Элементы массива через пробел: ').split()
lstN = list(map(int, lst))

# Можно добавить проверку
# if len(lst1) != number
# print("Wrong number")
# else:

x = int(input("Искомое число: "))
count = 0

for i in range(number):
    if lstN[i] == x:
        count += 1
print(f'Встречается {count} раз/раза')
