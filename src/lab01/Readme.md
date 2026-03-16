# Отчет по лабораторной работе №1
## Тема: Класс и инкапсуляция (Python 3.x)
## Вариант 6: Игровая логика (класс Weapon)

---

## 📋 Как создать свой объект

```python
# Создание объекта оружия
sword = Weapon("Экскалибур", "sword", "legendary")
bow = Weapon("Лунный лук", "bow", "epic") 
staff = Weapon("Посох магии", "staff", "rare")
dagger = Weapon("Кинжал тени", "dagger", "common")

# После создания можно использовать методы:
sword.upgrade()           # улучшить оружие
damage = sword.attack()   # атаковать
sword.repair()            # починить
print(sword)              # вывести информацию

 # Вопрос №1. Что является сущностью
Ответ: Сущностью является игровое оружие (Weapon).
В контексте игровой логики оружие представляет собой предмет, которым персонаж может атаковать врагов. Оно обладает характеристиками: урон, прочность, редкость, уровень.
Примеры сущностей:

Меч-кладенец (легендарное оружие)
Лук охотника (обычное оружие)
Посох мага (эпическое оружие)
Кинжал ассасина (редкое оружие)
# Код, демонстрирующий сущность
def demonstrate_entity():
    """Демонстрация создания разных сущностей"""
    
    # Создаем разные виды оружия
    sword = Weapon("Меч-кладенец", "sword", "legendary")
    bow = Weapon("Лук охотника", "bow", "common")
    staff = Weapon("Посох мага", "staff", "epic")
    dagger = Weapon("Кинжал ассасина", "dagger", "rare")
    
    # Каждая сущность имеет свои уникальные характеристики
    weapons = [sword, bow, staff, dagger]
    
    print("Созданные сущности (оружие):")
    for weapon in weapons:
        print(f"  {weapon.description}")
    
    return weapons

# Вызов функции
weapons = demonstrate_entity()


# Вопрос №2. Какие атрибуты будут у данного объекта
Ответ: 6 закрытых атрибутов: название, тип, редкость, уровень, прочность, урон
# Доступ через свойства
print(sword.name)        # чтение
print(sword.level)       # чтение
sword.level = 3          # запись (с проверкой)
print(sword.damage)      # вычисляемое свойство

# Вопрос №3. Какие инварианты
Ответ: Инварианты - постоянные условия, которые всегда соблюдаются:
Уровень: 1 ≤ level ≤ 10
Прочность: 0 ≤ durability ≤ 100
Тип: только sword, bow, staff, dagger
Редкость: только common, rare, epic, legendary
Урон: всегда > 0
Имя: не пустое, минимум 2 символа
# Проверка инвариантов
try:
    sword.level = 11        # Ошибка! (>10)
    sword.durability = -50  # Ошибка! (<0)
    bad = Weapon("", "sword", "common")  # Ошибка! (пустое имя)
except ValueError as e:
    print(f"Инвариант соблюден: {e}")

# Вопрос №4. Что значит равенство
Ответ: Два объекта равны, если совпадают:
# Реализация __eq__
def __eq__(self, other):
    if not isinstance(other, Weapon):
        return False
    return (self._name == other._name and 
            self._weapon_type == other._weapon_type and 
            self._rarity == other._rarity and
            self._level == other._level)

# Примеры
w1 = Weapon("Меч", "sword", "legendary")
w2 = Weapon("Меч", "sword", "legendary")
w3 = Weapon("Меч", "sword", "legendary")
w3.level = 3

print(w1 == w2)  # True (одинаковые)
print(w1 == w3)  # False (разный уровень)

# Вопрос №5. Есть ли состояния
Ответ: Да, есть логическое состояние "сломано / исправно".
@property
def is_broken(self):
    return self._durability <= 0
    