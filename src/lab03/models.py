from base import Weapon

class Sword(Weapon):
    """Класс для меча, длина лезвия и одноручный или двуручный + заточка"""
    
    def __init__(self, name: str, rarity: str = "common", blade_length: float = 80.0, is_two_handed: bool = False):
        super().__init__(name, "sword", rarity)
        self._blade_length = blade_length  
        self._is_two_handed = is_two_handed  
        
    @property
    def blade_length(self):
        """Длина лезвия, в см, чтение"""
        return self._blade_length  
    
    @property
    def is_two_handed(self):
        """Правда если меч двуручный, не правда если одноручный"""
        return self._is_two_handed 
    
    def __str__(self):
        base_str = super().__str__()
        if self._is_two_handed:
            hand = "двуручный"
        else:
            hand = "одноручный"
        return f"{base_str} {hand} меч, лезвие {self._blade_length} см"  
    
    def sharpen(self):
        """Метод, заточка для меча:)"""
        bonus_damage = int(self._damage * 0.2)
        self._damage += bonus_damage  
        print(f"Меч '{self._name}' заточен, урон увеличен на {bonus_damage}, ура")
        return self._damage
    
    def get_special_bonus(self):
        """Полиморфный метод, возвращает бонус для меча"""
        return f"Меч '{self._name}' даёт +10 к урону"  


class Bow(Weapon):
    """Класс для лука, дальность и тип стрел""" 
    
    def __init__(self, name: str, rarity: str = "common", range_meters: float = 50.0, arrow_type: str = "wood"):
        super().__init__(name, "bow", rarity)
        self._range_meters = range_meters 
        self._arrow_type = arrow_type 
        
    @property
    def range_meters(self):
        """чтение дальность стрельбы"""
        return self._range_meters
    
    @property
    def arrow_type(self):
        """чтение, тип стрел"""
        return self._arrow_type 
    
    def __str__(self):
        base_str = super().__str__()
        """Словарь стрел"""
        arrow_names = {
            "wood": "деревянные",
            "metal": "металлические",
            "fire": "огненные"
        }
        arrow_rus = arrow_names.get(self._arrow_type, self._arrow_type)  
        return f"{base_str} лук, дальность {self._range_meters} м, стрелы: {arrow_rus}"  
   
    def upgrade_bow(self):
        """улучшение лука"""
        self._range_meters += 10
        print(f"Лук '{self._name}' улучшен, дальность теперь {self._range_meters} м")
        return self._range_meters
    
    def get_special_bonus(self):
        """Возвращает бонус лука"""
        return f"Лук '{self._name}' даёт +20 к дальности"
    
    def process(self):
        """Общий интерфейс для обработки оружия"""
        return self.upgrade_bow()