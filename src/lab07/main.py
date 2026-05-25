import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab07.app import WeaponApp
from lab07.cli import run
from lab07.storage import save, load

DATA_FILE = "weapons.json"


def main() -> None:
    """Главная функция приложения."""
    app = WeaponApp()
    load(DATA_FILE, app.get_collection())
    print(f"Загружено {len(app)} единиц оружия")
    run(app)
    save(app.get_collection(), DATA_FILE)
    print(f"Сохранено {len(app)} единиц оружия")


if __name__ == "__main__":
    main()