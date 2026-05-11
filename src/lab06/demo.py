import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Weapon
from lab03.models import Sword, Bow
from lab06.container import TypedCollection, Displayable, Scorable


def patch_classes():
    def display(self) -> str:
        return f"{self.name} (урон: {self.damage})"
    
    def score(self) -> float:
        return float(self.damage)
    
    for cls in [Weapon, Sword, Bow]:
        if not hasattr(cls, 'display'):
            cls.display = display
        if not hasattr(cls, 'score'):
            cls.score = score


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №6 - GENERICS И TYPING")
    print("=" * 60)
    
    patch_classes()
    
    # СЦЕНАРИЙ 1: БАЗОВАЯ РАБОТА
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: БАЗОВАЯ РАБОТА С GENERIC-КОЛЛЕКЦИЕЙ")
    print("=" * 60)
    
    weapons: TypedCollection[Weapon] = TypedCollection()
    
    sword = Sword("Экскалибур", "legendary", 90)
    bow = Bow("Лунный лук", "epic", 80)
    
    weapons.add(sword)
    weapons.add(bow)
    
    print("\n1.1 Коллекция после добавления:")
    print(f"   Количество: {len(weapons)}")
    
    print("\n1.2 Все элементы:")
    for item in weapons.get_all():
        print(f"   {item}")
    
    # СЦЕНАРИЙ 2: FIND, FILTER, MAP
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: МЕТОДЫ FIND, FILTER, MAP")
    print("=" * 60)
    
    col: TypedCollection[Weapon] = TypedCollection()
    col.add(Sword("Меч А", "common", 80))
    col.add(Sword("Меч Б", "legendary", 85))
    col.add(Bow("Лук", "epic", 70))
    
    print("\n2.1 find() - поиск legendary:")
    result = col.find(lambda x: x.rarity == "legendary")
    print(f"   Найдено: {result}")
    
    print("\n2.2 find() - поиск того чего нет:")
    result = col.find(lambda x: x.level == 10)
    print(f"   Результат: {result}")
    
    print("\n2.3 filter() - только legendary:")
    filtered = col.filter(lambda x: x.rarity == "legendary")
    for item in filtered:
        print(f"   {item}")
    
    print("\n2.4 map() - преобразование в имена (List[str]):")
    names = col.map(lambda x: x.name)
    print(f"   {names}")
    
    print("\n2.5 map() - преобразование в урон (List[int]):")
    damages = col.map(lambda x: x.damage)
    print(f"   {damages}")
    
    # СЦЕНАРИЙ 3: PROTOCOLS
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: PROTOCOLS И STRUCTURAL TYPING")
    print("=" * 60)
    
    displayable_col: TypedCollection[D] = TypedCollection()
    displayable_col.add(sword)
    displayable_col.add(bow)
    
    print("\n3.1 TypedCollection с ограничением Displayable:")
    print(f"   Количество: {len(displayable_col)}")
    print("   Вызов display() для каждого объекта:")
    for item in displayable_col:
        print(f"      {item.display()}")
    
    scorable_col: TypedCollection[S] = TypedCollection()
    scorable_col.add(sword)
    scorable_col.add(bow)
    
    print("\n3.2 TypedCollection с ограничением Scorable:")
    print(f"   Количество: {len(scorable_col)}")
    print("   Вызов score() для каждого объекта:")
    for item in scorable_col:
        print(f"      {item.name}: {item.score()}")
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()