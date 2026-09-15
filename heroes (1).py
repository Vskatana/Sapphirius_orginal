
class Hero:
    def __init__(self, name, hp,damage, mp, level = 1, xp = 0, gold = 0):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp
        self.gold = gold
        self.damage = damage
        self.weapon_damage = 0
        self.level = level
        self.xp = xp
        self.has_stone = False
        self.potions = 1
        self.element = False
        self.armor_level = 0
        self.has_broken_armor = False
        self.has_white_blade = False
        self.has_black_blade = False
        self.has_firstborn_armor = False
        self.has_killed_boss = False
        self.weapon_level = 0




    def attack(self, enemy):
        enemy.hp = enemy.hp - self.damage
        #print(f'{self.name} наносит {enemy.name} {self.damage} урона\n{self.name} | HP: {self.hp}\n{enemy.name} | HP: {enemy.hp}')




