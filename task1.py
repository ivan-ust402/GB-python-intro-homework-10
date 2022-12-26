"""
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


class Road:
    """
    Класс для создания объектов дорог
    """
    single_asphalt_mass = 25
    height_road = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_mass_asphalt(self):
        """
        Метод расчета полной массы асфальта для требуемой длины и ширины
        дорожного полотна
        :return: строка результата
        """
        road_mass = round(self._width * self._length *
                          self.single_asphalt_mass * self.height_road / 1000)
        return f'Масса асфальта, для дороги\nдлиной - {self._length} ' \
               f'метров,\nшириной - {self._width} метров,\n' \
               f'высотой полотна - {self.height_road} сантиметров\n' \
               f'равна {road_mass} тонн'


print('--------- Класс Road ---------')
m54_first_part = Road(5000, -20)
print(m54_first_part.calc_mass_asphalt())

m54_first_part.length = 5000
m54_first_part.width = 20
print(m54_first_part.calc_mass_asphalt())
print('')

class Car:
    """
    Класс машин
    """
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
toyota_ist = Car(-55, 'красная', 'toyota ist', False)
print(toyota_ist.name)
print(toyota_ist.speed)
print(toyota_ist.color)
print(toyota_ist.is_police)
print(toyota_ist.to_go())
print(toyota_ist.stop())
print(toyota_ist.turn('лево'))
print(toyota_ist.turn('право'))
print(toyota_ist.show_speed())
print(toyota_ist.show_status())
