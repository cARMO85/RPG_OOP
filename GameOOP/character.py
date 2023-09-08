import random
from constants import TYPES

class Character:
    _health = 0
    _attack = 0
    _dodge = 0

    def __init__(self, char_type):
        self._char_type = char_type
        self._assign_attributes()

    def __str__(self):
        return self._char_type

    def _assign_attributes(self):
        type_dict = TYPES[self._char_type]
        self._health = type_dict["health"]
        self._attack = type_dict["attack"]
        self._dodge = type_dict["dodge"]

    def attack(self):
        return self._attack

    def take_damage(self, damage):
        if self._dodge_success():
            return "Missed!"
        self._health -= damage
        return f"{self._char_type} took {damage} damage."

    def _dodge_success(self):
        dodge_chance = self._dodge * 5
        dodge_roll = random.randint(1, 100)
        if dodge_roll <= dodge_chance:
            return True
        return False

    def is_dead(self):
        return self._health <= 0
