# src/lab07/cli.py

from lab07.app import WeaponApp
from lab07.exceptions import DuplicateWeaponError, WeaponNotFoundError


def print_menu() -> None:
    """Выводит главное меню."""
    print("\n" + "=" * 50)
    print("УПРАВЛЕНИЕ КОЛЛЕКЦИЕЙ ОРУЖИЯ")
    print("=" * 50)
    print("1. Добавить оружие")
    print("2. Добавить меч")
    print("3. Добавить лук")
    print("4. Показать всё оружие")
    print("5. Найти по имени")
    print("6. Найти по редкости")
    print("7. Фильтр по уровню")
    print("8. Сортировка")
    print("9. Удалить по имени")
    print("0. Выход")
    print("-" * 50)


def get_int(prompt: str) -> int:
    """Безопасный ввод целого числа."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("   Ошибка: введите число")


def get_float(prompt: str) -> float:
    """Безопасный ввод числа с плавающей точкой."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("   Ошибка: введите число")


def get_bool(prompt: str) -> bool:
    """Ввод подтверждения (y/n)."""
    while True:
        val = input(prompt + " (y/n): ").lower()
        if val in ('y', 'yes', 'да', 'д'):
            return True
        if val in ('n', 'no', 'нет', 'н'):
            return False
        print("   Введите y или n")


def get_name(prompt: str) -> str:
    """Безопасный ввод имени (только буквы и пробелы)."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("   Ошибка: имя не может быть пустым")
            continue
        if all(c.isalpha() or c.isspace() for c in value):
            return value
        print("   Ошибка: имя должно содержать только буквы и пробелы")


def get_weapon_type(prompt: str) -> str:
    """Безопасный ввод типа оружия."""
    allowed = ['sword', 'bow', 'staff', 'dagger']
    while True:
        value = input(prompt).strip().lower()
        if value in allowed:
            return value
        print(f"   Ошибка: тип должен быть одним из {allowed}")


def get_rarity(prompt: str) -> str:
    """Безопасный ввод редкости."""
    allowed = ['common', 'rare', 'epic', 'legendary']
    while True:
        value = input(prompt).strip().lower()
        if value in allowed:
            return value
        print(f"   Ошибка: редкость должна быть одной из {allowed}")


def get_arrow_type(prompt: str) -> str:
    """Безопасный ввод типа стрел."""
    allowed = ['wood', 'metal', 'fire']
    while True:
        value = input(prompt).strip().lower()
        if value in allowed:
            return value
        print(f"   Ошибка: тип стрел должен быть одним из {allowed}")


def run(app: WeaponApp) -> None:
    """Запуск основного цикла CLI."""
    while True:
        print_menu()
        choice = get_int("Выберите пункт: ")

        if choice == 1:
            name = get_name("   Имя: ")
            wtype = get_weapon_type("   Тип (sword/bow/staff/dagger): ")
            rarity = get_rarity("   Редкость (common/rare/epic/legendary): ")
            try:
                app.add_weapon(name, wtype, rarity)
                print("   Оружие добавлено")
            except DuplicateWeaponError as e:
                print(f"   Ошибка: {e}")

        elif choice == 2:
            name = get_name("   Имя: ")
            rarity = get_rarity("   Редкость: ")
            length = get_float("   Длина лезвия (см): ")
            two_handed = get_bool("   Двуручный")
            try:
                app.add_sword(name, rarity, length, two_handed)
                print("   Меч добавлен")
            except DuplicateWeaponError as e:
                print(f"   Ошибка: {e}")

        elif choice == 3:
            name = get_name("   Имя: ")
            rarity = get_rarity("   Редкость: ")
            range_m = get_float("   Дальность (м): ")
            arrow = get_arrow_type("   Тип стрел (wood/metal/fire): ")
            try:
                app.add_bow(name, rarity, range_m, arrow)
                print("   Лук добавлен")
            except DuplicateWeaponError as e:
                print(f"   Ошибка: {e}")

        elif choice == 4:
            items = app.get_all()
            print(f"\n   Всего оружия: {len(items)}")
            for i, w in enumerate(items, 1):
                print(f"   {i}. {w.name} | {w.rarity} | урон {w.damage}")

        elif choice == 5:
            name = get_name("   Имя: ")
            found = app.find_by_name(name)
            print(f"\n   Найдено: {len(found)}")
            for w in found:
                print(f"   {w}")

        elif choice == 6:
            rarity = get_rarity("   Редкость: ")
            found = app.find_by_rarity(rarity)
            print(f"\n   Найдено: {len(found)}")
            for w in found:
                print(f"   {w}")

        elif choice == 7:
            min_lvl = get_int("   Минимальный уровень: ")
            filtered = app.filter_by_min_level(min_lvl)
            print(f"\n   Оружие с уровнем >= {min_lvl}: {len(filtered)} шт.")
            for i, w in enumerate(filtered, 1):
                print(f"   {i}. {w.name} | {w.rarity} | уровень {w.level} | урон {w.damage}")

        elif choice == 8:
            print("\n   Сортировать по:")
            print("   1. Имени")
            print("   2. Уровню")
            print("   3. Урону")
            sort_choice = get_int("   Выберите: ")
            rev = get_bool("   По убыванию")
            if sort_choice == 1:
                app.sort_by_name(rev)
            elif sort_choice == 2:
                app.sort_by_level(rev)
            elif sort_choice == 3:
                app.sort_by_damage(rev)
            else:
                print("   Неверный выбор")
                continue
            print("   Сортировка выполнена")

            items = app.get_all()
            print(f"\n   Отсортированное оружие ({len(items)} шт.):")
            for i, w in enumerate(items, 1):
                print(f"   {i}. {w.name} | {w.rarity} | уровень {w.level} | урон {w.damage}")

        elif choice == 9:
            name = get_name("   Имя для удаления: ")
            if not get_bool(f"   Удалить '{name}'"):
                print("   Удаление отменено")
                continue
            try:
                app.remove_by_name(name)
                print("   Удалено")
            except WeaponNotFoundError as e:
                print(f"   Ошибка: {e}")

        elif choice == 0:
            print("   До свидания")
            break

        else:
            print("   Неверный пункт меню")