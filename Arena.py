import random

"""Словарь с вещами: процент к здоровью, процент к урону, процент к защите."""
Things_list = [
            ("Броня когтя дракона", [0.1, 0.02, 0.05]),
            ("Каркас", [0.1, 0.03, 0.03]),
            ("Кольчуга", [0.1, 0.04, 0.025]),
            ("Броня вавилона", [0.1, 0.01, 0.1]),
            ("Сандали Ахилеса", [0.4, 0.015, 0.07]),
            ("Плащ Нимезиды", [0.2, 0.033, 0.06]),
]

"""Имена бойцов."""
warriors_names = ["Ахилес", "Архимед",
                  "Бульдог", "Рыцарь",
                  "Ворон", "Астерикс",
                  "Обеликс", "Панармикс",
                  "Кватериск", "Гватемалорикс",
                  "Илья Муромец", "Соловей Разбойник",
                  "Никита Добрынич", "Змей Горыныч",
                  "Баба Яга", "Кощей бессмертный",
                  "Шут", "Князь Гвидон",
                  "Скороход", "Голландец",
                  ]

"""Лист с базовыми характеристиками здоровье, урон, защита"""
List_base = (200, 100, 10)


class Thing:
    """Класс с вещами"""

    def __init__(self,
                 name: str,
                 health_percent: float,
                 damage_percent: float,
                 armor_percent: float,
                 ) -> None:
        self.name = name
        self.health_percent = health_percent
        self.damage_percent = damage_percent
        self.armor_percent = armor_percent


class Person:
    """Базовый класс."""

    def __init__(self,
                 name: str,
                 health: float,
                 damage: float,
                 armor: float,
                 ) -> None:
        self.name = name + " (Персонаж)"
        self.health = health
        self.damage = damage
        self.armor = armor

    def set_things(self, things):  # применяю вещи к персонажу
        random_index = random.randint(0, len(things) - 1)
        print(f'{self.name} получает: {things[random_index].name}.')
        self.health = (self.health
                       * things[random_index].health_percent + self.health)
        self.damage = (self.damage
                       * things[random_index].damage_percent + self.damage)
        self.armor = (self.armor
                      * things[random_index].armor_percent + self.armor)

    def attack_damage(self, attack):  # расчет урона после аттаки
        return (attack.damage-attack.damage*(self.armor/100))  # величина урона

    def kritikal(self) -> float:
        return 1


class Paladin(Person):
    """Палладин с увеличенным здоровьем и защитой."""

    def __init__(self,
                 name: str,
                 health: float,
                 damage: float,
                 armor: float,
                 ) -> None:
        super().__init__(name, health, damage, armor)
        self.name = name + (" (Паладин)")
        self.health = health*2
        self.armor = armor*2


class Warrior (Person):
    """Воин с увеличенной атакой."""

    def __init__(self,
                 name: str,
                 health: float,
                 damage: float,
                 armor: float,
                 ) -> None:
        super().__init__(name, health, damage, armor)
        self.damage = damage*2
        self.name = name + (" (Воин)")


class Elf (Person):
    """Эльф с броней и уклоном."""

    def __init__(self,
                 name: str,
                 health: float,
                 damage: float,
                 armor: float,
                 ) -> None:
        super().__init__(name, health, damage, armor)
        self.name = name + (" (Эльф)")
        self.armor = armor*2

    def attack_damage(self, attack):  # расчет урона после аттаки
        t = random.randint(0, 1)  # 50 процентный шанс уклониться
        if t != 0:
            Attac_force = attack.damage-attack.damage*(self.armor/100)
        else:
            Attac_force = 0
            print(f'-----------{self.name} уклонился! Урон '
                  'будет равен 0----------')
        return Attac_force


class Russian_Bogatir(Person):
    """Русский богатырь с критическим ударом."""
    def __init__(self,
                 name: str,
                 health: float,
                 damage: float,
                 armor: float,
                 ) -> None:
        super().__init__(name, health, damage, armor)
        self.damage = damage*1.2
        self.name = name + (" (Русский богатырь)")
        self.armor = armor*2
        self.health = health*2

    def kritikal(self):  # 50% шанс крит
        t = random.randint(0, 1)  # 50% шанс крит
        if t != 0:
            krit_damage = 2
            print(f'------{self.name} наносит критический удар!--------')
        else:
            krit_damage = 1
        return krit_damage


"""Cловарь распределения персонажей."""
"""Максимальное число игроков 20 (ограничение по словарб имен)"""
Dict_person = {Person: 2, Paladin: 2, Warrior: 2, Elf: 7, Russian_Bogatir: 3}


def create_things(Things_list: list):
    """Создание спсика вещей things."""

    print("Создаем вещи:")
    things = list()
    for i in Things_list:
        one_thing = Thing(i[0], *i[1])
        print(f'Создан объект: {one_thing.name}:')
        things.append(one_thing)
        print(f'здоровье: +{one_thing.health_percent*100:.1f}%, урон: '
              f'+{one_thing.damage_percent*100:.1f}%, защита: '
              f'+{one_thing.armor_percent*100:.1f}%')
    print()
    print("------------------------Все объекты созданы----------------------")
    print()
    return things


def create_warriors(warriors_names, things):
    """Создание бойцов."""

    All_warriors = list()  # Список всех бойцов
    i = 0  # подсчет количества персонажей
    for Key_dict in Dict_person:
        k = 0
        while k < Dict_person[Key_dict]:
            his_name = random.choice(warriors_names)
            warriors = Key_dict(his_name, *List_base)
            warriors_names.remove(his_name)  # удаляем использоавнные имена
            if warriors not in All_warriors:
                k += 1
                i += 1
                print(f'Создан боец: № {i}: {warriors.name}.')
                warriors.set_things(things)
                All_warriors.append(warriors)
                print(f'Здоровье: {warriors.health:.1f}, урон: '
                      f'{warriors.damage:.1f}, защита: {warriors.armor:.1f}')
                print()
    print("-------------------Все персонажи созданы----------------------")
    return All_warriors

def Control_fight(HP: float, 
                  F1: Person, F2: Person):
    Attack_point = F1.attack_damage(F2) * F2.kritikal()
    HP = HP- Attack_point
    if HP < 0:
        HP = 0
    print(f'{F2.name} наносит удар по '
          f'{F1.name} на {Attack_point:.1f}'
          f' урона, здоровье {F1.name}: {HP:.1f}')
    return  HP


def Fight(fighter1, fighter2):
    HitPoints: float = 100  # переменная для контроля здоровья в ходе битвы
    HitPoints1 = fighter1.health
    HitPoints2 = fighter2.health

    print(f'--------Новый бой: {fighter1.name} здоровье {HitPoints1} vs '
          f'{fighter2.name} здоровье {HitPoints2}-------------')

    while HitPoints > 0:
        HitPoints1 = Control_fight(HitPoints1, fighter1, fighter2)
        if HitPoints1 == 0:
            break
        HitPoints2 = Control_fight(HitPoints2, fighter2, fighter1)
        if HitPoints2 == 0:
            break
        HitPoints = min(HitPoints1, HitPoints2)

    if HitPoints1 > HitPoints2:
        lost = fighter2
        win = fighter1
    else:
        lost = fighter1
        win = fighter2

    print(f'------------------Итог: {fighter1.name}: '
          f'здоровье {HitPoints1:.1f}, '
          f'{fighter2.name}: здоровье {HitPoints2:.1f}')
    print(f'----------победил {win.name}-------------')
    print()
    return lost


"""Запуск основного кода."""

things = create_things(Things_list)  # создаю вещи
All_warriors = create_warriors(warriors_names, things)
print()
print('В битве учавствуют:')
for i in range(len(All_warriors)):
    print(f'{i+1} - {All_warriors[i].name}')
print()

while len(All_warriors) > 1:
    User1 = input(f"Выберите бойца №1 (введите цифру от 1 до {len(All_warriors)}): ")
    User2 = input(f"Выберите бойца №2 (введите цифру от 1 до {len(All_warriors)}): ")
    Start_stop = input(f'Начать бой? (y/n)')
    if Start_stop == "n": break

    fighter1 = All_warriors[int(User1) - 1]  # выбрали бойца номер 1
    fighter2 = All_warriors[int(User2) - 1]   # выбрали бойца номер 2
    if fighter1 != fighter2:
        lost = Fight(fighter1, fighter2)
        All_warriors.remove(lost)
        print(f'Пока еще жив:')
        for i in range(len(All_warriors)):
            print(f'{i+1} - {All_warriors[i].name}')
        print()


print(f'Победитель: {All_warriors[0].name}')
