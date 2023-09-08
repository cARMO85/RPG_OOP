import random
from character import Character

def character_fight(type_1, type_2):
    character_1 = Character(type_1)
    character_2 = Character(type_2)
    coin_toss = random.randint(0, 1)
    if coin_toss == 0:
        first, second = [character_1, character_2]
    else:
        first, second = [character_2, character_1]

    while True:
        if attack_character(first, second):
            return str(first)
        if attack_character(second, first):
            return str(second)

def attack_character(first, second):
    damage = first.attack()
    second.take_damage(damage)
    if second.is_dead():
        return True
    return False
