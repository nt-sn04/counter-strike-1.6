# counter-strike-1.6

Bu OOP ni yaxshiroq tushunish uchun yaratilgan Counter-Strike 1.6 o'yinining soddalashtirilgan versiyasidir.

## O'yin haqida
Counter-Strike 1.6 - bu ko'p o'yinchi birinchi shaxs otish o'yini bo'lib, unda o'yinchilar teroristlar va kontr-terroristlar bo'lib, teroristlar o'yin davomida bombani joylashtirishga harakat qiladi, kontr-terroristlar esa teroristlarni to'xtatishga harakat qiladi.

# class

- Player:
    - attributes:
        - group: Terrorist, Counter-Terrorist
        - nickname
        - health
        - weapons
        - money
    - methods:
        - shoot
        - damage
        - planned_bomb
        - defuse_bomb

- Weapon:
    - attributes:
        - name
        - price
        - ammo
        - damage

    - methods:
        - dec_ammo
