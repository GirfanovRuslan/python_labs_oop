
from model import Weapon
from collection import WeaponCollection


def main():
    print("=" * 60)
    print("ЛАБОРАТОРНАЯ РАБОТА №2 - КОЛЛЕКЦИЯ WEAPON")
    print("=" * 60)
    
    # СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ

    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ")
    print("=" * 60)
    
    collection = WeaponCollection()
    
    sword1 = Weapon("Экскалибур", "sword", "legendary")
    sword2 = Weapon("Меч кладенец", "sword", "epic")  # было "Меч-кладенец"
    bow = Weapon("Лунный лук", "bow", "rare")
    staff = Weapon("Посох магии", "staff", "common")
    
    print("\n1.1 Добавление оружия в коллекцию:")
    collection.add(sword1)
    print(f"   Добавлен: {sword1}")
    collection.add(sword2)
    print(f"   Добавлен: {sword2}")
    collection.add(bow)
    print(f"   Добавлен: {bow}")
    collection.add(staff)
    print(f"   Добавлен: {staff}")
    
    print(f"\n1.2 Размер коллекции: {len(collection)}")
    
    print("\n1.3 Все элементы коллекции:")
    print(collection)
    
    print("\n1.4 Удаление элемента:")
    collection.remove(bow)
    print(f"   Удалён: {bow}")
    print(f"   Размер после удаления: {len(collection)}")
    
    print("\n1.5 Коллекция после удаления:")
    print(collection)
    
    # СЦЕНАРИЙ 2: ПОИСК, ИТЕРАЦИЯ, ЗАЩИТА ОТ ДУБЛИКАТОВ
 
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 2: ПОИСК, ИТЕРАЦИЯ, ЗАЩИТА ОТ ДУБЛИКАТОВ")
    print("=" * 60)
    
    collection2 = WeaponCollection()
    collection2.add(Weapon("Экскалибур", "sword", "legendary"))
    collection2.add(Weapon("Лунный лук", "bow", "epic"))
    collection2.add(Weapon("Посох магии", "staff", "rare"))
    collection2.add(Weapon("Кинжал тени", "dagger", "common"))
    collection2.add(Weapon("Древний меч", "sword", "rare"))
    collection2.add(Weapon("Ветряной лук", "bow", "legendary"))
    
    print("\n2.1 Поиск по имени 'Экскалибур':")
    found = collection2.find_by_name("Экскалибур")
    for w in found:
        print(f"   {w}")
    
    print("\n2.2 Поиск по типу 'sword':")
    found = collection2.find_by_type("sword")
    for w in found:
        print(f"   {w}")
    
    print("\n2.3 Поиск по редкости 'legendary':")
    found = collection2.find_by_rarity("legendary")
    for w in found:
        print(f"   {w}")
    
    print("\n2.4 Итерация по коллекции (for ... in):")
    for i, weapon in enumerate(collection2):
        print(f"   {i+1}. {weapon}")
    
    print("\n2.5 Проверка защиты от дубликатов:")
    try:
        duplicate = Weapon("Экскалибур", "sword", "legendary")
        collection2.add(duplicate)
        print(f"   Ошибка: дубликат был добавлен")
    except ValueError as e:
        print(f"   Не удалось добавить дубликат: {e}")
    
    print(f"\n2.6 Длина коллекции: {len(collection2)}")
    
    # СЦЕНАРИЙ 3: ИНДЕКСАЦИЯ, СОРТИРОВКА, ФИЛЬТРАЦИЯ
    print("\n" + "=" * 60)
    print("СЦЕНАРИЙ 3: ИНДЕКСАЦИЯ, СОРТИРОВКА, ФИЛЬТРАЦИЯ")
    print("=" * 60)
    
    collection3 = WeaponCollection()
    collection3.add(Weapon("Меч А", "sword", "common"))
    collection3.add(Weapon("Меч Б", "sword", "rare"))
    collection3.add(Weapon("Лук А", "bow", "epic"))
    collection3.add(Weapon("Посох А", "staff", "legendary"))
    collection3.add(Weapon("Кинжал А", "dagger", "common"))
    
    print("\n3.1 Исходная коллекция:")
    print(collection3)
    
    print("\n3.2 Индексация:")
    print(f"   collection3[0] = {collection3[0]}")
    print(f"   collection3[2] = {collection3[2]}")
    print(f"   collection3[-1] = {collection3[-1]}")
    
    print("\n3.3 Удаление по индексу:")
    removed = collection3.remove_at(2)
    print(f"   Удалён: {removed}")
    print(collection3)
    
    print("\n3.4 Сортировка по имени:")
    collection3.sort_by_name()
    print(collection3)
    
    print("\n3.5 Сортировка по урону (по убыванию):")
    collection3.sort_by_damage(reverse=True)
    print(collection3)
    
    print("\n3.6 Сортировка по редкости:")
    collection3.sort_by_rarity()
    print(collection3)
    

    
    print("\n3.8 Фильтрация: только оружие с уровнем >= 3")
    high_level = collection3.filter_by_min_level(3)
    print(high_level)
    
    print("\n3.9 Фильтрация: только эпическое оружие")
    all_weapons = WeaponCollection()
    all_weapons.add(Weapon("Меч", "sword", "legendary"))
    all_weapons.add(Weapon("Лук", "bow", "epic"))
    all_weapons.add(Weapon("Посох", "staff", "rare"))
    all_weapons.add(Weapon("Кинжал", "dagger", "common"))
    
    for w in all_weapons.get_all():
        w.level = 5
    
    print("Исходная коллекция:")
    print(all_weapons)
    
    
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)


if __name__ == "__main__":
    main()