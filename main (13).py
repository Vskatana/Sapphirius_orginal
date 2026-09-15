import json
import random
import os
from heroes import Hero
from helpers import generate_enemy, generate_dan_enemy, generate_dark_berserk, generate_boss, separation
def save_game(player):
    data = {
        'name': player.name,
        'hp': player.hp,
        'max_hp': player.max_hp,
        'damage': player.damage,
        'weapon_damage': player.weapon_damage,
        'mp': player.mp,
        'max_mp': player.max_mp,
        'level': player.level,
        'xp': player.xp,
        'gold': player.gold,
        'has_stone': player.has_stone,
        'potions': player.potions,
        'element': player.element,
        'armor_level': player.armor_level,
        'weapon_level': player.weapon_level,
        'has_broken_armor': player.has_broken_armor,
        'has_white_blade': player.has_white_blade,
        'has_black_blade': player.has_black_blade,
        'has_firstborn_armor': player.has_firstborn_armor,
        'has_killed_boss': player.has_killed_boss,
    }
    with open('rpg_save.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_game():
    try:
        with open('rpg_save.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(f'Профиль игрока {data['name']} успешно загружен')
            loaded_hero = Hero(data['name'], data['hp'], data['damage'], data['mp'], gold = data['gold'])
            loaded_hero.max_hp = data.get('max_hp', 100)
            loaded_hero.level = data.get('level', 1)
            loaded_hero.xp = data.get('xp', 0)
            loaded_hero.max_mp = data.get('max_mp', 100)
            loaded_hero.weapon_damage = data.get('weapon_damage', 0)
            loaded_hero.has_stone = data.get('has_stone', False)
            loaded_hero.has_broken_armor = data.get('has_broken_armor', False)
            loaded_hero.element = data.get('element', False)
            loaded_hero.potions = data.get('potions', 1)
            loaded_hero.armor_level = data.get('armor_level', 0)
            loaded_hero.weapon_level = data.get('weapon_level', 0)
            loaded_hero.has_white_blade = data.get('has_white_blade', False)
            loaded_hero.has_black_blade = data.get('has_black_blade', False)
            loaded_hero.has_firstborn_armor = data.get('has_firstborn_armor', False)
            loaded_hero.has_killed_boss = data.get('has_killed_boss', False)
            return loaded_hero

    except FileNotFoundError:
        name = input("Введите имя нового персонажа:")
        return Hero(name,100, 10, 100)
player = load_game()
while True:
    summ_damage = player.weapon_damage + player.damage
    separation()
    print(f'{player.name} | HP: {player.hp} | MP: {player.mp}\nLevel: {player.level} | XP: {player.xp}\nЗолото:{player.gold}--- ')
    print("1 - исследовать лес\n2 - пойти в неизвестное\n3 - пойти в Заброшенный Замок\n4 - магазин\n5 - сохранить и выйти")
    choice1 = input("Выберите путь:")
    if choice1 == '5' :
        save_game(player)
        print('До встречи')
        break
    elif choice1 == '4':
        separation()
        print('Добро пожаловать в оружейную лавку 🗡')
        print(f'Ваш текущий урон: {summ_damage}')
        print(f'Ваше текущее количество золота: {player.gold}')
        print(f'Разделы:\nОружие\nДоспехи\nЗелья\nМагические предметы')
        separation()
        choice2 = input('1 - Оружие\n2 - Доспехи\n3 - Зелья\n4 - Магические предметы\n5 - Выйти\n')
        if choice2 == '1':
            choice_weapon = input('Каталог оружия:\n1 - Острый Топор (150 золота)\n2 - Отточенный Клинок (300 золота)\n3 - Катана Ронина (555 золота)\n4 - Секира Подземных Существ (700 золота)\n5 - Белый Клинок Равновесия (1000 золота)\n6 - Выйти\n')
            if choice_weapon == '1':
                if player.weapon_level > 1:
                    print('У вас уже есть оружие лучше этого')
                if player.weapon_level == 1:
                    print('Вы уже купили топор!')
                else:
                    axe_choice = input('Вы хотите купить Острый Топор (150 золота | Урон: 7)?\n1 - да\n2 - нет\n')
                    if axe_choice == '1':
                        if player.gold >= 150:
                           player.gold -= 150
                           player.weapon_damage = 7
                           player.weapon_level = 1
                           print('Вы купили Острый Топор')
                        elif player.gold < 150:
                           print("У тебя мало золота")
                        else:
                           print('Неверный ввод')
                    elif axe_choice == '2':
                        print("Вы отказались")
                    else:
                        print('Неверный ввод')
            elif choice_weapon == '2':
                if player.weapon_level > 2:
                    print('У вас уже есть оружие лучше этого')
                if player.weapon_level == 2:
                    print('Вы уже купили клинок!')
                else:
                    sword_choice = input('Вы хотите купить Отточенный Клинок (300 золота | Урон: 15)?\n1 - да\n2 - нет\n')
                    if sword_choice == '1':
                        if player.gold >= 300:
                           player.gold -= 300
                           player.weapon_damage = 15
                           player.weapon_level = 2
                           print('Вы купили Отточенный Клинок')
                        elif player.gold < 300:
                           print("У тебя мало золота")
                        else:
                           print('Неверный ввод')
                    elif sword_choice == '2':
                        print("Вы отказались")
                    else:
                        print('Неверный ввод')
            elif choice_weapon == '3':
                if player.weapon_level > 3:
                    print('У вас уже есть оружие лучше этого')
                if player.weapon_level == 3:
                    print('Вы уже купили катану!')
                else:
                    choice_katana = input('Вы хотите купить Катана Ронина (555 золота | Урон: 23)?\n1 - да\n2 - нет\n')
                    if choice_katana == '1':
                        if player.gold >= 555:
                           player.gold -= 555
                           player.weapon_damage = 23
                           player.weapon_level = 3
                           print('Вы купили Катана Ронина')
                        elif player.gold < 555:
                           print("У тебя мало золота")
                        else:
                           print('Неверный ввод')
                    elif choice_katana == '2':
                        print("Вы отказались")
                    else:
                        print('Неверный ввод')
            elif choice_weapon == '4':
                if player.weapon_level > 4:
                    print('У вас уже есть оружие лучше этого')
                if player.weapon_level == 4:
                    print('Вы уже купили секиру!')
                else:
                    choice_ax = input('Вы хотите купить Секира Подземных Существ (700 золота | Урон: 30)?\n1 - да\n2 - нет\n')
                    if choice_ax == '1':
                        if player.gold >= 700:
                           player.gold -= 700
                           player.weapon_damage = 30
                           player.weapon_level = 4
                           print('Вы купили Секира Подземных Существ')
                        elif player.gold < 700:
                           print("У тебя мало золота")
                        else:
                           print('Неверный ввод')
                    elif choice_ax == '2':
                        print("Вы отказались")
                    else:
                        print('Неверный ввод')
            elif choice_weapon == '5':
                if player.weapon_level > 5:
                    print('У вас уже есть оружие лучше этого')
                if player.weapon_level == 5:
                    print('Вы уже купили клинок!')
                else:
                    choice_white_blade = input('Вы хотите купить Белый Клинок Равновесия (1000 золота | Урон: 20)?\nПримечание: Кузнец рассказывает вам легенду, что где-то под землей хранится точно такой же клинок, но только черный. Говорят, что этот черный клинок полная противоположность белому, и если использовать сразу два клинка, то их эффективность полностью раскроется. Эти клинки принадлежали Перворожденному, в них заточена сила двух сторон.\n1 - да\n2 - нет\n')
                    if choice_white_blade == '1':
                        if player.gold >= 1000 and player.has_black_blade == True:
                            player.gold -= 1000
                            player.has_white_blade = True
                            player.weapon_level = 5
                            player.weapon_damage = 45
                            print('Вы купили Белый Клинок Равновесия\nВы вспоминаете про неизвестный черный клинок, который получили с убийства Темного Берсерка\nВы решаетесь взять оба клинка в руки...И в этот миг хаос внутри вас затихает. Холод Черного Клинка и Тепло Белого смешиваются у вас в центре груди, превращаясь в идеальный баланс.\nВы слышите в своей голове чей-то шепот...\n!Братья воссоединились!')

                        elif player.gold >= 1000 and player.has_black_blade == False:
                            if player.weapon_level > 2:
                                player.gold -= 1000
                                player.has_white_blade = True
                                print('Вы купили Белый Клинок Равновесия, но он показался вам слишком слабым и вы решили пока не использовать его')
                            elif player.weapon_level < 3:
                                player.gold -= 1000
                                player.has_white_blade = True
                                player.weapon_damage = 20
                                print('Вы купили Белый Клинок Равновесия\nВы почувствовали приятное тепло в руке...')
                        else:
                           print('Неверный ввод')
                    elif choice_white_blade == '2':
                        print("Вы отказались")
                    else:
                        print('Неверный ввод')


            elif choice_weapon == '6':
                print('Вы вышли')
            else:
                print('Неверный ввод или недостаточно средств')
        elif choice2 == '2':
                choice_armor = input('Каталог доспехов:\n1 - Кожаный Костюм (150 золота)\n2 - Стальные Доспехи (300 золота)\n3 - Титановый Панцирь (500 золота)\n4 - Броня 4-х Ветров (750 золота)\n5 - Доспехи Перворожденного (1000 золота)\n6 - Выйти\n')
                if choice_armor == '1':
                    if player.armor_level == 1:
                        print('У вас уже есть этот костюм')
                    elif player.armor_level > 1:
                        print('У вас имеются доспехи лучше этих')
                    else:
                        choice_leather_suit = input('Вы хотите купить Кожаный Костюм (150 золота | Защита: 5%)?\n1 - да\n2 - нет\n')
                        if choice_leather_suit == '1':
                            if player.gold >= 150:
                                player.gold -= 150
                                print('Вы купили Кожаный Костюм')
                                player.armor_level = 1
                            else:
                                print('Недостаточно золота или неверный ввод')
                        elif choice_leather_suit == '2':
                            print('Вы отказались')
                elif choice_armor == '2':
                    if player.armor_level == 2:
                        print('У вас уже есть эти доспехи')
                    elif player.armor_level > 2:
                        print('У вас имеются доспехи лучше этих')
                    else:
                        choice_steel_armor = input('Вы хотите купить Стальные Доспехи (300 золота | Защита: 15%)?\n1 - да\n2 - нет\n')
                        if choice_steel_armor == '1':
                            if player.gold >= 300:
                                player.gold -= 300
                                print('Вы купили Стальные Доспехи')
                                player.armor_level = 2
                            else:
                                print('Недостаточно золота или неверный ввод')
                        elif choice_steel_armor == '2':
                            print('Вы отказались')
                elif choice_armor == '3':
                    if player.armor_level == 3:
                        print('У вас уже есть эти доспехи')
                    elif player.armor_level > 3:
                        print('У вас имеются доспехи лучше этих')
                    else:
                        choice_titanium_armor = input('Вы хотите купить Титановый Панцирь (500 золота | Защита: 25%)?\n1 - да\n2 - нет\n')
                        if choice_titanium_armor == '1':
                            if player.gold >= 500:
                                player.gold -= 500
                                print('Вы купили Титановый Панцирь')
                                player.armor_level = 3
                            else:
                                print('Недостаточно золота или неверный ввод')
                        elif choice_titanium_armor == '2':
                            print('Вы отказались')
                elif choice_armor == '4':
                    if player.armor_level == 4:
                        print('У вас уже есть эти доспехи')
                    elif player.armor_level > 4:
                        print('У вас имеются доспехи лучше этих')
                    else:
                        choice_windy_armor = input('Вы хотите купить Броню 4-х Ветров (750 золота | Защита: 40%)?\n1 - да\n2 - нет\n')
                        if choice_windy_armor == '1':
                            if player.gold >= 750:
                                player.gold -= 750
                                print('Вы купили Броню 4-х Ветров')
                                player.armor_level = 4
                            else:
                                print('Недостаточно золота или неверный ввод')
                        elif choice_windy_armor == '2':
                            print('Вы отказались')
                elif choice_armor == '5':
                    if player.armor_level == 5:
                        print('У вас уже есть эти доспехи')
                    elif player.armor_level > 5:
                        print('У вас имеются доспехи лучше этих')
                    else:
                        choice_firstborn_armor = input('Вы хотите купить Доспехи Перворожденного (1000 золота | Защита: 60%)?\nПримечание: Кузнец предупреждает, что доспехи поломаны.\nДля починки нужна астатиевая руда, которую находили последний раз 300 лет назад. Сейчас это просто груда тяжелого древнего металла\n1 - да\n2 - нет\n')
                        if choice_firstborn_armor == '1':
                            if player.gold >= 1000 and player.has_stone == True:
                                player.gold -= 1000
                                player.has_stone = False
                                print('Вы приобрели Доспехи Перворожденного...\nВаш рюкзак начинает светиться и трястись\nИз вашего рюкзака выскакивает Таинственнный Камень и с треском врезается в центр сломанного нагрудника. Камень превращается в жидкий свет и заполняет трещины и сколы на броне. Старый металл перерождается, вспыхивая лазурным пламенем.\n!Легендарные Доспехи Перворожденного полностью восстановлены!')
                                player.has_firstborn_armor = True
                                player.armor_level = 5
                            elif player.gold >= 1000 and player.has_stone == False:
                                player.gold -= 1000
                                player.has_broken_armor = True
                                print('Вы отдали кузнецу 1000 золота за сломанную броню')
                                print('Вы пытаетесь примерить ее, но она начинает разваливаться')
                            else:
                                print('Недостаточно золота или неверный ввод')
                        elif choice_firstborn_armor == '2':
                            print('Вы отказались')
                elif choice_armor == '6':
                    print('Вы вышли')


        elif choice2 == '3':
            choice_potions = input('Каталог зелий:\n1 - Лечебное Зелье (50 золота)\n2 - Выйти\n')
            if choice_potions == '1':
                potion_hp_choice = input('Вы хотите купить "Лечебное зелье"(50 золота)?\n1 - да\n2 - нет\n')
                if potion_hp_choice == '1':
                    if player.gold >= 50:
                        player.gold -= 50
                        print('Вы купили Лечебное зелье')
                        player.potions += 1
                    else:
                        print('У тебя мало золота')
                elif potion_hp_choice == '2':
                    print('Вы отказались')
                else:
                    print('Неверный ввод или недостаточно средств')
        elif choice2 == '4':
            choice_magic_item = input('Каталог Магических предметов:\n1 - Книга Стихий (400 золота)\n2 - Таинственный Камень (1000 золота)\n3 - Выйти\n')
            if choice_magic_item == '1':
                if player.element != False:
                    print('Вы уже познали магию стихий')
                else:
                    element_list = ["Огонь", "Земля", "Молния", "Лед", "Жизнь"]
                    element_choice = input(f'Вы хотите купить "Книга стихий"(400 золота)?\nВам может выпасть следующее:{element_list}\n1 - да\n2 - нет\n')
                    if element_choice == '1':
                        if player.gold >= 400:
                            player.gold -= 400
                            player.element = random.choices(element_list, weights=[24,24,24,24,4])[0]
                            print(f'Книга стихий вспыхнула у вас в руках\nВнутри вас пробудилась сила стихий: {player.element}')
                            if player.element == 'Жизнь':
                                print('Вы познали саму сущность бытия')
                    elif element_choice == '2':
                        print('Вы отказались')
            elif choice_magic_item == '2':
                stone_choice = input('Вы хотите купить "Таинственный Камень"(1000 золота)?\n1 - да\n2 - нет\n')
                if stone_choice == '1':
                    if player.has_stone == True:
                        print('Вы уже купили Таинственный Камень')
                    else:
                        if player.gold >= 1000:
                            player.gold -= 1000
                            if player.has_broken_armor == False:
                                player.has_stone = True
                                print('Вы купили Таинственный Камень...')
                            elif player.has_broken_armor == True:
                                player.armor_level = 5
                                player.has_stone = False
                                player.has_broken_armor = False
                                print('Вы купили Таинственный Камень...\nВы берете его в руки, но при этом чувствуете, как ваш рюкзак начинает светиться и трястись\nКамень выскакивает из ваших рук, летит к вашему рюкзаку, пробивает его и сливается с Доспехами Перворожденного\nТрещины и сколы в доспехах заполняются жидким светом\nСтарый металл перерождается, вспыхивая лазурным пламенем\n!Легендарные Доспехи Перворожденного полностью восстановлены!')
                                player.has_firstborn_armor = True
                        else:
                            print('У тебя мало золота')
                elif stone_choice == '2':
                    print('Вы отказались')
                else:
                    print('Неверный ввод или недостаточно средств')

        elif choice2 == '5':
            print('Вы вышли')


    elif choice1 == '1':
        enemy = generate_enemy()
        separation()
        print(f'Вы встретили врага: {enemy.name} (HP:{enemy.hp})')

        while player.hp > 0 and enemy.hp > 0:
            choice3 = input('Выберите действие:\n1 - атаковать\n2 - использовать магию стихий (20 маны)\n3 - выпить лечебное зелье\n4 - попытаться сбежать\n')
            if choice3 == '1':
               summ_damage = player.weapon_damage + player.damage
               enemy.hp -= summ_damage
               print(f'{player.name} наносит {enemy.name} {summ_damage} урона')
               if enemy.hp > 0:
                   damage_taken = enemy.damage
                   if player.armor_level == 0:
                       pass
                   elif player.armor_level == 1:
                       damage_taken = int(damage_taken * 0.95)
                   elif player.armor_level == 2:
                       damage_taken = int(damage_taken * 0.85)
                   elif player.armor_level == 3:
                       damage_taken = int(damage_taken * 0.75)
                   elif player.armor_level == 4:
                       damage_taken = int(damage_taken * 0.60)
                   elif player.armor_level == 5:
                       damage_taken = int(damage_taken * 0.40)
                   player.hp -= damage_taken
                   print(f'{enemy.name} наносит {player.name} {damage_taken} урона')
                   separation()
                   print(f'{player.name} | HP: {player.hp}')
                   print(f'{enemy.name} | HP: {enemy.hp}')
                   separation()
               if enemy.hp <= 0:
                 loot = random.randint(1000000, 10000000)
                 player.gold += loot
                 player.xp += 40
                 player.mp = player.max_mp
                 print(f'Вы победили врага, вам зачислили {loot} золота\nВам зачислили 40 XP')
                 if player.xp >= 100:
                    player.level += 1
                    player.xp -= 100
                    player.max_hp += 20
                    player.hp = player.max_hp
                    player.max_mp += 10
                    player.mp = player.max_mp
                    player.damage += 1
                    print(f'Вы повысили уровень, ваши характеристики выросли\nВаш текущий уровень - {player.level}')
            elif choice3 == '2':
                if player.element == False:
                    print('Вы не обладаете силой стихий')
                else:
                    if player.mp < 20:
                        print('У вас недостаточно маны')
                    elif player.mp >= 20:
                        player.mp -= 20
                        if player.element == "Огонь":
                            enemy.hp -= 45
                            print('Заклинание:🔥Огненный Шар🔥')
                            print('Из вас вырывается сила огня\nВраг окутан пламенем\nНанесено 45 урона')
                        elif player.element == "Земля":
                            enemy.hp -= 35
                            print('Заклинание:🌍Землетресение🌍')
                            print('Земля начинает дрожать под ногами\nЗемля уходит из-под ног врага\nНанесено 35 урона')
                        elif player.element == "Молния":
                            lighting_dam = random.randint(20, 60)
                            enemy.hp -= lighting_dam
                            print('Заклинание:⚡Вспышка Молнии⚡')
                            print(f'Ваши руки заряжены электричеством\nМолния сокрушает врага на {lighting_dam} урона')
                        elif player.element == "Лед":
                            enemy.hp -= 25
                            player.hp += 15
                            if player.hp > player.max_hp:
                                player.hp = player.max_hp
                            print('Заклинание:❄Ледяные Оковы❄')
                            print('Вы окутываете врага ледяными оковами\nВраг заморожен на 25 урона, а вы восстанавливаете 15 HP')
                        elif player.element == "Жизнь":
                            enemy.hp -= 30
                            player.hp += 45
                            if player.hp > player.max_hp:
                                player.hp = player.max_hp
                            print('Легендарное заклинание:🌱Переизбыток Жизни🌱')
                            print('Вы насыщаете врага эссенцией жизни - ему становится плохо\nВраг разлагается на 30 урона, тем временем вы восстанавливаете 45 HP')
                        if enemy.hp > 0:
                            damage_taken = enemy.damage
                            if player.armor_level == 0:
                                pass
                            elif player.armor_level == 1:
                                damage_taken = int(damage_taken * 0.95)
                            elif player.armor_level == 2:
                                damage_taken = int(damage_taken * 0.85)
                            elif player.armor_level == 3:
                                damage_taken = int(damage_taken * 0.75)
                            elif player.armor_level == 4:
                                damage_taken = int(damage_taken * 0.60)
                            elif player.armor_level == 5:
                                damage_taken = int(damage_taken * 0.40)
                            player.hp -= damage_taken
                            print(f'{enemy.name} наносит {player.name} {damage_taken} урона')
                            separation()
                            print(f'{player.name} | HP: {player.hp}')
                            print(f'{enemy.name} | HP: {enemy.hp}')
                            separation()
                        if enemy.hp <= 0:
                            loot = random.randint(1000, 1000)
                            player.gold += loot
                            player.xp += 40
                            player.mp = player.max_mp
                            print(f'Вы победили врага, вам зачислили {loot} золота\nВам зачислили 40 XP')
                            if player.xp >= 100:
                                player.level += 1
                                player.xp -= 100
                                player.max_hp += 20
                                player.hp = player.max_hp
                                player.max_mp += 10
                                player.mp = player.max_mp
                                player.damage += 1


            elif choice3 == '3':
                if player.potions > 0:
                    player.hp += 40
                    player.potions -= 1
                    print('Вы выпили лечебное зелье')
                    if player.hp > player.max_hp:
                        player.hp = player.max_hp
                else:
                    print('У вас нету зелий')
            elif choice3 == '4':
                escape = random.randint(1, 2)
                if escape == 1:
                    print('Вы трусливо сбежали с поля боя')
                    break
                elif escape == 2:
                    if enemy.hp > 0 and player.hp > 0:
                        damage_taken = enemy.damage
                        if player.armor_level == 0:
                            pass
                        elif player.armor_level == 1:
                            damage_taken = int(damage_taken * 0.95)
                        elif player.armor_level == 2:
                            damage_taken = int(damage_taken * 0.85)
                        elif player.armor_level == 3:
                            damage_taken = int(damage_taken * 0.75)
                        elif player.armor_level == 4:
                            damage_taken = int(damage_taken * 0.60)
                        elif player.armor_level == 5:
                            damage_taken = int(damage_taken * 0.40)
                        player.hp -= damage_taken
                        print(f'Побег не удался, монстр перекрыл вам путь и нанес {damage_taken} урона')




    elif choice1 == '2':
        print('Вы пошли в неизвестное...')
        dan_enemy = generate_dan_enemy()
        dark_berserk = generate_dark_berserk()
        separation()
        print(f'Вы встретили врага: {dan_enemy.name} (HP:{dan_enemy.hp})')

        while player.hp > 0 and dan_enemy.hp > 0:
            choice3 = input('Выберите действие:\n1 - атаковать\n2 - использовать магию стихий (20 маны)\n3 - выпить лечебное зелье\n4 - попытаться сбежать\n')
            if choice3 == '1':
                summ_damage = player.weapon_damage + player.damage
                dan_enemy.hp -= summ_damage
                print(f'{player.name} наносит {dan_enemy.name} {summ_damage} урона')
                if dan_enemy.hp > 0:
                    damage_taken = dan_enemy.damage
                    if player.armor_level == 0:
                        pass
                    elif player.armor_level == 1:
                        damage_taken = int(damage_taken * 0.95)
                    elif player.armor_level == 2:
                        damage_taken = int(damage_taken * 0.85)
                    elif player.armor_level == 3:
                        damage_taken = int(damage_taken * 0.75)
                    elif player.armor_level == 4:
                        damage_taken = int(damage_taken * 0.60)
                    elif player.armor_level == 5:
                        damage_taken = int(damage_taken * 0.40)
                    player.hp -= damage_taken
                    print(f'{dan_enemy.name} наносит {player.name} {damage_taken} урона')
                    separation()
                    print(f'{player.name} | HP: {player.hp}')
                    print(f'{dan_enemy.name} | HP: {dan_enemy.hp}')
                    separation()
                if dan_enemy.hp <= 0:
                    loot = random.randint(35, 60)
                    player.gold += loot
                    player.xp += 80
                    player.mp = player.max_mp
                    print(f'Вы победили  опасного врага, вам зачислили {loot} золота\nВам зачислили 80 XP')
                    if player.xp >= 100:
                        player.level += 1
                        player.xp -= 100
                        player.max_hp += 20
                        player.hp = player.max_hp
                        player.max_mp += 10
                        player.mp = player.max_mp
                        player.damage += 1
                        print(f'Вы повысили уровень, ваши характеристики выросли\nВаш текущий уровень - {player.level}')
                    separation()
                    if dan_enemy.name == "Темный Берсерк":
                        if random.randint(1, 2) == 2:
                            if player.has_white_blade == True:
                                player.has_black_blade = True
                                player.weapon_level = 5
                                player.weapon_damage = 45
                                print('После убийства Темного Берсерка, вы замечаете на земле темный клинок, похожий на Белый Клинок Равновесия\nВы решаетесь взять оба клинка в руки...И в этот миг хаос внутри вас затихает. Холод Черного Клинка и Тепло Белого смешиваются у вас в центре груди, превращаясь в идеальный баланс.\nВы слышите в своей голове чей-то шепот...\n!Братья воссоединились!')
                            else:
                                player.has_black_blade = True
                                if player.weapon_level > 2:
                                    print('После убийства Темного Берсерка, вы видите на земле темный клинок\nВы решаетесь оставить его как реликвию')
                                elif player.weapon_level < 3:
                                    player.weapon_damage = 20
                                    print('После того, как вы победили Темного Берсерка, вы замечаете на земле темный клинок\nВы решаете взять его и осмотреть, но чувствуете непонятный холод в груди, будто чего-то не хватает.\nУ вас появляется желание использовать его как основное оружие')

            elif choice3 == '2':
                if player.element == False:
                    print('Вы не обладаете силой стихий')
                else:
                    if player.mp < 20:
                        print('У вас недостаточно маны')
                    elif player.mp >= 20:
                        player.mp -= 20
                        if player.element == "Огонь":
                            dan_enemy.hp -= 45
                            print('Заклинание:🔥Огненный Шар🔥')
                            print('Из вас вырывается сила огня\nВраг окутан пламенем\nНанесено 45 урона')
                        elif player.element == "Земля":
                            dan_enemy.hp -= 35
                            print('Заклинание:🌍Землетресение🌍')
                            print('Земля начинает дрожать под ногами\nЗемля уходит из-под ног врага\nНанесено 35 урона')
                        elif player.element == "Молния":
                            lighting_dam = random.randint(20, 60)
                            dan_enemy.hp -= lighting_dam
                            print('Заклинание:⚡Вспышка Молнии⚡')
                            print(f'Ваши руки заряжены электричеством\nМолния сокрушает врага на {lighting_dam} урона')
                        elif player.element == "Лед":
                            dan_enemy.hp -= 25
                            player.hp += 15
                            if player.hp > player.max_hp:
                                player.hp = player.max_hp
                            print('Заклинание:❄Ледяные Оковы❄')
                            print(
                                'Вы окутываете врага ледяными оковами\nВраг заморожен на 25 урона, а вы восстанавливаете 15 HP')
                        elif player.element == "Жизнь":
                            dan_enemy.hp -= 30
                            player.hp += 45
                            if player.hp > player.max_hp:
                                player.hp = player.max_hp
                            print('Легендарное заклинание:🌱Переизбыток Жизни🌱')
                            print(
                                'Вы насыщаете врага эссенцией жизни - ему становится плохо\nВраг разлагается на 30 урона, тем временем вы восстанавливаете 45 HP')
                        if dan_enemy.hp > 0:
                            damage_taken = dan_enemy.damage
                            if player.armor_level == 0:
                                pass
                            elif player.armor_level == 1:
                                damage_taken = int(damage_taken * 0.95)
                            elif player.armor_level == 2:
                                damage_taken = int(damage_taken * 0.85)
                            elif player.armor_level == 3:
                                damage_taken = int(damage_taken * 0.75)
                            elif player.armor_level == 4:
                                damage_taken = int(damage_taken * 0.60)
                            elif player.armor_level == 5:
                                damage_taken = int(damage_taken * 0.40)
                            player.hp -= damage_taken
                            print(f'{dan_enemy.name} наносит {player.name} {damage_taken} урона')
                            separation()
                            print(f'{player.name} | HP: {player.hp}')
                            print(f'{dan_enemy.name} | HP: {dan_enemy.hp}')
                            separation()
                        if dan_enemy.hp <= 0:
                            loot = random.randint(50, 75)
                            player.gold += loot
                            player.xp += 80
                            player.mp = player.max_mp
                            print(f'Вы победили врага, вам зачислили {loot} золота\nВам зачислили 80 XP')
                            if player.xp >= 100:
                                player.level += 1
                                player.xp -= 100
                                player.max_hp += 20
                                player.hp = player.max_hp
                                player.max_mp += 10
                                player.mp = player.max_mp
                                player.damage += 1
                            if dan_enemy.name == "Темный Берсерк":
                                if random.randint(1, 2) == 2:
                                    if player.has_white_blade == True:
                                        player.has_black_blade = True
                                        player.weapon_level = 5
                                        player.weapon_damage = 45
                                        print(
                                            'После убийства Темного Берсерка, вы замечаете на земле темный клинок, похожий на Белый Клинок Равновесия\nВы решаетесь взять оба клинка в руки...И в этот миг хаос внутри вас затихает. Холод Черного Клинка и Тепло Белого смешиваются у вас в центре груди, превращаясь в идеальный баланс.\nВы слышите в своей голове чей-то шепот...\n!Братья воссоединились!')
                                    else:
                                        player.has_black_blade = True
                                        if player.weapon_level > 2:
                                            print('После убийства Темного Берсерка, вы видите на земле темный клинок\nВы решаетесь оставить его как реликвию')
                                        elif player.weapon_level < 3:
                                            player.weapon_damage = 20
                                            print('После того, как вы победили Темного Берсерка, вы замечаете на земле темный клинок\nВы решаете взять его и осмотреть, но чувствуете непонятный холод в груди, будто чего-то не хватает.\nУ вас появляется желание использовать его как основное оружие')

            elif choice3 == '3':
                if player.potions > 0:
                    player.hp += 40
                    player.potions -= 1
                    print('Вы выпили лечебное зелье')
                    if player.hp > player.max_hp:
                        player.hp = player.max_hp
                else:
                    print('У вас нету зелий')
            elif choice3 == '4':
                escape = random.randint(1, 2)
                if escape == 1:
                    print('Вы трусливо сбежали с поля боя')
                    break
                elif escape == 2:
                    if dan_enemy.hp > 0 and player.hp > 0:
                        damage_taken = dan_enemy.damage
                        if player.armor_level == 0:
                            pass
                        elif player.armor_level == 1:
                            damage_taken = int(damage_taken * 0.95)
                        elif player.armor_level == 2:
                            damage_taken = int(damage_taken * 0.85)
                        elif player.armor_level == 3:
                            damage_taken = int(damage_taken * 0.75)
                        elif player.armor_level == 4:
                            damage_taken = int(damage_taken * 0.60)
                        elif player.armor_level == 5:
                            damage_taken = int(damage_taken * 0.40)
                        player.hp -= damage_taken
                        print(f'Побег не удался, монстр перекрыл вам путь и нанес {damage_taken} урона')
    elif choice1 == '3':
        if player.level < 10:
            print('Вы слишком слабы для этого места, приходите когда достигнете 10 уровня')
        elif player.has_killed_boss == True:
            print('Вы разгуливаете по заброшенному замку, но кроме красивого вида ничего не находите')
        else:
            print('Вы пошли в Заброшенный Замок...')
            print('Когда-то ходили слухи, что здесь жил Перворожденный со своей избранницей Кураи. После смерти Перворожденного Кураи очень сильно загрустила. Она была воплощением дисциплины и спокойствия, но и это не помогло. Когда слеза Кураи падала на Землю, в мире начинал происходить хаос и он рушился. В итоге Кураи ушла из замка, а внутри него обнаружили статую неизвестного существа. Когда же человек долго смотрел на эту статую, разум его темнел, и он со временем становился безжизненным, будто у него забирали всю энергию.')
            print('Вы исследуете замок и находите ту самую статую\nВам становится не по себе')
            choice_statue = input('Дотронуться до статуи?\n1 - да\n2 - нет\n')
            if choice_statue == '2':
                print('Вы решили не дотрагиваться до статуи и исследовать замок. По пути вы смотрите на картины и замечаете картину, на которой изображено что-то нечеловеческое, что очень похоже на демона')
                print('После исследования замка вы решаетесь уйти')
            elif choice_statue == '1':
                print('Вы решаетесь дотронуться до статуи...')
                boss = generate_boss()
                print('Вам не стоило дотрагиваться до статуи...\nКаменная статуя начала рассыпаться,оказывается вы пробудили то Неизвестное Существо...')
                print(f'Неизвестное существо:\nHP | {boss.hp}\nDM | {boss.damage}\nMP | {boss.mp}')
                while player.hp > 0 and boss.hp > 0:
                    choice3 = input('Выберите действие:\n1 - атаковать\n2 - использовать магию стихий (20 маны)\n3 - выпить лечебное зелье\n4 - попытаться сбежать\n')
                    if choice3 == '1':
                        summ_damage = player.weapon_damage + player.damage
                        boss.hp -= summ_damage
                        print(f'{player.name} наносит Неизвестное Существо {summ_damage} урона')
                    elif choice3 == '2':
                        if player.element == False:
                            print('Вы не обладаете силой стихий')
                            continue
                        else:
                            if player.mp < 20:
                                print('У вас недостаточно маны')
                                continue
                            elif player.mp >= 20:
                                player.mp -= 20
                                if player.element == "Огонь":
                                    boss.hp -= 45
                                    print('Заклинание:🔥Огненный Шар🔥')
                                    print('Из вас вырывается сила огня\nВраг окутан пламенем\nНанесено 45 урона')
                                elif player.element == "Земля":
                                    boss.hp -= 35
                                    print('Заклинание:🌍Землетресение🌍')
                                    print(
                                        'Земля начинает дрожать под ногами\nЗемля уходит из-под ног врага\nНанесено 35 урона')
                                elif player.element == "Молния":
                                    lighting_dam = random.randint(20, 60)
                                    boss.hp -= lighting_dam
                                    print('Заклинание:⚡Вспышка Молнии⚡')
                                    print(
                                        f'Ваши руки заряжены электричеством\nМолния сокрушает врага на {lighting_dam} урона')
                                elif player.element == "Лед":
                                    boss.hp -= 25
                                    player.hp += 15
                                    if player.hp > player.max_hp:
                                        player.hp = player.max_hp
                                    print('Заклинание:❄Ледяные Оковы❄')
                                    print(
                                        'Вы окутываете врага ледяными оковами\nВраг заморожен на 25 урона, а вы восстанавливаете 15 HP')
                                elif player.element == "Жизнь":
                                    boss.hp -= 30
                                    player.hp += 45
                                    if player.hp > player.max_hp:
                                        player.hp = player.max_hp
                                    print('Легендарное заклинание:🌱Переизбыток Жизни🌱')
                                    print(
                                        'Вы насыщаете врага эссенцией жизни - ему становится плохо\nВраг разлагается на 30 урона, тем временем вы восстанавливаете 45 HP')
                    elif choice3 == '3':
                        if player.potions > 0:
                            player.hp += 40
                            player.potions -= 1
                            print('Вы выпили лечебное зелье')
                            if player.hp > player.max_hp:
                               player.hp = player.max_hp
                        else:
                            print('У вас нету зелий')
                        continue
                    elif choice3 == '4':
                        print('Вы не смогли сбежать...')
                        if boss.hp > 0 and player.hp > 0:
                            damage_taken = boss.damage
                            if player.armor_level == 0:
                                pass
                            elif player.armor_level == 1:
                                damage_taken = int(damage_taken * 0.95)
                            elif player.armor_level == 2:
                                damage_taken = int(damage_taken * 0.85)
                            elif player.armor_level == 3:
                                damage_taken = int(damage_taken * 0.75)
                            elif player.armor_level == 4:
                                damage_taken = int(damage_taken * 0.60)
                            elif player.armor_level == 5:
                                damage_taken = int(damage_taken * 0.40)
                            player.hp -= damage_taken
                            print(f'Побег не удался, монстр перекрыл вам путь и нанес {damage_taken} урона')
                            continue

                    if boss.hp > 0:
                        damage_taken = boss.damage
                        if player.armor_level == 0:
                            pass
                        elif player.armor_level == 1:
                            damage_taken = int(damage_taken * 0.95)
                        elif player.armor_level == 2:
                            damage_taken = int(damage_taken * 0.85)
                        elif player.armor_level == 3:
                            damage_taken = int(damage_taken * 0.75)
                        elif player.armor_level == 4:
                            damage_taken = int(damage_taken * 0.60)
                        elif player.armor_level == 5:
                            damage_taken = int(damage_taken * 0.40)
                        player.hp -= damage_taken
                        print(f'Неизвестное Существо наносит {player.name} {damage_taken} урона')
                        separation()
                        print(f'{player.name} | HP: {player.hp}')
                        print(f'Неизвестное Существо | HP: {boss.hp}')
                        separation()
                    if boss.hp <= 0:
                        separation()
                        if player.has_white_blade and player.has_black_blade:
                            loot = random.randint(1000, 1500)
                            player.gold += loot
                            player.xp += 600
                            player.mp = player.max_mp
                            player.has_killed_boss = True
                            print(f'Вы победили Неизвестное Существо\nОно смотрит на тебя, ее взор падает на твои Клинки Равновесия и она узнает их\nОна рассказывает историю, что она была спутницей Перворожденного. Когда его время пришло, он оставил ей защищать этот мир от хаоса и удерживать баланс\nОна раскрывает правду: Настоящее имя Перворожденного - Сапфириус\nПерворожденный - это первое существо, родившееся на стыке Света и Тьмы. Именно он сковал эти два клинка, ведь в его венах течет сила двух сторон.\nТакже она подмечает, что у Перворожденного были преемники, но никто не знает где сейчас они и что вы очень похожи на него\n')
                            print('Кураи говорит, что ее время тоже пришло. Она слишком долго была в отчаянии, но наконец-то она воссоеденится с Перворожденным\nНа последок она отдает вам каплю своей силы и  растворяется в воздухе...')
                            print('Игра пройдена...')
                            separation()
                        elif player.has_firstborn_armor == True:
                            loot = random.randint(1000, 1500)
                            player.gold += loot
                            player.xp += 600
                            player.mp = player.max_mp
                            player.has_killed_boss = True
                            print(f'Вы победили Неизвестное Существо\nОно смотрит на тебя, ее взор падает на твою Броню Перворожденного и она узнает ее\nОна рассказывает историю, что она была спутницей Перворожденного. Когда его время пришло, он оставил ей защищать этот мир от хаоса и удерживать баланс\nОна раскрывает правду: Настоящее имя Перворожденного - Сапфириус\nПерворожденный - это первое существо, родившееся на стыке Света и Тьмы. Именно он создал эту броню, ведь в его венах течет сила двух сторон.\nТакже она подмечает, что у Перворожденного были преемники, но никто не знает где они сейчас и что вы очень похожи на него\n')
                            print('Кураи говорит, что ее время тоже пришло. Она слишком долго была в отчаянии, но наконец-то она воссоеденится с Перворожденным\nНа последок она отдает вам каплю своей силы и растворяется в воздухе...')
                            print('Игра пройдена...')
                            separation()
                        else:
                            loot = random.randint(500, 1000)
                            player.gold += loot
                            player.xp += 100
                            player.mp = player.max_mp
                            print(f'Вы победили Неизвестное Существо\nОно смотрит на тебя, но не находит ничего ни в тебе ни в твоей экипировке\nНеизвестное существо превращается в статую')
                        if player.xp >= 100:
                            player.level += 1
                            player.xp -= 100
                            player.max_hp += 20
                            player.hp = player.max_hp
                            player.max_mp += 10
                            player.mp = player.max_mp
                            player.damage += 1
                            print(f'Вы повысили уровень, ваши характеристики выросли\nВаш текущий уровень - {player.level}')
                        separation()
    else:
        print("XX Неверный ввод XX")
    if player.hp <= 0:
        print('Вы погибли')
        if os.path.exists('rpg_save.json'):
            os.remove('rpg_save.json')
        break