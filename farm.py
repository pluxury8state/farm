class animals():
    feed_indicator = 'хочет есть'
    voice = ''
    name = 0
    weight = 0

    def feed(self):
        self.feed_indicator = 'не хочет есть'

    def __init__(self, Name, weight):
        self.name = Name
        self.weight = weight

    def all_weight(self, val):
        val += self.weight
        return val

    def return_weight(self):
        return self.weight


class Goose(animals):
    egg_counter = 'яйца не собраны'
    voice = 'GA GA'

    def collect_egg(self):
        self.egg_counter = 'яйца собраны'


class Cow(animals):
    voice = 'Mow mow'
    milk_counter = 'не подоен'

    def collect_milk(self):
        self.milk_counter = 'подоен'


class Sheep(animals):
    voice = 'Beea'

    wool = 'не подстрижен'

    def heircut(self):
        self.wool = 'подстрижен'


class Chicken(Goose):
    voice = 'Ko ko ko'


class Goat(Cow):
    voice = 'Meea'


class Duck(Goose):
    voice = 'Krya'


# Инициализация классов


Gray = Goose("Серый", 8)
White = Goose("Белый", 7.5)

Mankya = Cow("Манька", 400)

Lamb = Sheep("Барашек", 27)

Curly = Sheep("Кудрявый", 84)

Ko_ko = Chicken("Ко-ко", 2)

Cock_a_doodle_doo = Chicken("Кукареку", 1)

Horns = Goat("Рога", 53)
Hoofs = Goat("Копыта", 67)

Kryakva = Duck("Кряква", 3)

# для облегчения отображений заключаю объекты в список
animal = [Gray, White, Mankya, Lamb, Curly, Ko_ko, Cock_a_doodle_doo, Horns, Hoofs, Kryakva]

# работа с объектами


print('состояние животных до использования метотдов')
for Name in animal:
    print(f'{Name.name}, с весом {Name.weight} кг - {Name.feed_indicator}')

print('\nнакормим всех животных:\n')
for Name in animal:
    Name.feed()
    print(f'{Name.name}, с весом {Name.weight} кг - {Name.feed_indicator}')

print('\nСписок животных,которых не подоили:\n')
for Name in animal:
    if isinstance(Name, Cow):
        print(f'{Name.name}, {Name.milk_counter}')

print('\nтеперь подоили\n')

for Name in animal:
    if isinstance(Name, Cow):
        Name.collect_milk()
        print(f'{Name.name}, {Name.milk_counter}')

print('\nСписок животных,которых не подстригли:\n')
for Name in animal:
    if isinstance(Name, Sheep):
        print(f'{Name.name}, {Name.wool}')

print('\nтеперь подстригли\n')

for Name in animal:
    if isinstance(Name, Sheep):
        Name.heircut()
        print(f'{Name.name}, {Name.wool}')

print('\nСписок животных,у которых не собрали яйца:\n')
for Name in animal:
    if isinstance(Name, Goose):
        print(f'у {Name.name} - {Name.egg_counter}')

print('\nтеперь яйца собраны\n')
for Name in animal:
    if isinstance(Name, Goose):
        Name.collect_egg()
        print(f'у {Name.name} - {Name.egg_counter}')

print('\nподсчитаем общий вес животных \n')

weight = 0
for Name in animal:
    weight = Name.all_weight(weight)

print(f'общий вес животных = {weight}')

weight = 0

animal_bigger_name = ' '

for Name in animal:
    if weight <= Name.weight:
        weight = Name.weight
        animal_bigger_name = Name.name

print(f'\nимя животного с самым большим весом -{animal_bigger_name} и его вес составляет : {weight} \n')



