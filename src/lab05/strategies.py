from typing import Any, Callable
def by_name(item):
    """Сортировка по имени (ниж рег)"""
    return item.name.lower()
def by_level(item):
    """Сорт по уровню"""
    return item.level
def by_rarity(item):
    """Сорт по редкости"""
    rarity_orde = {"common": 0, "rare" : 1, "epic": 2, "legendary" : 3}
    return rarity_orde.get(item.rarity,0)


# фабрика функций 
def make_level_filter(min_level):
    def level_filter(item):
        return item.level>=min_level
    return level_filter
# функции фильтрыы
def is_legendary(item):
    return item.rarity == "legendary"

def is_not_broken(item):
    return not item.is_broken


# call объект 
class DamageBonusStrategy:
    """Callable объект , может хранить состояние и создание разных объектов"""
    
    def __init__ (self,bonus):
        self.bonus = bonus
    def __call__(self,item):
        item._damage += self.bonus
        return item
    
    
