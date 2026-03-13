class Weapon:
    """Класс оружия для игры"""
    
    # ----- АТРИБУТЫ КЛАССА (общие для всех объектов) -----
    WEAPON_TYPES = {
        'sword': 'Меч',
        'bow': 'Лук',
        'staff': 'Посох',
        'dagger': 'Кинжал'
    }
    
    RARITY_MULTIPLIERS = {
        'common': 1.0,    # обычное
        'rare': 1.5,      # редкое
        'epic': 2.0,      # эпическое
        'legendary': 3.0  # легендарное
    }
    
    # Константы
    MAX_LEVEL = 10
    MIN_LEVEL = 1
    MAX_DURABILITY = 100
    MIN_DURABILITY = 0
    
    # ----- КОНСТРУКТОР -----
    def __init__(self, name: str, weapon_type: str, rarity: str = 'common'):
        """
        Создание нового оружия
        :param name: название (например, "Экскалибур")
        :param weapon_type: тип (sword, bow, staff, dagger)
        :param rarity: редкость (common, rare, epic, legendary)
        """
        
        # Валидация входных данных
        self._validate_name(name)
        self._validate_weapon_type(weapon_type)
        self._validate_rarity(rarity)
        
        # Закрытые атрибуты (с подчеркиванием)
        self._name = name                # имя
        self._weapon_type = weapon_type  # тип
        self._rarity = rarity            # редкость
        self._level = 1                   # уровень (начинается с 1)
        self._durability = 100            # прочность (100%)
        self._damage = self._calculate_damage()  # урон (вычисляется)
    
    # ----- МЕТОДЫ ВАЛИДАЦИИ (все с _ в начале) -----
    
    def _validate_name(self, name):
        """Проверка имени"""
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if len(name.strip()) < 2:
            raise ValueError("Имя должно содержать минимум 2 символа")
        return True
    
    def _validate_weapon_type(self, weapon_type):
        """Проверка типа оружия"""
        if not isinstance(weapon_type, str):
            raise TypeError("Тип оружия должен быть строкой")
        if weapon_type not in self.WEAPON_TYPES:
            types = ', '.join(self.WEAPON_TYPES.keys())
            raise ValueError(f"Неизвестный тип. Доступны: {types}")
        return True
    
    def _validate_rarity(self, rarity):
        """Проверка редкости"""
        if not isinstance(rarity, str):
            raise TypeError("Редкость должна быть строкой")
        if rarity not in self.RARITY_MULTIPLIERS:
            rarities = ', '.join(self.RARITY_MULTIPLIERS.keys())
            raise ValueError(f"Неизвестная редкость. Доступны: {rarities}")
        return True
    
    def _validate_level(self, level):
        """Проверка уровня"""
        if not isinstance(level, int):
            raise TypeError("Уровень должен быть целым числом")
        if level < self.MIN_LEVEL or level > self.MAX_LEVEL:
            raise ValueError(f"Уровень должен быть от {self.MIN_LEVEL} до {self.MAX_LEVEL}")
        return True
    
    def _validate_durability(self, durability):
        """Проверка прочности"""
        if not isinstance(durability, (int, float)):
            raise TypeError("Прочность должна быть числом")
        if durability < self.MIN_DURABILITY or durability > self.MAX_DURABILITY:
            raise ValueError(f"Прочность должна быть от {self.MIN_DURABILITY} до {self.MAX_DURABILITY}")
        return True
    
    def _calculate_damage(self):
        """Расчет урона на основе типа, редкости и уровня"""
        base_damage = {
            'sword': 10,
            'bow': 8,
            'staff': 12,
            'dagger': 6
        }
        base = base_damage.get(self._weapon_type, 10)
        multiplier = self.RARITY_MULTIPLIERS.get(self._rarity, 1.0)
        return base * multiplier * self._level
    
    # ----- ГЕТТЕРЫ (чтение данных) -----
    
    @property
    def name(self):
        """Имя оружия (только чтение)"""
        return self._name
    
    @property
    def weapon_type(self):
        """Тип оружия (только чтение)"""
        return self._weapon_type
    
    @property
    def rarity(self):
        """Редкость оружия (только чтение)"""
        return self._rarity
    
    @property
    def level(self):
        """Уровень оружия"""
        return self._level
    
    @level.setter
    def level(self, value):
        """Установка уровня с проверкой"""
        old_level = self._level
        self._validate_level(value)
        
        # Логическая проверка: нельзя понизить уровень
        if value < old_level:
            raise ValueError("Нельзя понизить уровень оружия!")
        
        self._level = value
        self._damage = self._calculate_damage()  # пересчет урона
        print(f"✨ Уровень повышен до {value}")
    
    @property
    def durability(self):
        """Прочность оружия"""
        return self._durability
    
    @durability.setter
    def durability(self, value):
        """Установка прочности с проверкой"""
        old_value = self._durability
        self._validate_durability(value)
        
        self._durability = value
        
        # Логические сообщения о состоянии
        if self._durability == 0 and old_value > 0:
            print(" ОРУЖИЕ СЛОМАНО! Требуется ремонт.")
        elif self._durability < 30 and self._durability > 0:
            print("Оружие в плохом состоянии")
        elif self._durability > old_value:
            print(" Оружие отремонтировано")
    
    @property
    def damage(self):
        """Урон оружия (вычисляется автоматически)"""
        return self._damage
    
    @property
    def is_broken(self):
        """Проверка, сломано ли оружие"""
        return self._durability <= 0
    
    @property
    def description(self):
        """Красивое описание оружия"""
        return f"⚔ {self._rarity} {self._weapon_type} '{self._name}' (ур.{self._level}, урон {self._damage})"
    
    def __str__(self):
        """Для пользователей - красивое описание"""
        return self.description
    
    def __repr__(self):
        """Для разработчиков - как создать объект"""
        return f"Weapon('{self._name}', '{self._weapon_type}', '{self._rarity}')"
    
    def __eq__(self, other):
        """Сравнение двух объектов"""
        if not isinstance(other, Weapon):
            return False
        return (self._name == other._name and 
                self._weapon_type == other._weapon_type and 
                self._rarity == other._rarity and
                self._level == other._level)
    
    def upgrade(self):
        """Улучшить оружие на 1 уровень"""
        if self.is_broken:
            raise ValueError("Нельзя улучшить сломанное оружие!")
        
        if self._level >= self.MAX_LEVEL:
            print(f"✨ Оружие уже имеет максимальный уровень ({self.MAX_LEVEL})!")
            return False
        
        self.level = self._level + 1
        return True
    
    def repair(self):
        """Починить оружие до 100%"""
        self.durability = self.MAX_DURABILITY
        return True
    
    def attack(self):
        """Атаковать оружием (уменьшает прочность)"""
        if self.is_broken:
            raise ValueError("Невозможно атаковать! Оружие сломано.")
        
        # Потеря прочности зависит от редкости
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
        return (f"Статус: {self._name} | "
                f"Тип: {self._weapon_type} | "
                f"Редкость: {self._rarity} | "
                f"Уровень: {self._level}/{self.MAX_LEVEL} | "
                f"Урон: {self._damage} | "
                f"Прочность: {self._durability}% | "
                f"Состояние: {status}")