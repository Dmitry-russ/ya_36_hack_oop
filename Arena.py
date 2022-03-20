import random

"""Словарь с вещами: процент к здоровью, процент к урону, процент к защите."""
Things_list = [
            ("Броня когтя дракона", [0.1, 0.02, 0.05]),
            ("Каркас", [0.1, 0.03, 0.03]),
            ("Кольчуга", [0.1, 0.04, 0.025]),
            ("Броня вавилона", [0.1, 0.01, 0.1]),
            ("Сандали Ахилеса", [0.4, 0.015, 0.07]),
            ("Плащ Немезиды", [0.2, 0.033, 0.06]),
]

"""Имена бойцов."""
warriors_names = ("Ахилес", "Архимед",
                  "Бульдог", "Рыцарь",
                  "Ворон", "Астерикс",
                  "Обеликс", "Панармикс",
                  "Кватериск", "Гватемалорикс",
                  "Илья Муромец", "Соловей Разбойник",
                  "Никита Добрынич", "Змей Горыныч",
                  "Баба Яга", "Кощей бессмертный",
                  "Шут", "Князь Гвидон",
                  "Скороход", "Голландец"
                  )

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


"""Cловарь распределения персонажей."""
Dict_person = {Person: 7, Paladin: 2, Warrior: 1}


"""Создание спсика вещей things."""


def create_things(Things_list: list):
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
    All_warriors = list()  # Список всех бойцов
    i = 0  # подсчет количества персонажей
    Sum_warriors = sum(Dict_person.values())

    while len(All_warriors) < Sum_warriors:

        if len(All_warriors) < Dict_person[Person]:
            warriors = Person(random.choice(warriors_names), *List_base)
        elif len(All_warriors) >= Dict_person[Person] and len(All_warriors) < (Dict_person[Person] + Dict_person[Paladin]):
            warriors = Paladin(random.choice(warriors_names), *List_base)
        else:
            warriors = Warrior(random.choice(warriors_names), *List_base)

        if warriors not in All_warriors:
            i += 1
            print(f'Создан персонаж №{i} : {warriors.name}.')
            warriors.set_things(things)
            All_warriors.append(warriors)
            print(f'Здоровье: {warriors.health:.1f}, урон: '
                  f'{warriors.damage:.1f}, защита: {warriors.armor:.1f}')
            print()
    print("-------------------Все персонажи созданы----------------------")
    return All_warriors


def Fight(fighter1, fighter2):
    HitPoints: float = 100  # переменная для контроля здоровья в ходе битвы
    HitPoints1 = fighter1.health
    HitPoints2 = fighter2.health

    print(f'--------новый бой: {fighter1.name} здоровье {HitPoints1} vs '
          f'{fighter2.name} здоровье {HitPoints2}-------------')
    while HitPoints > 0:

        Attack_point = fighter1.attack_damage(fighter2)
        HitPoints1 = HitPoints1-Attack_point
        if HitPoints1 < 0:
            HitPoints1 = 0
        print(f'{fighter2.name} наносит удар по '
              f'{fighter1.name} на {Attack_point:.1f}'
              f' урона, здоровье {fighter1.name}: {HitPoints1:.1f}')
        if HitPoints1 == 0:
            break

        if HitPoints2 > 0:
            Attack_point = fighter2.attack_damage(fighter1)
            HitPoints2 = HitPoints2-Attack_point
            if HitPoints2 < 0:
                HitPoints2 = 0
            print(f'{fighter1.name} наносит удар по '
                  f'{fighter2.name} на {Attack_point:.1f}'
                  f' урона, здоровье {fighter2.name}: {HitPoints2:.1f}')
        else:
            break
        HitPoints = min(HitPoints1, HitPoints2)

    if HitPoints1 > HitPoints2:
        lost = fighter2
        win = fighter1
    else:
        lost = fighter1
        win = fighter2
    print(f'------------------Итог: {fighter1.name}:'
          f'здоровье {HitPoints1:.1f}, '
          f'{fighter2.name}: здоровье {HitPoints2:.1f}-----победил {win.name}')
    print()
    return lost


"""Запуск основного кода."""

things = create_things(Things_list)  # создаю вещи
All_warriors = create_warriors(warriors_names, things)
print()
print('В битве учавствуют:')
for i in range(len(All_warriors)):
    print(f'{All_warriors[i].name}')
print()


while len(All_warriors) > 1:
        fighter1 = random.choice(All_warriors)  # выбрали бойца номер 1
        fighter2 = random.choice(All_warriors)  # выбрали бойца номер 2
        if fighter1 != fighter2:
            lost = Fight(fighter1, fighter2)
            All_warriors.remove(lost)
            for i in range(len(All_warriors)):
                print(f'Пока еще жив: {All_warriors[i].name}')
            print()


print(f'Победитель: {All_warriors[0].name}')
