class WeaponCollection : 
    """Коллекция моя"""
    
    def __init__(self):
        self._items = []
    
    def add(self, item):
        """Добавялет объекты"""
        self._items.append(item)
    
    def get_all(self):
        """Копия """
        return self._items.copy()
    
    def __len__(self, item):
        """Длина списка"""
        return len(self._items)
    
    def __iter__(self, item):
        """Маг метод, для цикла"""
        return iter(self._items)
    
    def __str__(self):
        """МАг метод. красивый вывод"""
        if not self._items:
            return "Коллекция пуста" 
        result = f"Коллекция оружия ({len(self._items)} шт.)\n" 
        for i, item in enumerate(self._items):
            result +=f"{i+1}. {item}\n"
        return result.strip()

# методы со стратегиями 
    def sort_by(self, key_func, reverse=False):
        """Отсортирует коллекцию по функции ключу """
        self._items.sort(key=key_func, reverse = reverse)
        return self
    def filter_by(self, predicate):
        """Фильтрует коллекцию по переданному условию"""       
        self._items  =list(filter(predicate, self._items))
        return self
    def apply(self, func):
        self._items = list(map(func,self._items))
        return self
    def copy(self):
        """Копия коллекция """
        new_collection = WeaponCollection()
        for item in self._items:
            new_collection.add(item)
        return new_collection