from классы import Car

class Battery:
    """Модель аккумулятора автомобиля"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"Эта машина имеет {self.battery_size} кВт·ч заряда.")
    
    def get_range(self):
        """Вывод приблизительного запаса хода"""
        if self.battery_size == 75:
            range_km = 260
        elif self.battery_size == 100:
            range_km = 315
        else:
            range_km = "неизвестно" # На случай другого размера батареи
            
        print(f"На этой зарядке машина может проехать около {range_km} км.")

    def upgrade_battery(self):
        self.battery_size = 100

class ElectricCar(Car):
    """Аспекты машины, специфические для электромобилей"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты родителя и специфические для электрокара"""
        super().__init__(make, model, year)
        self.battery = Battery() # Создаем экземпляр Battery как атрибут

    def fill_gas_tank(self):
        """У электромобиля нет бензобака (переопределение метода)"""
        print("У электромобиля нет бензобака!")