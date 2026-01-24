class Player:
    health = 100
    money = 7000
    weapons = []

    def __init__(self, group, nickname):
        self.group = group
        self.nickname = nickname
        # self.weapons = []

    def get_weapon(self, weapon):
        self.weapons.append(weapon)


p01 = Player('terrorist', 'ali')
p02 = Player('counter-terrorist', 'vali')


p01.get_weapon('AK-47')
p02.get_weapon('M416')


print(p01.weapons)
print(p02.weapons)
