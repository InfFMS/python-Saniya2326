# Задача 3: Периметр и площадь прямоугольника
# Напишите программу, которая запрашивает у пользователя длину и ширину прямоугольника и выводит его периметр и площадь.
# Пример:
# Ввод: 4, 7
# Вывод: Периметр: 22, Площадь: 28

x = int(input())
y = int(input())

print('Периметр:', 2*(x + y))
print('Площадь,', x*y)