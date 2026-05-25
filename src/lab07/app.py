from typing import List
from lab06.container import TypedCollection
from lab07.models import Weapon, Sword, Bow
from lab07.exceptions import DuplicateWeaponError, WeaponNotFoundError


class WeaponApp:
    """Бизнес-логика приложения для управления оружием."""

    def __init__(self) -> None:
        self._collection: TypedCollection[Weapon] = TypedCollection()

    def add_weapon(self, name: str, weapon_type: str, rarity: str) -> None:
        """Добавляет оружие. Проверяет дубликаты по имени."""
        if self._collection.find_by_name(name):
            raise DuplicateWeaponError(f"Оружие с именем '{name}' уже существует")

        weapon = Weapon(name, weapon_type, rarity)
        self._collection.add(weapon)

    def add_sword(self, name: str, rarity: str, blade_length: float, is_two_handed: bool) -> None:
        """Добавляет меч."""
        if self._collection.find_by_name(name):
            raise DuplicateWeaponError(f"Оружие с именем '{name}' уже существует")

        sword = Sword(name, rarity, blade_length, is_two_handed)
        self._collection.add(sword)

    def add_bow(self, name: str, rarity: str, range_meters: float, arrow_type: str) -> None:
        """Добавляет лук."""
        if self._collection.find_by_name(name):
            raise DuplicateWeaponError(f"Оружие с именем '{name}' уже существует")

        bow = Bow(name, rarity, range_meters, arrow_type)
        self._collection.add(bow)

    def remove_by_name(self, name: str) -> None:
        """Удаляет оружие по имени (первое найденное)."""
        to_remove = self._collection.find_by_name(name)
        if not to_remove:
            raise WeaponNotFoundError(f"Оружие с именем '{name}' не найдено")

        for weapon in to_remove:
            self._collection.remove(weapon)

    def get_all(self) -> List[Weapon]:
        """Возвращает все оружие."""
        return self._collection.get_all()

    def find_by_name(self, name: str) -> List[Weapon]:
        """Поиск по имени."""
        return self._collection.find_by_name(name)

    def find_by_rarity(self, rarity: str) -> List[Weapon]:
        """Поиск по редкости."""
        return self._collection.find_by_rarity(rarity)

    def filter_by_min_level(self, min_level: int) -> List[Weapon]:
        """Фильтрация по минимальному уровню."""
        return self._collection.filter_by_min_level(min_level).get_all()

    def sort_by_name(self, reverse: bool = False) -> None:
        """Сортировка по имени."""
        self._collection.sort_by_name(reverse)

    def sort_by_level(self, reverse: bool = False) -> None:
        """Сортировка по уровню."""
        self._collection.sort_by_level(reverse)

    def sort_by_damage(self, reverse: bool = False) -> None:
        """Сортировка по урону."""
        self._collection.sort_by_damage(reverse)

    def get_collection(self):
        """Возвращает коллекцию (для storage)."""
        return self._collection

    def __len__(self) -> int:
        return len(self._collection)