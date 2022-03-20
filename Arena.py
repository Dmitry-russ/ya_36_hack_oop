"""
Игра Арена!
*Класс с вещами - название, процент защиты, атаки и жизни
*Создать класс с бойцами (базовый) - Имя, кол-во л.с./жизни, базовую атаку, базовый процент защиты
    *метод, принимающий на вход список вещей set_things(things)
    *метод вычитания жизни на основе  входной атаки, а также методы для выполнения алгоритма, представленного ниже;
*Создать класс с вещами

"""
import random


"""Словарь с вещами: процент к здоровью, процент к урону, процент к защите."""
Things_list = [
            ("Броня когтя дракона", [0.1, 0.02, 0.05]),
            ("Каркас" , [0.1, 0.03, 0.03]), 
            ("Кольчуга" , [0.1, 0.04, 0.025]), 
            ("Броня вавилона" , [0.1, 0.01, 0.1]), 
            ("Сандали Ахилеса" , [0.4, 0.015, 0.07]),
            ("Плащ Немезиды" , [0.2, 0.033, 0.06]),
]

"""Имена бойцов."""
warriors_names = ("Ахилес", "Архимед", 
            "Бульдог", "Рыцарь", 
            "Ворон", "Астерикс", 
            "Обеликс", "Панармикс", 
            "Кватериск", "Гватемалорикс"
            "Илья Муромец", "Соловей Разбойник",
            "Никита Добрынич", "Змей Горыныч",
            "Баба Яга", "Кощей бессмертный",
            "Шут", "Князь Гвидон",
            "Скороход", "Голландец"
            )

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
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def set_things(self, things):
        random_index = random.randint(0, len(things) - 1)
        print (f'{self.name} получает: {things[random_index].name}.')
        self.health = (self.health*things[random_index].health_percent + self.health)
        self.damage = (self.damage*things[random_index].damage_percent + self.damage)
        self.armor = (self.armor*things[random_index].armor_percent + self.armor)




        
class Paladin(Person):
    """Палладин с увеличенным здоровьем и защитой."""

    def __init__(self,
                 name: str,
                 health: float,
                 damage: float,
                 armor: float,
                 ) -> None:
        super().__init__(name, damage)
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
        super().__init__(name, health, armor)
        self.damage = damage*2

"""Создание спсика вещей things."""
def create_things(Things_list: list):
    print ("Создаем вещи:")
    things = list ()
    for i in Things_list:
        one_thing = Thing(i[0], *i[1])
        print(f'Создан объект: {one_thing.name}:')
        things.append(one_thing)
        print(f'здоровье: +{one_thing.health_percent*100:.1f}%, урон: ' 
              f'+{one_thing.damage_percent*100:.1f}%, защита: +{one_thing.armor_percent*100:.1f}%') 
    return things

def create_warriors (warriors_names, things)-> Person:
    random_index = random.randint(0, len(warriors_names) - 1)
    warriors = Person(warriors_names[random_index], 100, 100, 100)
    print (f'Создан персонаж: {warriors.name}.')
    warriors.set_things(things)
    print (f'Здоровье: {warriors.health:.1f}, урон: ' 
              f'{warriors.damage:.1f}, защита: {warriors.armor:.1f}')



things=create_things(Things_list)
for i in range(11):
    create_warriors(warriors_names, things)


