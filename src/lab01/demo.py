# src/lab01/demo.py

from model import Weapon


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №1 - КЛАСС WEAPON")
    print("=" * 60)
    
    # =========================================================================
    # СЦЕНАРИЙ 1: НОРМАЛЬНАЯ РАБОТА
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: НОРМАЛЬНАЯ РАБОТА С ОРУЖИЕМ")
    print("=" * 60)
    
    print("\n1.1 Создание легендарного меча")
    sword = Weapon("Экскалибур", "sword", "legendary")
    print(f"   Создан: {sword}")
    print(f"   Характеристики: уровень {sword.level}, урон {sword.damage}, прочность {sword.durability}%")
    
    print("\n1.2 Улучшение оружия")
    sword.upgrade()
    print(f"   После улучшения: уровень {sword.level}, урон {sword.damage}")
    
    sword.upgrade()
    print(f"   После второго улучшения: уровень {sword.level}, урон {sword.damage}")
    
    print("\n1.3 Атака оружием")
    for i in range(3):
        damage = sword.attack()
        print(f"   Атака {i+1}: урон {damage}, прочность {sword.durability}%")
    
    print("\n1.4 Ремонт оружия")
    sword.repair()
    print(f"   После ремонта: прочность {sword.durability}%")
    
    print("\n1.5 Полный статус")
    print(f"   {sword.get_status()}")
    
    # =========================================================================
    # СЦЕНАРИЙ 2: ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ (ОБРАБОТКА ОШИБОК)
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ (ОБРАБОТКА ОШИБОК)")
    print("=" * 60)
    
    print("\n2.1 Ошибки при создании объекта:")
    
    print("   Попытка создать оружие с пустым именем:")
    try:
        bad = Weapon("", "sword", "common")
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("   Попытка создать оружие с неверным типом:")
    try:
        bad = Weapon("Меч", "gun", "common")
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("   Попытка создать оружие с неверной редкостью:")
    try:
        bad = Weapon("Меч", "sword", "mythic")
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("\n2.2 Ошибки при изменении уровня:")
    test_sword = Weapon("Тестовый меч", "sword", "common")
    print(f"   Текущий уровень: {test_sword.level}")
    
    print("   Попытка установить уровень 11:")
    try:
        test_sword.level = 11
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("   Попытка установить уровень 0:")
    try:
        test_sword.level = 0
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    test_sword.level = 5
    print(f"   Уровень повышен до {test_sword.level}")
    
    print("   Попытка понизить уровень:")
    try:
        test_sword.level = 3
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("\n2.3 Ошибки при изменении прочности:")
    print("   Попытка установить отрицательную прочность:")
    try:
        test_sword.durability = -50
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("   Попытка установить прочность выше 100:")
    try:
        test_sword.durability = 150
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    # =========================================================================
    # СЦЕНАРИЙ 3: ДЕМОНСТРАЦИЯ ЛОГИЧЕСКИХ СОСТОЯНИЙ И ИЗМЕНЕНИЯ СОСТОЯНИЯ
    # =========================================================================
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: ЛОГИЧЕСКИЕ СОСТОЯНИЯ И ИЗМЕНЕНИЕ СОСТОЯНИЯ")
    print("=" * 60)
    
    print("\n3.1 Создание обычного меча")
    fragile = Weapon("Хрупкий меч", "sword", "common")
    print(f"   Создан: {fragile}")
    print(f"   Состояние: is_broken = {fragile.is_broken}")
    
    print("\n3.2 Использование оружия до поломки (изменение состояния)")
    attack_count = 0
    while not fragile.is_broken:
        damage = fragile.attack()
        attack_count += 1
        print(f"   Атака {attack_count}: урон {damage}, прочность {fragile.durability}%, is_broken = {fragile.is_broken}")
    
    print(f"\n   Оружие сломалось после {attack_count} атак")
    print(f"   Состояние: is_broken = {fragile.is_broken}")
    
    print("\n3.3 Попытка использовать сломанное оружие")
    print("   Попытка атаковать:")
    try:
        fragile.attack()
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("   Попытка улучшить:")
    try:
        fragile.upgrade()
    except ValueError as e:
        print(f"     Ошибка: {e}")
    
    print("\n3.4 Ремонт оружия (изменение состояния)")
    fragile.repair()
    print(f"   После ремонта: прочность {fragile.durability}%, is_broken = {fragile.is_broken}")
    
    print("\n3.5 Снова атакуем после ремонта")
    damage = fragile.attack()
    print(f"   Атака: урон {damage}, прочность {fragile.durability}%, is_broken = {fragile.is_broken}")
    
    print("\n3.6 Демонстрация разных состояний у разных объектов")
    legendary = Weapon("Легендарный меч", "sword", "legendary")
    epic = Weapon("Эпический лук", "bow", "epic")
    broken = Weapon("Сломанный кинжал", "dagger", "common")
    broken.durability = 0
    
    print(f"   {legendary.get_status()}")
    print(f"   {epic.get_status()}")
    print(f"   {broken.get_status()}")
    
    # =========================================================================
    # ИТОГ
    # =========================================================================
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()