'''Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
они сделали S журавликов. Сколько журавликов сделал каждый
ребенок, если известно, что Петя и Сережа сделали одинаковое
количество журавликов, а Катя сделала в два раза больше журавликов,
чем Петя и Сережа вместе?'''

s = int(input("Введите общее количество журавликов: "))
print(f'Петя сделал {(s//6)}, Катя сделала {((s//6)*4)}, Сережа сделал {(s//6)}')