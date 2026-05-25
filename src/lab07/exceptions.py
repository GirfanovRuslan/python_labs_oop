class WeaponNotFoundError(Exception):
    """Оружие не найдено в коллекции."""
    pass


class DuplicateWeaponError(Exception):
    """Оружие с таким именем уже существует."""
    pass