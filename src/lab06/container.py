from typing import TypeVar, Generic, Callable, Optional, List, Protocol

class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить"""
    def display(self) -> str:
        ...


class Scorable(Protocol):
    """Протокол для объектов, которые можно оценить"""
    def score(self) -> float:
        ...



# TYPEVAR


T = TypeVar('T')                      
D = TypeVar('D', bound=Displayable)   
S = TypeVar('S', bound=Scorable)      
R = TypeVar('R')                      


# КОЛЛЕКЦИЯ

class TypedCollection(Generic[T]):
    """Generic-коллекция для хранения объектов"""
    
    def __init__(self) -> None:
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        """Добавить элемент"""
        self._items.append(item)
    
    def remove(self, item: T) -> None:
        """Удалить элемент"""
        self._items.remove(item)
    
    def get_all(self) -> List[T]:
        """Вернуть копию списка"""
        return self._items.copy()
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Найти первый подходящий элемент"""
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Вернуть список подходящих элементов"""
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Преобразовать элементы и вернуть список"""
        return [transform(item) for item in self._items]