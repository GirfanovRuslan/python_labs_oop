# Лабораторная работа №6

## 1. Цель работы

Освоение системы аннотаций типов (typing), создание обобщённых (generic) коллекций с помощью TypeVar и Generic, понимание структурной типизации через Protocol.

## 2. Реализованные типы и контейнеры

### Generic-коллекция TypedCollection[T]

Обобщённая версия коллекции из ЛР-2 (WeaponCollection). Хранит объекты любого типа T, но сохраняет информацию о типе.

**Методы коллекции (все из ЛР-2 + новые):**

| Категория | Методы |
|-----------|--------|
| Базовые | add, remove, remove_at, get_all, clear |
| Поиск | find_by_name, find_by_type, find_by_rarity, find_by_level |
| Магические | __len__, __iter__, __getitem__, __contains__, __str__, __repr__ |
| Сортировка | sort_by_name, sort_by_level, sort_by_damage, sort_by_rarity, sort |
| Фильтрация (новая коллекция) | filter_by_rarity, filter_by_min_level, filter_by_min_durability |
| Удобные фильтры | get_legendary, get_epic, get_rare, get_common, get_broken, get_repairable |
| Новые (ЛР-6) | find, filter, map |

### Protocols (структурные интерфейсы)

| Protocol | Метод | Требование |
|----------|-------|-------------|
| Displayable | display() -> str | объект можно отобразить |
| Scorable | score() -> float | объект можно оценить |

Ограничения:
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

### TypeVar

| Переменная | Назначение |
|------------|-----------|
| T | любой тип |
| D | только с методом display() |
| S | только с методом score() |
| R | тип результата преобразования (для map) |

## 3. Демонстрация работы

### Сценарий 1: базовые операции + поиск + сортировка

Создаётся TypedCollection[Weapon], добавляются объекты, вызываются методы из ЛР-2.

### Сценарий 2: find, filter, map

Показывается:
- поиск первого легендарного оружия (find)
- фильтрация легендарного оружия (filter)
- преобразование в имена (map -> list[str])
- преобразование в урон (map -> list[int])

### Сценарий 3: Protocols

Создаются коллекции с ограничениями Displayable и Scorable. У объектов вызываются методы display() и score().




![Вывод всех сценариев](<../../images/lab06/image copy 3.png>)




## 4. Вывод

В ходе работы реализованы:

- Generic-коллекция с сохранением всех методов ЛР-2
- Аннотации типов для всех методов
- find / filter / map с корректной типизацией
- Protocol (утиная типизация без явного наследования)
- TypeVar с ограничениями (bound)
- Демонстрация изменения типа в map
