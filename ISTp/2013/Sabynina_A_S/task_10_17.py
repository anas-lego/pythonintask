#Задача 9. Вариант 17.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно быть предоставлено 30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и возвращать их туда из характеристик, которым он решил присвоить другие значения.

import os

class Hero:
    def __init__(self):
        self.stats = [0,  # Сила
                      0,  # Ловкость
                      0,  # Здоровье
                      0]  # Мудрость
        self.error_list = []
        self.get_stats_sum = lambda stats: sum(stats)
        self.is_stats_overflowed = lambda stats_sum: stats_sum not in range(0, 31)

    def change_stats(self, stat_n=0, amount=0):
        self.error_list = []
        if amount > 0:
            if self.is_stats_overflowed(self.get_stats_sum(self.stats) + amount):
                amount = 30 - self.get_stats_sum(self.stats)
                self.error_list.append('Вы привысили максимальный лимит очков распраделения.')
                self.error_list.append('Прирост уменьшен до {}'.format(amount))
        elif self.stats[stat_n] < abs(amount):
            amount = - self.stats[stat_n]
            self.error_list.append('Нельзя уменьшить характеристику сильнее, чем до 0')
        self.stats[stat_n] += amount
        self.stat_pool -= amount


class GUI:
    def __init__(self, hero):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.hero = hero
        print("""Введите <номер хар-ки> <изменение> для изменения характеристики.
<изменеие> может быть как больше, так и меньше нуля, если вы хотите уменьшить эту характеристику
Или просто нажмите <Enter> для выхода.
""")


    def main_menu(self):
        while True:

            print("""Главное меню:
1. Сила     {}
2. Ловкость {}
3. Здоровье {}
4. Мудрость {}
Нераспределенных очков: {}
""".format(*self.hero.stats, self.hero.stat_pool))
            {print(error) for error in self.hero.error_list}
            print()
            exit_code = input('Ваш ввод: ').split()

            try:
                stat_n = int(exit_code[0]) - 1
                amount = int(exit_code[1])
            except Exception:
                return
            os.system('cls' if os.name == 'nt' else 'clear')
            self.hero.change_stats(stat_n, amount)


my_hero = Hero()
gui = GUI(my_hero)
gui.main_menu()
input("\n\nНажмите Enter для выхода.")