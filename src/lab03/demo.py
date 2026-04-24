import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base import Weapon
from models import Sword, Bow
from collection import WeaponCollection


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №3 - НАСЛЕДОВАНИЕ")
    print("=" * 60)

    # =========================================================================
    # СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И МЕТОДЫ
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И МЕТОДЫ")
    print("=" * 60)

    sword = Sword("Экскалибур", "legendary", blade_length=90, is_two_handed=False)
    bow = Bow("Лунный лук", "epic", range_meters=80, arrow_type="fire")

    print("\n1.1 Объекты:")
    print(f"   {sword}")
    print(f"   {bow}")

    print("\n1.2 Методы базового класса:")
    sword.upgrade()
    print(f"   После улучшения: уровень {sword.level}, урон {sword.damage}")

    print("\n1.3 Новые методы дочерних классов:")
    sword.sharpen()
    print(f"   После заточки: урон {sword.damage}")
    bow.upgrade_bow()
    print(f"   После улучшения: дальность {bow.range_meters} м")

    # =========================================================================
    # СЦЕНАРИЙ 2: ПОЛИМОРФИЗМ
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ПОЛИМОРФИЗМ")
    print("=" * 60)

    weapons = [sword, bow]

    print("\n2.1 Полиморфный метод get_special_bonus():")
    for w in weapons:
        print(f"   {w.get_special_bonus()}")

    print("\n2.2 Проверка типов через isinstance():")
    for w in weapons:
        if isinstance(w, Sword):
            print(f"   {w.name} - это меч")
        elif isinstance(w, Bow):
            print(f"   {w.name} - это лук")

    # =========================================================================
    # СЦЕНАРИЙ 3: КОЛЛЕКЦИЯ РАЗНЫХ ТИПОВ ОРУЖИЯ
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: КОЛЛЕКЦИЯ РАЗНЫХ ТИПОВ ОРУЖИЯ")
    print("=" * 60)

    collection = WeaponCollection()
    
    sword2 = Sword("Меч кладенец", "rare", blade_length=85, is_two_handed=True)
    bow2 = Bow("Ветряной лук", "rare", range_meters=60, arrow_type="metal")

    collection.add(sword)
    collection.add(bow)
    collection.add(sword2)
    collection.add(bow2)

    print("\n3.1 Все объекты в коллекции:")
    print(collection)

    print("\n3.2 Вызов полиморфного метода get_special_bonus() для всех объектов:")
    for item in collection:
        print(f"   {item.get_special_bonus()}")

    print("\n3.3 Фильтрация по типу (только мечи):")
    swords_only = collection.get_only_swords()
    print(swords_only)

    print("\n3.4 Фильтрация по типу (только луки):")
    bows_only = collection.get_only_bows()
    print(bows_only)

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()