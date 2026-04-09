

from model import Weapon

class WeaponCollection:
    """Класс для хранения колекции объектов Weapon"""
    def __init__(self):
        """Создаем пустой список для оружия"""
        self._items=[] # закрытый spisok
    def add(self, weapon: Weapon) ->bool:
        """Добавляем оружие в коллекцию, проверяет тип и на повторяемость предмета"""
        if not isinstance(weapon, Weapon):
            raise TypeError("Не является типом Weapon")
        if weapon in self._items:
            raise ValueError("Такой предмет уже есть")
        self._items.append(weapon)
        return True
    def remove(self,weapon:Weapon) -> bool:
        """Удаляет оружие из коллекции"""
        if weapon not in self._items:
            return False
        self._items.remove(weapon)
        return True
    def remove_at(self, index: int):
        """Удаляет по позиции в списке"""
        if index<0 or index>=len(self._items):
            raise IndexError("Номера нет в списке")
        return self._items.pop(index)# Pop удаляет элемент  по номеру
    def get_all(self)->list:
        """Копия списка, оригинал нельзя изменить"""
        return self._items.copy()
    def clear(self):
        """удаляет все и всех"""
        self._items.clear()
    def find_by_name(self,name: str)-> list:
        """Ищет оружие по иммени"""
        result=[]
        for weapon in self._items:
            if weapon.name.lower()== name.lower():
                #  получаем имя через геттер
                result.append(weapon)
        return result
    def find_by_type(self,weapon_type: str)-> list:
        """Ищет оружие типа, sword и т д"""
        result =[]
        for weapon in self._items:
            if weapon.weapon_type == weapon_type:
                result.append(weapon)
        return result
    def find_by_rarity(self, rarity: str)-> list:
        """Ищет оружие по редкости, по типу common и т д"""
        result= []
        for weapon in self._items:
            if weapon.rarity==rarity:
                result.append(weapon)
        return result 
    def find_by_level(self,level: int) -> list:
        """Ищет оружие по уровню"""
        result=[]
        for weapon in self._items:
            if weapon.level==level:
                result.append(weapon)
        return result
    def __len__(self):
        """Полуачем количество элементов из коллекции"""
        return len(self._items)
    def __iter__(self):
        """Возращает итератор для перебора элементов"""
        return iter(self._items)
    def __getitem__(self, index):
        """Позволяет обращаться по индексу и делать срезы"""
        if isinstance(index, slice):
            return self._items[index]
    # Преобразуем отрицательный индекс в положительный
        if index < 0:
            index = len(self._items) + index
        if index < 0 or index >= len(self._items):
            raise IndexError("Диапазон нарушен")
        return self._items[index]
    def __contains__(self, weapon)->bool:
        """Проверяет наличие оружия в коллекции"""
        return weapon in self._items
    def __str__(self):
        """Возвращает коллекцию"""
        if not self._items:
            return "Коллекция пуста"
        result = f"Коллекция оружия ({len(self._items)} шт.)\n"
        for i, weapon in enumerate(self._items):
            result += f"{i+1}. {weapon}\n"
        return result.strip()
    def __repr__(self)-> str:
        """Возвращает консол для разработчиков"""
        return f"WeaponCollection({self._items})"
# Сортировка
    def sort_by_name(self, reverse: bool = False):
        """Сортировка по имени в алф порядке"""
        self._items.sort(key=lambda w: w.name.lower(), reverse=reverse)
    def sort_by_level(self, reverse: bool = False):
        """Сортировка коллекции по уровню оружия."""
        # key=lambda берёт уровень оружия для сравнения
        self._items.sort(key=lambda w: w.level, reverse=reverse)
    
    def sort_by_damage(self, reverse: bool = False):
        """Сортировка коллекции по урону оружия."""
        self._items.sort(key=lambda w: w.damage, reverse=reverse)
    def sort_by_rarity(self, reverse: bool = False):
        """
        Сортировка коллекции по редкости.
        """
        # Словарь  редкости к числовому значению 
        rarity_order = {'common': 0, 'rare': 1, 'epic': 2, 'legendary': 3}
        # lambda берёт числовое значение редкости из словаря
        self._items.sort(key=lambda w: rarity_order.get(w.rarity, 0), reverse=reverse)
    def filter_by_rarity(self, rarity: str):
        """
        Создаёт и возвращает новую коллекцию с оружием заданной редкости.
        """
        new_collection = WeaponCollection() 
        for weapon in self._items:  
            if weapon.rarity == rarity:  
                new_collection.add(weapon)  
        return new_collection
    
    def filter_by_min_level(self, min_level: int):
        """
        Создаёт новую коллекцию с оружием, уровень которого больше мин lVL
        """
        new_collection = WeaponCollection()
        for weapon in self._items:
            if weapon.level >= min_level:
                new_collection.add(weapon)
        return new_collection
    
    def filter_by_min_durability(self, min_durability: int = 50):
        """
        Создаёт новую коллекцию с оружием, прочность которого большего минимального
        """
        new_collection = WeaponCollection()
        for weapon in self._items:
            if weapon.durability >= min_durability:
                new_collection.add(weapon)
        return new_collection
    
# ВСЕ