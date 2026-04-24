
from base import Weapon
class WeaponCollection:
    def __init__(self):
        self._items = []
    
    def add(self, weapon: Weapon) -> bool:
        if not isinstance(weapon, Weapon):
            raise TypeError("Не является типом Weapon")
        if weapon in self._items:
            raise ValueError("Такой предмет уже есть")
        self._items.append(weapon)
        return True
    
    def remove(self, weapon: Weapon) -> bool:
        if weapon not in self._items:
            return False
        self._items.remove(weapon)
        return True
    
    def remove_at(self, index: int):
        if index < 0 or index >= len(self._items):
            raise IndexError("Номера нет в списке")
        return self._items.pop(index)
    
    def get_all(self) -> list:
        return self._items.copy()
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._items[index]
        if index < 0:
            index = len(self._items) + index
        if index < 0 or index >= len(self._items):
            raise IndexError("Диапазон нарушен")
        return self._items[index]
    
    def __contains__(self, weapon) -> bool:
        return weapon in self._items
    
    def __str__(self):
        if not self._items:
            return "Коллекция пуста"
        result = f"Коллекция оружия ({len(self._items)} шт.)\n"
        for i, weapon in enumerate(self._items):
            result += f"{i+1}. {weapon}\n"
        return result.strip()
    
    def filter_by_type(self, weapon_type):
        """Фильтрация по типу оружия (sword, bow, staff, dagger)"""
        new_collection = WeaponCollection()
        for weapon in self._items:
            if weapon.weapon_type == weapon_type:
                new_collection.add(weapon)
        return new_collection
    
    def get_only_swords(self):
        """Только мечи"""
        return self.filter_by_type("sword")
    
    def get_only_bows(self):
        """Только луки"""
        return self.filter_by_type("bow")