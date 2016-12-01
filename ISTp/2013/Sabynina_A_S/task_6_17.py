# Задача 6. Вариант 17.
# Создайте игру, в которой компьютер загадывает название одного из пяти космических челноков проекта Спейс шаттл, а игрок должен его угадать.



import random

shuttle = ['Колумбия',
         'Челленджер',
         'Дискавери',
         'Атлантис',
         'Индевор']

random_shuttle = random.choice(shuttle)
print('Программа случайным образом загадывает название одной из пяти космических челноков проекта Спейс шаттл, а игрок должен его угадать.')
print('Допустимые значения: ', end=' ')
for x in shuttle:
    print(x, end=" ")
print()
my_shuttle = input('Назовите один из челноков:')
print()
if my_shuttle == random_shuttle:
    print('Вы угадали!')
else:
    print('Вы не угадали =(')
    print('Правильный ответ:', random_shuttle)

input("\n\nНажмите Enter для выхода.")