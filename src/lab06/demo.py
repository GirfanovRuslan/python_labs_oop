import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab01.model import Weapon
from lab03.models import Sword, Bow
from lab06.container import TypedCollection, Displayable, Scorable


def patch():
    def display(self):
        return f"{self.name} (урон: {self.damage})"
    def score(self):
        return float(self.damage)
    for cls in (Weapon, Sword, Bow):
        if not hasattr(cls, 'display'):
            cls.display = display
        if not hasattr(cls, 'score'):
            cls.score = score


def main():
    patch()
    print("=== ЛР-6: GENERICS, PROTOCOLS, FIND/FILTER/MAP ===\n")

    # ----- сценарий 1: вся функциональность ЛР-2 -----
    print("СЦЕНАРИЙ 1: методы из ЛР-2")
    col = TypedCollection[Weapon]()
    col.add(Sword("Экскалибур", "legendary", 90))
    col.add(Bow("Лунный лук", "epic", 80))
    col.add(Sword("Меч кладенец", "rare", 85))

    print("get_all:", [w.name for w in col.get_all()])
    print("find_by_rarity(legendary):", [w.name for w in col.find_by_rarity("legendary")])
    col.sort_by_name()
    print("sort_by_name:", [w.name for w in col.get_all()])
    print("get_legendary():", [w.name for w in col.get_legendary().get_all()])

    # ----- сценарий 2: find / filter / map -----
    print("\nСЦЕНАРИЙ 2: find / filter / map")
    col2 = TypedCollection[Weapon]()
    col2.add(Sword("Меч A", "common", 80))
    col2.add(Sword("Меч B", "legendary", 85))
    col2.add(Bow("Лук C", "epic", 70))

    print("find (легендарка):", col2.find(lambda x: x.rarity == "legendary"))
    print("filter (легендарка):", [w.name for w in col2.filter(lambda x: x.rarity == "legendary")])
    print("map -> имена:", col2.map(lambda x: x.name))
    print("map -> урон:", col2.map(lambda x: x.damage))

    # ----- сценарий 3: Protocols + bound -----
    print("\nСЦЕНАРИЙ 3: Protocols + bound")
    disp: TypedCollection[D] = TypedCollection()
    disp.add(Sword("Sword X", "rare", 100))
    disp.add(Bow("Bow Y", "epic", 90))

    print("display():")
    for d in disp:
        print(" ", d.display())

    sc: TypedCollection[S] = TypedCollection()
    sc.add(Sword("Sword Z", "legendary", 120))
    sc.add(Bow("Bow W", "common", 50))

    print("score():")
    for s in sc:
        print(" ", s.name, "→", s.score())


if __name__ == "__main__":
    main()