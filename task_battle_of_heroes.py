# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта
# по этапам/или создать kanban доску для работы над данным проектом.
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра
# состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.

# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20

# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False

# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero

# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию
# о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random
from abc import ABC, abstractmethod

# Создаем абстрактный класс героев
class Heroes(ABC):
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, other):
        pass

    def is_alive(self):
        return self.health > 0

# Создаем разные классы героев
class HeroKnight(Heroes):
    def __init__(self, name):
        super().__init__(name)

    def attack(self, other):
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        other.health -= damage
        print(f"{self.name} (Рыцарь) атакует {other.name} и наносит урон - {damage}!")

class HeroBarbarian(Heroes):
    def __init__(self, name):
        super().__init__(name, health=80, attack_power=25)

    def attack(self, other):
        damage = random.randint(self.attack_power - 3, self.attack_power + 7)
        other.health -= damage
        print(f"{self.name} (Варвар) атакует {other.name} и наносит урон - {damage}!")

# Создаем класс игры
class Game:
    def __init__(self, player: Heroes, computer: Heroes):
        self.player = player
        self.computer = computer

    def start(self):
        print("Начинается битва героев!")
        print(f"Игрок {self.player.name} против {self.computer.name}")

        while self.player.is_alive() and self.computer.is_alive():
            input("Нажмите Enter для атаки")
            self.player.attack(self.computer)

            if not self.computer.is_alive():
                print(f"{self.computer.name} повержен! {self.player.name} победил!")
                break

            self.computer.attack(self.player)

            if not self.player.is_alive():
                print(f"{self.player.name} повержен! {self.computer.name} победил!")
                break

            print(f"{self.player.name}: {self.player.health} HP | {self.computer.name}: {self.computer.health} HP\n")

        print("Игра окончена!")

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player_class = input("Выберите класс (knight/barbarian): ").strip().lower()

    if player_class == "barbarian":
        player = HeroBarbarian(player_name)
    else:
        player = HeroKnight(player_name)

    computer = random.choice([HeroKnight("Компьютер-рыцарь"), HeroBarbarian("Компьютер-варвар")])

    game = Game(player, computer)
    game.start()