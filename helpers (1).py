import time
import sys
import random
from heroes import Hero

def generate_enemy():
    monster_name = ['Дикий Гоблин', 'Ядовитый Паук', 'Скелет Воин', 'Зомби', 'Призрак Жителя']
    name = random.choice(monster_name)
    hp = random.randint(30, 70)
    damage = random.randint(5, 12)
    mp = random.randint(40, 75)
    return  Hero(name, hp, damage, mp)
def generate_dan_enemy():
    if random.randint(1,5) == 1:
        return generate_dark_berserk()
    dangerous_monsters = ['Пещерный Тролль', 'Голодный Орк', 'Падший Воин']
    name = random.choice(dangerous_monsters)
    hp  = random.randint(100, 150)
    damage = random.randint(20, 25)
    mp = random.randint(60, 100)
    return Hero(name, hp, damage, mp)
def generate_dark_berserk():
    name  = 'Темный Берсерк'
    hp = 165
    damage = 25
    mp = 200
    return Hero(name, hp, damage, mp)
def generate_boss():
    name = 'Кураи'
    hp = 350
    damage = 50
    mp = 10000000000
    return Hero(name, hp, damage, mp)


def separation():
    print('-----------------')