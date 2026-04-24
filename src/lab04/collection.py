from lab04.interfaces import Displayable, Attackable
class WeaponCollection:
    """Коллекция для хранения объектов Weapon"""
    def __init__(self):
        self._items=[]
    def add(self, weapon)-> bool:
        """Добавляет объект в коллекцию:)"""
        self._items.append(weapon)
        return True
    def get_all(self):
        """Копия списка"""
        return self._items.copy()
    def __len__(self):
        """Маг метод, нужен для длины коллекции"""
        return len(self._items)
    def __iter__(self):
       """Маг метод, для цикла, for и т д"""
       return iter(self._items)
    def __str__(self):
        """маг метод, красивый принт"""
        if not self._items:
            return "Пусто"        
        result= f"Коллекция оружия ({len(self._items)} шт) \n"
        for i, weapon in enumerate(self._items):
            result += f"{i+1}. {weapon} \n"
        return result.strip()
# новые методы фильтрации по интерфейсу
    def get_displayable(self):
        """Вернет новую коллекцию, в которуй будут объекты использующие интерфейс Displayable"""
        new_collection=WeaponCollection()
        for item in self._items:
            if isinstance(item, Displayable):
                new_collection.add(item)
        return new_collection
    def get_attackable(self):
        """Вернет коллекцию, в которой обЪекты используют интерфейс Attackable"""
        new_collection=WeaponCollection()
        for item in self._items:
            if isinstance(item, Attackable):
                new_collection.add(item)
        return new_collection
    