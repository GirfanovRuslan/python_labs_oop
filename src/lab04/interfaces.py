from abc import ABC, abstractmethod
class Displayable (ABC):
    """Интерфейс для объектов, которые можно отобразить"""
    def display_info(self)-> str:
        """Вернуть строку с информацией"""
        pass
class Attackable(ABC):
    """Интерфейс для объектов, которые могут атаковать"""
    @abstractmethod
    def attack_power(self)->int:
        """Вернуть сиду атаки оружия"""
        pass
class Upgradable(ABC):
    """Интерфейс для объектов, которые можно улучшать"""
    @abstractmethod
    def upgrade(Self)-> bool:
        """Улучшить оружие"""
        pass
    