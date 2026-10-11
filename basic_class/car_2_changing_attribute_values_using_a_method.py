class Car:
    def __init__(self, name, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Добавили атрибут пробега авто. Исх. знач. всегда равно 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание"""
        long_name = f"{self.year} {self.name} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в км"""
        print(f"This car has {self.odometer_reading} km on it.")


# Создаем экземпляр класса Car и присваиваем его переменной my_new_car
my_new_car = Car("audi", "a4", "2024")
print(my_new_car.get_descriptive_name()) # Вызываем метод get_descriptive_name() и видим с какой машиной раб. прог.
my_new_car.read_odometer()