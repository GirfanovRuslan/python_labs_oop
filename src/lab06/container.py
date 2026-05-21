from typing import TypeVar, Generic, Callable, Optional, List, Protocol


class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


T = TypeVar('T')
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)
R = TypeVar('R')


class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    #  базовые операции 
    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def remove_at(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def get_all(self) -> List[T]:
        return self._items.copy()

    def clear(self) -> None:
        self._items.clear()

    #  поиск 
    def find_by_name(self, name: str) -> List[T]:
        return [i for i in self._items if hasattr(i, 'name') and i.name.lower() == name.lower()]

    def find_by_type(self, weapon_type: str) -> List[T]:
        return [i for i in self._items if hasattr(i, 'weapon_type') and i.weapon_type == weapon_type]

    def find_by_rarity(self, rarity: str) -> List[T]:
        return [i for i in self._items if hasattr(i, 'rarity') and i.rarity == rarity]

    def find_by_level(self, level: int) -> List[T]:
        return [i for i in self._items if hasattr(i, 'level') and i.level == level]

    #  магические 
    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._items[index]
        if index < 0:
            index = len(self._items) + index
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items[index]

    def __contains__(self, item: T) -> bool:
        return item in self._items

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"
        lines = [f"{i+1}. {item}" for i, item in enumerate(self._items)]
        return f"Коллекция ({len(self._items)} шт.)\n" + "\n".join(lines)

    def __repr__(self) -> str:
        return f"TypedCollection({self._items})"

    #  сортировка
    def sort_by_name(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.name.lower() if hasattr(x, 'name') else "", reverse=reverse)

    def sort_by_level(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.level if hasattr(x, 'level') else 0, reverse=reverse)

    def sort_by_damage(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda x: x.damage if hasattr(x, 'damage') else 0, reverse=reverse)

    def sort_by_rarity(self, reverse: bool = False) -> None:
        rarity_order = {'common': 0, 'rare': 1, 'epic': 2, 'legendary': 3}
        self._items.sort(key=lambda x: rarity_order.get(x.rarity, 0) if hasattr(x, 'rarity') else 0, reverse=reverse)

    def sort(self, key: Callable[[T], any], reverse: bool = False) -> None:
        self._items.sort(key=key, reverse=reverse)

    # ---------- фильтрация (новая коллекция) ----------
    def filter_by_rarity(self, rarity: str) -> 'TypedCollection[T]':
        new = TypedCollection[T]()
        for i in self._items:
            if hasattr(i, 'rarity') and i.rarity == rarity:
                new.add(i)
        return new

    def filter_by_min_level(self, min_level: int) -> 'TypedCollection[T]':
        new = TypedCollection[T]()
        for i in self._items:
            if hasattr(i, 'level') and i.level >= min_level:
                new.add(i)
        return new

    def filter_by_min_durability(self, min_durability: int = 50) -> 'TypedCollection[T]':
        new = TypedCollection[T]()
        for i in self._items:
            if hasattr(i, 'durability') and i.durability >= min_durability:
                new.add(i)
        return new

    #  удобные фильтры 
    def get_legendary(self) -> 'TypedCollection[T]':
        return self.filter_by_rarity('legendary')

    def get_epic(self) -> 'TypedCollection[T]':
        return self.filter_by_rarity('epic')

    def get_rare(self) -> 'TypedCollection[T]':
        return self.filter_by_rarity('rare')

    def get_common(self) -> 'TypedCollection[T]':
        return self.filter_by_rarity('common')

    def get_broken(self) -> 'TypedCollection[T]':
        new = TypedCollection[T]()
        for i in self._items:
            if hasattr(i, 'is_broken') and i.is_broken:
                new.add(i)
        return new

    def get_repairable(self) -> 'TypedCollection[T]':
        return self.filter_by_min_durability(50)

    # методы ЛР-6
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for i in self._items:
            if predicate(i):
                return i
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        return [i for i in self._items if predicate(i)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        return [transform(i) for i in self._items]