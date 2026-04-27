

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab04.models import Sword, Bow, Staff
from lab04.collection import WeaponCollection
from lab04.interfaces import Displayable


def print_all_displayable(items):
    """Универсальная функция, работающая через интерфейс Displayable"""
    for item in items:
        if isinstance(item, Displayable):
            print(f"   {item.display_info()}")


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №4 - ИНТЕРФЕЙСЫ (ABC)")
    print("=" * 60)

    # СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И ВЫЗОВ ИНТЕРФЕЙСНЫХ МЕТОДОВ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: СОЗДАНИЕ ОБЪЕКТОВ И ИНТЕРФЕЙСНЫЕ МЕТОДЫ")
    print("=" * 60)

    sword = Sword("Экскалибур", "legendary", blade_length=90)
    bow = Bow("Лунный лук", "epic", range_meters=80)
    staff = Staff("Посох магии", "rare")

    print("\n1.1 Displayable метод display_info():")
    print(f"   {sword.display_info()}")
    print(f"   {bow.display_info()}")
    print(f"   {staff.display_info()}")

    print("\n1.2 Upgradable метод upgrade():")
    sword.upgrade()
    bow.upgrade()

    # СЦЕНАРИЙ 2: ИНТЕРФЕЙС КАК ТИП И ПРОВЕРКА isinstance
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ИНТЕРФЕЙС КАК ТИП И ПРОВЕРКА isinstance")
    print("=" * 60)

    items = [sword, bow, staff]

    print("\n2.1 Проверка через isinstance():")
    for item in items:
        print(f"   {item.__class__.__name__}: Displayable? {isinstance(item, Displayable)}")

    print("\n2.2 Универсальная функция print_all_displayable():")
    print_all_displayable(items)

    # СЦЕНАРИЙ 3: КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСУ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: КОЛЛЕКЦИЯ И ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСУ")
    print("=" * 60)

    collection = WeaponCollection()
    collection.add(sword)
    collection.add(bow)
    collection.add(staff)

    print("\n3.1 Исходная коллекция:")
    print(collection)

    print("\n3.2 Фильтрация: только Displayable объекты:")
    for item in collection.get_displayable():
        print(f"   {item.display_info()}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()