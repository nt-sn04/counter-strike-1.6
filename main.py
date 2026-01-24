import random
from objects import Weapon, Terrorist, CounterTerrorist


def main():
    weapons = [
        Weapon('M416', 5000, 30, 15),
        Weapon('AK-47', 3000, 30, 10),
        Weapon('AWP', 5000, 10, 30),
    ]

    t01 = Terrorist('kobra')
    t02 = Terrorist('tiger')

    ct01 = CounterTerrorist('hunter')
    ct02 = CounterTerrorist('elephand')

    t01.buy_weapon(random.choice(weapons))
    t01.buy_weapon(random.choice(weapons))
    t02.buy_weapon(random.choice(weapons))
    ct01.buy_weapon(random.choice(weapons))
    ct02.buy_weapon(random.choice(weapons))

    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)
    t01.shoot(ct02)

    t02.plant_bomb()
    
    ct01.defuse_bomb()

main()
