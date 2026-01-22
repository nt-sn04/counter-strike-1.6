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
    def __init__(self, group, nickname):
        self.group = group
        self.nickname = nickname
        self.health = 100
        self.weapons = [Weapon('USP', 200, 12, 5)]
        self.current_weapon = Weapon('USP', 200, 12, 5)
        self.money = 7000

        self.join_message()

    def join_message(self):
        print(f'{self.nickname} has joined to {self.group}')
    
    def shoot(self):
        pass

    def damage(self):
        pass

    def plant_bomb(self):
        pass

    def defuse_bomb(self):
        pass

    def buy_weapon(self, weapon: Weapon):
        if weapon not in self.weapons:
            if self.money >= weapon.price:
                self.weapons.append(weapon)
                self.money -= weapon.price
                print(f'{self.nickname} has bought {weapon.name}')
            else:
                print(f'{self.nickname} has not enough money for {weapon.name}')
        else:
            print(f'{self.nickname} already has {weapon.name}')
