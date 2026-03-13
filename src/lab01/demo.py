# demo.py - ПОЛНАЯ ДЕМОНСТРАЦИЯ КЛАССА Weapon

from model import Weapon

def main():
    """Главная функция демонстрации"""
    
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №1 - КЛАСС WEAPON")
    print("=" * 60)
    
    # ----- 1. СОЗДАНИЕ ОБЪЕКТОВ -----
    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ:")
    print("-" * 40)
    
    try:
        sword = Weapon("Экскалибур", "sword", "legendary")
        bow = Weapon("Лунный лук", "bow", "epic")
        staff = Weapon("Посох магии", "staff", "rare")
        dagger = Weapon("Кинжал тени", "dagger", "common")
        
        print("✓ Создано 4 объекта:")
        print(f"  {sword}")
        print(f"  {bow}")
        print(f"  {staff}")
        print(f"  {dagger}")
    except Exception as e:
        print(f"✗ Ошибка: {e}")
        return
    
    # ----- 2. ДЕМОНСТРАЦИЯ ГЕТТЕРОВ -----
    print("\n2. ДЕМОНСТРАЦИЯ ГЕТТЕРОВ (чтение данных):")
    print("-" * 40)
    
    print(f"  name: {sword.name}")
    print(f"  weapon_type: {sword.weapon_type}")
    print(f"  rarity: {sword.rarity}")
    print(f"  level: {sword.level}")
    print(f"  damage: {sword.damage}")
    print(f"  durability: {sword.durability}")
    print(f"  is_broken: {sword.is_broken}")
    print(f"  description: {sword.description}")
    
    # ----- 3. ДЕМОНСТРАЦИЯ СЕТТЕРОВ -----
    print("\n3. ДЕМОНСТРАЦИЯ СЕТТЕРОВ (изменение данных):")
    print("-" * 40)
    
    print(f"  Текущий уровень: {sword.level}")
    sword.level = 3
    print(f"  После повышения: уровень = {sword.level}")
    print(f"  Урон изменился: {sword.damage}")
    
    print(f"\n  Текущая прочность: {sword.durability}")
    sword.durability = 50
    print(f"  После установки: прочность = {sword.durability}")
    
    # ----- 4. ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ -----
    print("\n4. ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ (обработка ошибок):")
    print("-" * 40)
    
    # Ошибки при создании
    print("\n  4.1 Ошибки при создании:")
    try:
        bad = Weapon("", "sword", "common")
    except ValueError as e:
        print(f"    ✓ Пустое имя: {e}")
    
    try:
        bad = Weapon("Меч", "gun", "common")
    except ValueError as e:
        print(f"    ✓ Неверный тип: {e}")
    
    # Ошибки при изменении
    print("\n  4.2 Ошибки при изменении:")
    try:
        sword.level = 11
    except ValueError as e:
        print(f"    ✓ Уровень 11: {e}")
    
    try:
        sword.level = 1
    except ValueError as e:
        print(f"    ✓ Понижение уровня: {e}")
    
    try:
        sword.durability = -50
    except ValueError as e:
        print(f"    ✓ Отрицательная прочность: {e}")
    
    # ----- 5. ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ -----
    print("\n5. ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ:")
    print("-" * 40)
    
    print(f"  __str__: {sword}")
    print(f"  __repr__: {repr(sword)}")
    
    sword2 = Weapon("Экскалибур", "sword", "legendary")
    sword2.level = 3
    print(f"  sword == sword2: {sword == sword2}")
    
    # ----- 6. ДЕМОНСТРАЦИЯ АТРИБУТОВ КЛАССА -----
    print("\n6. ДЕМОНСТРАЦИЯ АТРИБУТОВ КЛАССА:")
    print("-" * 40)
    
    print(f"  Через класс:")
    print(f"    Weapon.WEAPON_TYPES: {Weapon.WEAPON_TYPES}")
    print(f"    Weapon.RARITY_MULTIPLIERS: {Weapon.RARITY_MULTIPLIERS}")
    print(f"    Weapon.MAX_LEVEL: {Weapon.MAX_LEVEL}")
    
    print(f"\n  Через экземпляр:")
    print(f"    sword.WEAPON_TYPES['sword']: {sword.WEAPON_TYPES['sword']}")
    print(f"    sword.RARITY_MULTIPLIERS['legendary']: {sword.RARITY_MULTIPLIERS['legendary']}")
    
    # ----- 7. ДЕМОНСТРАЦИЯ БИЗНЕС-МЕТОДОВ -----
    print("\n7. ДЕМОНСТРАЦИЯ БИЗНЕС-МЕТОДОВ:")
    print("-" * 40)
    
    test = Weapon("Тестовое", "sword", "epic")
    print(f"  Начальное состояние: {test}")
    
    # upgrade
    print("\n  7.1 upgrade():")
    test.upgrade()
    print(f"    После upgrade: уровень {test.level}, урон {test.damage}")
    
    # attack
    print("\n  7.2 attack():")
    for i in range(3):
        damage = test.attack()
        print(f"    Атака {i+1}: урон {damage}, прочность {test.durability}%")
    
    # repair
    print("\n  7.3 repair():")
    test.repair()
    print(f"    После ремонта: прочность {test.durability}%")
    
    # ----- 8. ДЕМОНСТРАЦИЯ ЛОГИЧЕСКОГО СОСТОЯНИЯ -----
    print("\n8. ДЕМОНСТРАЦИЯ ЛОГИЧЕСКОГО СОСТОЯНИЯ:")
    print("-" * 40)
    
    fragile = Weapon("Хрупкое", "dagger", "common")
    print(f"  Создано: {fragile}")
    
    # Доводим до поломки
    print("\n  8.1 Используем до поломки:")
    while not fragile.is_broken:
        fragile.attack()
        print(f"    Прочность: {fragile.durability}%")
    
    # Пытаемся использовать сломанное
    print("\n  8.2 Попытка использовать сломанное:")
    try:
        fragile.attack()
    except ValueError as e:
        print(f"    ✓ Ошибка: {e}")
    
    # Ремонтируем
    print("\n  8.3 Ремонт:")
    fragile.repair()
    print(f"    После ремонта: прочность {fragile.durability}%")
    
    # ----- 9. ДЕМОНСТРАЦИЯ СТАТУСА -----
    print("\n9. ДЕМОНСТРАЦИЯ ПОЛНОГО СТАТУСА:")
    print("-" * 40)
    
    epic_sword = Weapon("Легендарный меч", "sword", "legendary")
    epic_sword.level = 5
    epic_sword.durability = 75
    print(epic_sword.get_status())
    
    # ----- 10. ИТОГ -----
    print("\n" + "=" * 60)
    print("✅ ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 60)

if __name__ == "__main__":
    main()