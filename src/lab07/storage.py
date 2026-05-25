import json
from typing import List, Dict, Any
from lab07.models import Weapon, Sword, Bow


def weapon_to_dict(weapon: Weapon) -> Dict[str, Any]:
    """Преобразует оружие в словарь для JSON."""
    data = {
        "type": weapon.__class__.__name__,
        "name": weapon.name,
        "weapon_type": weapon.weapon_type,
        "rarity": weapon.rarity,
        "level": weapon.level,
        "durability": weapon.durability,
        "damage": weapon.damage
    }

    if isinstance(weapon, Sword):
        data["blade_length"] = weapon.blade_length
        data["is_two_handed"] = weapon.is_two_handed
    elif isinstance(weapon, Bow):
        data["range_meters"] = weapon.range_meters
        data["arrow_type"] = weapon.arrow_type

    return data


def dict_to_weapon(data: Dict[str, Any]) -> Weapon:
    """Восстанавливает оружие из словаря."""
    name = data["name"]
    rarity = data["rarity"]

    if data["type"] == "Sword":
        return Sword(name, rarity, data["blade_length"], data["is_two_handed"])
    elif data["type"] == "Bow":
        return Bow(name, rarity, data["range_meters"], data["arrow_type"])
    else:
        return Weapon(name, data["weapon_type"], rarity)


def save(collection, filepath: str) -> None:
    """Сохраняет коллекцию в JSON-файл."""
    data = [weapon_to_dict(item) for item in collection.get_all()]
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load(filepath: str, collection) -> None:
    """Загружает коллекцию из JSON-файла (если существует)."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            for item_data in data:
                weapon = dict_to_weapon(item_data)
                collection.add(weapon)
    except FileNotFoundError:
        pass