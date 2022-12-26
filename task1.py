"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


# Первый пример
class RoadAttrValidator:
    """Класс для валидации отрицательных значений"""
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if isinstance(value, int) and isinstance(value, float):
            raise ValueError(f'Значение {self.my_attr} должно иметь тип int'
                             f' или float')
        if value < 0:
            raise ValueError(f'Значение {self.my_attr} не может быть'
                             f' отрицательным!')
        instance.__dict__[self.my_attr] = value


class Road:
    """
    Класс для создания объектов дорог
    """
    single_asphalt_mass = 25
    height_road = 5

    length = RoadAttrValidator('length')
    width = RoadAttrValidator('width')

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_mass_asphalt(self):
        """
        Метод расчета полной массы асфальта для требуемой длины и ширины
        дорожного полотна
        :return: строка результата
        """
        road_mass = round(self.width * self.length *
                          self.single_asphalt_mass * self.height_road / 1000)
        return f'Масса асфальта, для дороги\nдлиной - {self.length} ' \
               f'метров,\nшириной - {self.width} метров,\n' \
               f'высотой полотна - {self.height_road} сантиметров\n' \
               f'равна {road_mass} тонн'


print('--------- Класс Road ---------')
m54_first_part = Road(5000, 20)
# m54_first_part = Road(-5000, 20)
# m54_first_part = Road(5000, -20)
# m54_first_part = Road("string", 20)
# m54_first_part = Road(5000, "string")
print(m54_first_part.calc_mass_asphalt())

m54_first_part.length = 5000
# m54_first_part.length = -5000
m54_first_part.width = 20
# m54_first_part.width = -20
print(m54_first_part.calc_mass_asphalt())
print('')


# Второй пример
class NumValueValidator:
    """Класс для валидации числовых значений"""
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if not isinstance(value, int) and not isinstance(value, float):
            raise ValueError(f'Значение {self.my_attr} должно иметь тип int'
                             f' или float!')
        if value < 0:
            raise ValueError(f'Значение {self.my_attr} должно быть'
                             f' положительным!')
        instance.__dict__[self.my_attr] = value


class StrValueValidator:
    """Класс для валидации строковых значений"""
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'Значение {self.my_attr} должно иметь тип str!')
        instance.__dict__[self.my_attr] = value


class BoolValueValidator:
    """Класс для валидации булевых значений"""
    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if not isinstance(value, bool):
            raise ValueError(f'Значение {self.my_attr} должно иметь тип bool!')
        instance.__dict__[self.my_attr] = value


class Car:
    """
    Класс машин
    """
    speed = NumValueValidator('speed')
    color = StrValueValidator('color')
    name = StrValueValidator('name')
    is_police = BoolValueValidator('is_police')

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def to_go(self):
        """
        Метод отображения движения машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} поехала'

    def stop(self):
        """
        Метод отображения остановки машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        """
        Метод отображения поворота машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} повернула на{direction}'

    def show_speed(self):
        """
        Метод отображения поворота машины
        :return: строка состояния машины
        """
        return f'Машина {self.name} едет со скоростью {self.speed} км/ч'

    def show_status(self):
        """Метод показывает, работает ли машина в полиции"""
        if self.is_police:
            return f'Машина {self.name} полицейская'
        return f'Машина {self.name} не полицейская'


print('--------- Класс Car ---------')
toyota_ist = Car(55, 'красная', 'toyota ist', False)
# toyota_ist = Car(55.5, 'красная', 'toyota ist', False)
# toyota_ist = Car(-55, 'красная', 'toyota ist', False)
# toyota_ist = Car('string', 'красная', 'toyota ist', False)
# toyota_ist = Car(55, 50, 'toyota ist', False)
# toyota_ist = Car(55, 'красная', True, False)
# toyota_ist = Car(55, 'красная', 'toyota ist', 123)
print(toyota_ist.name)
print(toyota_ist.speed)
print(toyota_ist.color)
print(toyota_ist.is_police)
