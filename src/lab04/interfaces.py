from abc import ABC, abstractmethod
class Displayable (ABC):
    """Интерфейс для объектов, которые можно отобразить"""
    def display_info(self)-> str:
        """Вернуть строку с информацией"""
        pass

class Upgradable(ABC):
    """Интерфейс для объектов, которые можно улучшать"""
    @abstractmethod
    def upgrade(Self)-> bool:
        """Улучшить оружие"""
        pass
    