import random
from objects import Weapon, Player


def main():
    weapons = [
        Weapon('M416', 5000, 30, 15),
        Weapon('AK-47', 3000, 30, 10),
        Weapon('AWP', 5000, 10, 30),
    ]

    t01 = Player('Terrorist', 'kobra')
    t02 = Player('Terrorist', 'tiger')

    ct01 = Player('Counter-Terrorist', 'hunter')
    ct02 = Player('Counter-Terrorist', 'elephand')

    t01.buy_weapon(random.choice(weapons))
    t01.buy_weapon(random.choice(weapons))
    t02.buy_weapon(random.choice(weapons))
    ct01.buy_weapon(random.choice(weapons))
    ct02.buy_weapon(random.choice(weapons))

    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)


    ct02.plant_bomb()
    ct01.defuse_bomb()

main()
