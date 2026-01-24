class Weapon:

    def __init__(self, name, price, ammo, damage):
        self.name = name
        self.price = price
        self.ammo = ammo
        self.damage = damage
    
    def dec_ammo(self):
        if self.ammo > 1:
            self.ammo -= 1
        

class Player:

    def __init__(self, nickname):
        self.nickname = nickname
        self.health = 100
        self.weapons = [Weapon('USP', 200, 12, 5)]
        self.current_weapon = Weapon('USP', 200, 12, 5)
        self.money = 7000

        self.join_message()

    def join_message(self):
        print(f'{self.nickname} has joined to {self.group}')
    
    def shoot(self, player):
        if self.current_weapon.ammo > 0 and self.health > 0 and player.health > 0:
            print(f'{self.nickname} shoot {player.nickname}')
            player.damage(self.current_weapon)
            self.current_weapon.dec_ammo()

    def damage(self, weapon):
        self.health -= weapon.damage
        if self.health <= 0:
            print(f'{self.nickname} has died.')

    def buy_weapon(self, weapon: Weapon):
        if weapon not in self.weapons:
            if self.money >= weapon.price:
                self.weapons.append(weapon)
                self.current_weapon = weapon
                self.money -= weapon.price
                print(f'{self.nickname} has bought {weapon.name}')
            else:
                print(f'{self.nickname} has not enough money for {weapon.name}')
        else:
            print(f'{self.nickname} already has {weapon.name}')


class Terrorist(Player):
    group = 'Terroris'
    
    def plant_bomb(self):
        if self.group == 'Terrorist':
            print(f'{self.nickname} planted bomb')


class CounterTerrorist(Player):
    group = 'Counter-Terroris'

    def defuse_bomb(self):
        if self.group == 'Counter-Terrorist':
            print(f'{self.nickname} defused bomb')
