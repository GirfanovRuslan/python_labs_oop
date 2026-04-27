# src/lab05/demo.py

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab05.collection import WeaponCollection
from lab05.strategies import *
from lab01.model import Weapon


def create_sample_collection():
    collection = WeaponCollection()
    collection.add(Weapon("Экскалибур", "sword", "legendary"))
    collection.add(Weapon("Лунный лук", "bow", "epic"))
    collection.add(Weapon("Посох магии", "staff", "rare"))
    collection.add(Weapon("Кинжал тени", "dagger", "common"))
    collection.add(Weapon("Древний меч", "sword", "rare"))
    for item in collection.get_all():
        item.level = 3
    return collection


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №5 - СТРАТЕГИИ И ДЕЛЕГАТЫ")
    print("=" * 60)

    # СЦЕНАРИЙ 1: СОРТИРОВКА ТРЁМЯ СТРАТЕГИЯМИ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: СОРТИРОВКА КОЛЛЕКЦИИ ТРЁМЯ СТРАТЕГИЯМИ")
    print("=" * 60)

    col = create_sample_collection()
    print("\n1.1 Исходная коллекция:")
    print(col)

    print("\n1.2 Сортировка по имени:")
    col2 = col.copy()
    col2.sort_by(by_name)
    print(col2)

    print("\n1.3 Сортировка по уровню:")
    col3 = col.copy()
    col3.sort_by(by_level)
    print(col3)

    print("\n1.4 Сортировка по редкости:")
    col4 = col.copy()
    col4.sort_by(by_rarity)
    print(col4)

    # СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ ДВУМЯ ФУНКЦИЯМИ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ")
    print("=" * 60)

    col5 = create_sample_collection()

    print("\n2.1 Фильтрация: только легендарное оружие:")
    filtered = list(filter(is_legendary, col5.get_all()))
    for item in filtered:
        print(f"   {item}")

    print("\n2.2 Фильтрация: только исправное оружие:")
    filtered2 = list(filter(is_not_broken, col5.get_all()))
    for item in filtered2:
        print(f"   {item}")

    # СЦЕНАРИЙ 3: MAP, ЦЕПОЧКА, CALLABLE
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: MAP, ЦЕПОЧКА ОПЕРАЦИЙ И CALLABLE-ОБЪЕКТ")
    print("=" * 60)

    col6 = create_sample_collection()

    print("\n3.1 Применение map() с lambda:")
    upgraded = list(map(lambda x: x.level + 1, col6.get_all()))
    print(f"   Новые уровни: {upgraded}")

    print("\n3.2 Фабрика функций make_level_filter(4):")
    high_filter = make_level_filter(4)
    filtered_high = list(filter(high_filter, col6.get_all()))
    print(f"   Объекты с уровнем >= 4: {len(filtered_high)} шт.")

    print("\n3.3 Цепочка операций filter -> sort -> apply:")
    col7 = create_sample_collection()
    result = (col7
              .copy()
              .filter_by(is_legendary)
              .sort_by(by_name)
              .apply(lambda x: x.upgrade()))
    print(f"   Результат: {result}")

    print("\n3.4 Callable-объект DamageBonusStrategy(5):")
    col8 = create_sample_collection()
    bonus = DamageBonusStrategy(5)
    print(f"   Урон до: {col8.get_all()[0].damage}")
    col8.apply(bonus)
    print(f"   Урон после: {col8.get_all()[0].damage}")

    print("\n3.5 Сортировка через lambda:")
    col9 = create_sample_collection()
    col9.sort_by(lambda x: x.name.lower(), reverse=True)
    print(col9)

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()