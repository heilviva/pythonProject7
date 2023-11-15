import random
import json
import csv

class Gnome:
    def __init__(self, name):
        self.name = name
        self.destination = None
        self.location = "Дол Гулдур"

    gnome_names = ["Гимли", "Фродо", "Сэм", "Мерри", "Пиппин"]
    gnomes = [(name) for name in gnome_names]
    random_gnome = random.choice(gnomes)

    def save_game(self):
        data = {
            "name": self.name,
            "destination": self.destination,
            "location": self.location
        }
        with open("game_save.json", "w") as file:
            json.dump(data, file)

    def load_game(self):
        try:
            with open("game_save.json", "r") as file:
                data = json.load(file)
                self.name = data.get("name", self.name)
                self.destination = data.get("destination", self.destination)
                self.location = data.get("location", self.location)
            print("Игра загружена.")
        except FileNotFoundError:
            print("Нет сохраненной игры.")

    def save_to_csv(self):
        data = [
            {"name": gnome.name, "destination": gnome.destination, "location": gnome.location}
            for gnome in self.gnomes
        ]
        with open("game_progress.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "destination", "location"])
            writer.writeheader()
            writer.writerows(data)

def main():
    print(f"Добро пожаловать, {Gnome.random_gnome.name}! Выбери свой путь:")
    print("1. Пойти в Темный Лес")
    print("2. Пойти к Драконьей Горе")
    print("3. Сохранить игру")
    print("4. Загрузить игру")

    choice = input("Введите номер выбранного пути: ")
    if choice == '1':
        explore_dark_forest()
    elif choice == '2':
        go_to_dragon_mountain()
    elif choice == '3':
        Gnome.random_gnome.save_game()  # save the game
    elif choice == '4':
        Gnome.random_gnome.load_game()  # load the game
    else:
        print("Пожалуйста, введите 1, 2, 3 или 4 для выбора пути.")
def explore_dark_forest():
    print(f"{Gnome.random_gnome.name} решил отправиться в Темный Лес...")
    print("Вы находитесь в глубоком Темном Лесу. Что вы хотите сделать?")
    choice = input("1. Пойти налево\n2. Пойти направо\n3. Остаться на месте\n")
    if choice == "1":
        print("Вы направились налево и наткнулись на старое заброшенное бревно. Что вы хотите сделать?")
        choice = input("1. Попытаться поднять бревно\n2. Пройти мимо\n3. Вернуться назад\n")
        if choice == "1":
            if random.random() < 0.5:
                print("Вы с трудом подняли бревно и нашли под ним сокровище!")
            else:
                print("Вы попытались поднять бревно, но у вас не получилось. Вы устали и вернулись назад.")
        elif choice == "2":
            print("Вы прошли мимо бревна и продолжили свой путь.")
        else:
            print("Вы решили вернуться назад и выбрать другой путь.")
    elif choice == "2":
        print("Вы пошли направо и встретили диких животных. Что вы хотите сделать?")
        choice = input("1. Попытаться приручить животных\n2. Убежать\n3. Попытаться спрятаться\n")
        if choice == "1":
            if random.random() < 0.3:
                print("Вы смогли приручить животных и они стали вашими верными спутниками.")
            else:
                 print("Попытка приручить животных закончилась неудачей, и они атаковали вас. Вы попали в битву.")
        elif choice == "2":
            print("Вы попытались убежать, но животные были слишком быстрыми. Они атаковали вас.")
        else:
            print("Вы спрятались и животные прошли мимо вас. Вы продолжили свой путь.")
    else:
        print("Вы решили остаться на месте и подумать. После некоторого времени, вы решили двигаться дальше.")
    print("Вы продолжаете свое приключение в Темном Лесу.")

def go_to_dragon_mountain():
    print(f"{Gnome.random_gnome.name} решил отправиться к Драконьей Горе...")
    print("Вы приближаетесь к Драконьей Горе и вдруг видите огромного дракона, спящего на огромной куче золота.")
    print("Что решаете сделать?")
    print("1. Попробовать украсть немного золота, не будя дракона.")
    print("2. Попробовать пройти мимо дракона незамеченным.")
    print("3. Атаковать дракона и попытаться одолеть его.")

    choice = input("Выберите действие (1/2/3): ")

    if choice == "1":
        if random.random() < 0.5:
            print("Вы незаметно украли немного золота и ушли, не разбудив дракона.")
        else:
            print("Ваша попытка украсть золото привлекла внимание дракона. Он проснулся и атаковал вас!")
    elif choice == "2":
        if random.random() < 0.7:
            print("Вы осторожно прошли мимо дракона, не привлекая его внимания.")
        else:
            print("Вы поскользнулись, и шум привлек внимание дракона. Он проснулся и начал гоняться за вами!")
    elif choice == "3":
        print("Вы решительно атакуете дракона. Это смело, но очень опасно!")

        if random.random() < 0.3:
            print("Ваша атака оказалась успешной! Вы одолели дракона и получили его сокровища.")
        else:
            print("Дракон оказался слишком сильным, и он атаковал вас. Ваше приключение закончилось неудачей.")


if __name__ == "__main__":
    main()
    Gnome.random_gnome.save_to_csv()  # save game progress to CSV
