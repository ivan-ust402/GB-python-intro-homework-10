"""
Создать метакласс для паттерна Синглтон (см. конец вебинара)
"""


class MetaSingleton(type):
    """Метакласс синглтон"""
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MySingletonClass(metaclass=MetaSingleton):
    """Класс синглтон"""
    def show(self):
        """Демонстрация инфо о классе MySingletonClass"""


class MyRegularClass:
    """Обычный класс"""
    def show(self):
        """Демонстрация инфо о классе MyRegularClass"""


x = MySingletonClass()
y = MySingletonClass()
# print(x._instance)
# print(y._instance)
print(x == y)

z = MyRegularClass()
k = MyRegularClass()

print(z == k)
