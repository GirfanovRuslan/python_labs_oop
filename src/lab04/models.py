import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lab04.interfaces import Displayable, Upgradable
class Weapon:
    """Класс для всего оружия из первой лабы"""
    
    def __init__(self, name:str , weapon_type: str, rarity : str = "common"):
        self._name = name
        self._weapon_type = weapon_type
        self._rarity = rarity
        self._level =1
        self._damage = self._calculate_base_damage()
   
    def _calculate_base_damage(self):
        """Приват метод для расчета урона"""
        base_damage = {"sword": 10, "bow" : 8, "staff": 12, "dagger" : 6}
        return base_damage.get(self._weapon_type, 10)
    
    @property 
    def name(self):
        """Геттер имя"""
        return self._name
    
    @property
    def damage(self):
        """Геттер урона"""
        return self._damage
   
    @property 
    def level(self):
        """Геттер уровня"""
        return self._level
    
    def __str__(self):
        """"Metod dlya krasivogo вывода"""
        return f"{self._rarity} {self._weapon_type} '{self._name}' (ур.{self._level}, урон {self._damage})"
# Класс меча :) 
class Sword(Weapon, Displayable, Upgradable):
    """Класс для меча, который наследует  класс Weapon и интерфейсы Displayable, Attackable, Upgradable """
    
    def __init__(self, name: str, rarity : str = "common", blade_length : float = 80.0):
        """Конструктор меча, плюс длина лезвия"""
        super().__init__(name,"sword", rarity)
        self._blade_length = blade_length
    
    def display_info(self)-> str:
        """Метод из интерфейса Displayable"""
        return f"Меч '{self._name}', длина лезвия: {self._blade_length} см, урон: {self._damage}"
    
    def upgrade(self) -> bool:
        """Улучшает меч, увеличивает урон на 20 проц"""
        self._damage+= int(self._damage *0.2)
        print(f"Меч '{self._name}' улучшен, урон на данный момент: {self._damage}")
        return True


# Класс лука
class Bow(Weapon, Displayable,Upgradable):
    
    def __init__(self, name: str, rarity: str = "common", range_meters: float = 50.0):
        super().__init__(name, "bow", rarity)
        self._range_meters = range_meters
    
    def display_info(self)-> str:
        """Реализация Displayable для лука"""
        return f"Лук '{self._name}', дальность: {self._range_meters} м, урон: {self._damage}"
    
    def upgrade(self)-> bool:
        """Реализует Upgradable + к дальности""" 
        self._range_meters+=10
        print(f"Лук '{self._name}' улучшен, дальность: {self._range_meters}")
        return True
           
 # Класс посох, он не улучшается и не атакует 
class Staff(Weapon, Displayable):
    
    def __init__(self, name: str, rarity: str= "common"):
        super().__init__(name, "staff" ,  rarity)
    
    def display_info(self) -> str:
        """Реализация Displayable """
        return f"Посох '{self._name}', урон: {self._damage}"
    
         
          
       