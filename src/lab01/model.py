import validate
class Weapon:
    """Класс оружия в игре"""
    WEAPON_TYPES={"sword": "Меч",
                  "bow": "Лук",
                  "staff": "Посох",
                  "dagger": "Кинжал"}
    RARITY_MULTIPLIERS = {"common": 1.0,
                          "rare": 1.5,
                          "epic": 2.0,
                          "legendary" : 3.0}
    MAX_LEVEL = 10
    MIN_LEVEL = 1 
    MAX_DURABILITY =  100
    MIN_DURABILITY = 0 
    def __init__(self, name: str,  weapon_type: str, rarity: str = "common"):
        validate.validate_name(name)
        validate.validate_weapon_type(weapon_type,self.WEAPON_TYPES.keys())
        validate.validate_rarity(rarity, self.RARITY_MULTIPLIERS.keys())
        self._name = name.strip()
        self._weapon_type=weapon_type
        self._rarity = rarity
        self._level = 1
        self._durability = 100
        self._damage = self._calculate_damage()
    def _calculate_damage(self):
        base_damage={"sword": 10,
                     "bow": 8,
                     "staff": 12,
                     "dagger": 6}
        base=base_damage.get(self._weapon_type,10)
        multiplier = self.RARITY_MULTIPLIERS.get(self.rarity,10)
        level_bonus= 1+(self._level-1)*0.2
        return int(base*multiplier*level_bonus)
    @property
    def name(self):
        """Имя оружия, чтение"""
        return self._name
    @property
    def weapon_type(self):
        """Тип оружия, чтение"""
        return self._weapon_type
    @property
    def rarity(self):
        """Редкость, чтение"""
        return self._rarity
    @property
    def level(self):
        """Уровень, чтение"""
        return self._level     
    
    @level.setter
    def level(self,value):
        validate.validate_not_broken(self.is_broken,"Улучшить оружие")
        validate.validate_level(value, self.MIN_LEVEL, self.MAX_LEVEL)
        validate.validate_level_upgrade(self._level,value, self.MAX_LEVEL)
        self._level=value
        self._damage = self._calculate_damage()
        print(f"Уровень повышен до {value}")
    @property
    def durability(self):
        """Прочность оружия, чтение"""
        return self._durability
    @durability.setter
    def durability(self, value):
        """Установить прочность, с проверкой"""
        validate.validate_durability(value,self.MIN_DURABILITY, self.MAX_DURABILITY) 
        old_value=self._durability
        self._durability=value
        if self.durability == 0 and old_value > 0 :
            print("Оружие сломано, нужен ремонт") 
        elif self._durability <30 and self._durability >0:
            print("Оружие в плохом состоянии") 
        elif self.durability>old_value:
            print("Оружие отремонтировано")     
    @property
    def damage(self):
        """Урон оружия, чтение"""
        return self._damage
    @property
    def is_broken(self):
        return self._durability <=0
    @property
    def description(self):
        """Характеристики оружия"""
        return (f"{self._rarity} {self._weapon_type} '{self._name}' (ур.{self._level}, урон {self._damage}")
# Magicheskie metods
    def __str__(self):
        """Преобразовывает объект в строку"""
        return self.description
    def __repr__(self):
        """В строку для разраба """
        return f"Weapon('{self._name}', '{self._weapon_type}', '{self._rarity}')"
    def __eq__(self, other):
        if not isinstance(other, Weapon):
            return False
        return (self._name == other._name and 
                self._weapon_type == other._weapon_type and 
                self._rarity == other._rarity and
                self._level == other._level)
# Если сравниваем объект с другого класса, они не равны
        return (self._name == other._name and 
                self._weapon_type == other._weapon_type and 
                self._rarity == other._rarity and
                self._level == other._level)
    def upgrade(self):
        """Улучшить оружие на 1 уровень"""
        if self._level >= self.MAX_LEVEL:
            print(f"Оружие уже имеет максимальный уровень ({self.MAX_LEVEL})!")
            return False
        self.level = self._level + 1
        return True

    def repair(self):
        """Починить оружие до 100%"""
        self.durability = self.MAX_DURABILITY
        return True

    def attack(self):
        """Атаковать оружием"""
        validate.validate_not_broken(self.is_broken, "атаковать")
        loss_table = {
            'legendary': 5,
            'epic': 10,
            'rare': 15,
            'common': 20
        }
        durability_loss = loss_table.get(self._rarity, 20)
        new_durability = self._durability - durability_loss
        if new_durability < 0:
            new_durability = 0
        self.durability = new_durability
        return self._damage

    def get_status(self):
        """Получить полный статус оружия"""
        status = "СЛОМАНО" if self.is_broken else "ИСПРАВНО"
        return (f"{self._name} | "
                f"Тип: {self.WEAPON_TYPES[self._weapon_type]} | "
                f"Редкость: {self._rarity.upper()} | "
                f"Уровень: {self._level}/{self.MAX_LEVEL} | "
                f"Урон: {self._damage} | "
                f"Прочность: {self._durability}% | "
                f"Состояние: {status}")