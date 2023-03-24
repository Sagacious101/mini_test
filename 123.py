import os
from random import *


class Humanoid:
    def __init__(self, name="существо", hp=20, race="human", damage=5, money=0, inventory=[]):
        self.name = name
        self.hp = hp
        self.race =  race
        self.damage = damage
        self.money = money
        self.inventory = inventory

    def pick_up_item(self, item):
        self.inventory.append(item)

    def show_inventory(self):
        for num, i in enumerate(self.inventory):
            if self.inventory[i].name:
                print(f'{num + 1}.{self.inventory[i].name}')

    def show_humanoid(self):
        print('Характеристики:')
        print(f'Имя: {self.name}')
        print(f'Раса: {self.race}')
        print(f'HP: {self.hp}')
        print(f'Монеты: {self.money}')
        print(f'Урон: {self.damage}')

class Weapon:
    def __init__(self, name=None, damage=0):
        self.name = name
        self.damage = damage

sword_1 = Weapon(name= 'Ржавый меч', damage= 10)
hero = Humanoid(name= 'Вася', money= 15, inventory= [sword_1])
enemy = Humanoid(name='бандит', damage= 1)

def start_fight(hero: Humanoid, enemy: Humanoid) -> None:
    text = "Выберите действие:\n"
    while hero.hp > 0 and enemy.hp > 0:
        os.system("cls")
        hero.show_humanoid
        enemy.show_humanoid
        print(text)
        options = [
            "Атаковать противника"
        ]
        show_option(options)
        option = choose_option(options)
        if option == 0:
            combat_turn(hero, enemy)
        combat_turn(enemy, hero)
        input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)

def combat_turn(attacker: Humanoid, defender: Humanoid) -> None:
    if attacker.damage > 0:
        damage = (attacker.damage)
        defender.hp -= damage
        print(f'{attacker.name} атаковал {defender.name} на {damage}!')

def combat_result(hero: Humanoid, enemy: Humanoid) -> None:
    os.system("cls")
    if hero.hp > 0 and enemy.hp <= 0:
        print(f'{hero.name} победил {enemy.name} и в награду получает:')
        hero.money += enemy.money
        print(f'{enemy.money} монет')
        input("Нажмите ENTER чтобы продолжить: ")
    else:
        print("Вы умерли")

def show_option(options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")


def choose_option(options: list) -> int:
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:
        print("\nВвод должен быть целым неотрицательным числом")
        return choose_option(options)
    else: 
        if option <= len(options) - 1 and option > -1:
            return option
        else:
            print("Нет такого выбора")
            return choose_option(options)

start_fight(hero, enemy)
hero.show_humanoid