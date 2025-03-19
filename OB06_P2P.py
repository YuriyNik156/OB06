class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health = max(other.health - self.attack_power, 0)

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра начинается!")
        round_number = 1
        while True:
            print(f"\nРаунд {round_number}")
            # Ход игрока
            self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name}. У {self.computer.name} осталось {self.computer.health} здоровья.")
            if not self.computer.is_alive():
                print(f"\n{self.computer.name} повержен! {self.player.name} побеждает!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name}. У {self.player.name} осталось {self.player.health} здоровья.")
            if not self.player.is_alive():
                print(f"\n{self.player.name} повержен! {self.computer.name} побеждает!")
                break

            round_number += 1


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name)
    computer = Hero("Компьютер")
    game = Game(player, computer)
    game.start()