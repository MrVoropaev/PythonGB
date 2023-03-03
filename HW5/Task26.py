'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''


number_a = int(input("Введите число: "))
number_b = int(input("В какую степень возвести число: "))


def degree_of_number(a, b):
    if b == 1:
        return a
    if b != 1:
        return a * degree_of_number(a, b - 1)


print(degree_of_number(number_a, number_b))
