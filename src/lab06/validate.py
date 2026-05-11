

def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    name = name.strip()
    if not name:
        raise ValueError("Имя не может быть пустым")
    if len(name) < 2:
        raise ValueError("Имя должно содержать минимум 2 символа")
    return True

def validate_weapon_type(weapon_type, allowed_types):
    if not isinstance(weapon_type, str):
        raise TypeError("Тип оружия должен быть строкой")
    if weapon_type not in allowed_types:
        raise ValueError(f"Неизвестный тип. Доступны: {allowed_types}")
    return True

def validate_rarity(rarity, allowed_rarities):
    if not isinstance(rarity, str):
        raise TypeError("Редкость должна быть строкой")
    if rarity not in allowed_rarities:
        raise ValueError(f"Неизвестная редкость. Доступны: {allowed_rarities}")
    return True

def validate_level(level, min_level, max_level):
    if not isinstance(level, int):
        raise TypeError("Уровень должен быть целым числом")
    if level < min_level or level > max_level:
        raise ValueError(f"Уровень должен быть от {min_level} до {max_level}")
    return True

def validate_durability(durability, min_durability, max_durability):
    if not isinstance(durability, (int, float)):
        raise TypeError("Прочность должна быть числом")
    if durability < min_durability or durability > max_durability:
        raise ValueError(f"Прочность должна быть от {min_durability} до {max_durability}")
    return True

def validate_not_broken(is_broken, operation):
    if is_broken:
        raise ValueError(f"Невозможно {operation}! Оружие сломано!")
    return True

def validate_level_upgrade(current_level, new_level, max_level):
    if new_level < current_level:
        raise ValueError("Нельзя понизить уровень оружия!")
    if new_level > max_level:
        raise ValueError(f"Нельзя превысить максимальный уровень ({max_level})!")
    if new_level == current_level:
        raise ValueError("Оружие уже имеет этот уровень!")
    return True