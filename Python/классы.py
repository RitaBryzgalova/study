#class Dog():
#   'Простая модель собаки'
#   def __init__(self,name,age):
#        'Инициализирует атрибуты name и age'
#        self.name = name
#        self.age = age
#
#    def sit(self):
#       'Собака садится по команде'
#        print(f'{self.name} is now sitting.')
#
#   def roll_ower(self):
#        'Собака перекатывыется по команде'
#        print(f'{self.name} roller over')

#my_dog = Dog('willie',6)
#your_dog = Dog('licy',3)

#print(f'My dogs my name is {my_dog.name}')
#print(f'My dog is {my_dog.age} years old')
#my_dog.sit()

#print(f'\nMy dogs my name is {your_dog.name}')
#print(f'My dog is {your_dog.age} years old')
#your_dog.sit()


#class restarant():
#    def __init__(self,restsraunt_name,cuisine_type):
 #       self.restaraunt = restsraunt_name
 #       self.cuisine = cuisine_type
   
 #   def describe_restarant(self):
#        print(f'\n{self.restaraunt},Уютное и милое место для ваших хороших воспоминаний: {self.cuisine}')
    
#    def open_restarant(self):
#       print("Рестаран открыт")


#class IseCreamStand(restarant):
 #   "Киоск с мороженным"
 #   def __init__(self, restsraunt_name, cuisine_type,flavors):
 #       super().__init__(restsraunt_name, cuisine_type)
#        self.flavors = flavors 
#
 #   def ShowIceCream(self):
 #       'Сорта мороженного'
 #       print(f'\n А киоске {self.restaraunt} есть такое сорта')
 #       for flavors in self.flavors:
 #           print(f'-{flavors}')

#iceCream= IseCreamStand('Снежинка', 'Десерты', ['Ванильное', 'Пломбир', 'Шоколадное'])
#iceCream.describe_restarant()
#iceCream.ShowIceCream()
#my_rest = restarant('Cloud Mone','Французская кухня')
#print(f'\nЭто {my_rest.restaraunt} c {my_rest.cuisine}')

#my_rest.describe_restarant()
#my_rest.open_restarant()

#my_rest1 = restarant('Шаурма на средном','Восточная кухня')
#my_rest1.describe_restarant()

#my_rest2 = restarant('Вкусно и точка','fast food')
#my_rest2.describe_restarant()


class user():
    def __init__(self,firsr_name,last_name,data_registration,password,login_attempts):
       self.fisrt = firsr_name
       self.last = last_name
       self.reg = data_registration
       self.password = password
       self.Login_attempts = 0 

    def describle_user(self):
            'Описывает пользователя'
            print(f'\nFirst name: {self.fisrt}')
            print(f'Last name: {self.last}')
            print(f'Data registration:{self.reg}')
            print(f'Password: {self.password}')
    
    def greet_user(self):            
         "Выводит приветствие"
         print(f'Hello {self.fisrt} {self.last}!')

    def increment_lOgin_attempts(self):
         'Попытки залогинится'
         self.Login_attempts += 1
         print(self.Login_attempts)  
            
    def reset_login_attemts(self):
         'Сброс попыток залогинится'
         self.Login_attempts = 0
         print({self.Login_attempts}, "Счетчик сброшен")

class Admin(user):
    'Адмииииин крут'
    def __init__(self, firsr_name, last_name, data_registration, password, login_attempts,privileges):
        super().__init__(firsr_name, last_name, data_registration, password, login_attempts)
        self.privileges= privileges  
    
    def show_admin(self):
        'показывает админа'
        print('Это админ бро')

class Privrleges(user):
     
    def __init__(self, firsr_name, last_name, data_registration, password, login_attempts,privileges):
            super().__init__(firsr_name, last_name, data_registration, password, login_attempts)
            self.privileges = privileges
    
    def show_priveleges(self):
        'Показывает привелегии'
        print(f'\nУ админа есть такие привилегии:')
        for priveleges in self.privileges:
            print(f'-{priveleges}')


#admin =Privrleges('Rita','Bryzgalova','26.03.2008','555777999',0,['Разрешенно добавлять сообщения','Разрешенно банить пользователей','Разрешенно удалять пользователей'])
#admin.describle_user()
#admin.show_priveleges()
#user1 = user('Rita','Bryzgalova','26.03.2008','555777999',0)
#user1.describle_user()
#user1.greet_user()
#user1.increment_lOgin_attempts()
#user1.increment_lOgin_attempts()
#user1.reset_login_attemts()



#user2 = user('Vova','Chernyavsky','22.12.2007','213423',0)
#user2.describle_user()
#user2.greet_user()
#
#user3 = user('Dasha','Sergeevna','16.04.2012','287657')
#user3.describle_user()
#user3.greet_user()


class Car:  
    """Простая модель автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.model = model
        self.make = make
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
   
    def read_odometer(self):
        """Выводит пробег машины в километрах"""
        print(f"Эта машина проехала {self.odometer_reading} километров.")
       
    def update_odometer(self, mileage):
        """Обновляет данные одометра. Отклоняет скрутку назад."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Вы не можете скрутить одометр назад!")
           
    def increment_odometer(self, miles):
        """Увеличивает данные одометра"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Нельзя прибавить отрицательный пробег!")
   
    def fill_gas_tank(self):
        """Заправляет машину (бензиновую)"""
        print("Бензобак полон!")

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


#my_tesla = Battery()
#my_tesla.get_range()
#my_tesla.upgrade_battery()
#my_tesla.get_range()

#my_car = Car('субару','аутбек',2015)
#my_car.fill_gas_tank()
#print(my_car.get_description_name())
#
#my_car.Update_odometr(23500)
#my_car.odometr()
#
#my_car.increment_odometr(100)
#my_car.odometr()
#
#my_car.Update_odometr(34) -- Изменения атрибута с использованием метода
#my_car.odometr()
#
#my_car.odometr_reding = 23 -- Прямое изминение атрибута
#my_car.odometr()


class Restarant():
    def __init__(self,restsraunt_name,cuisine_type):
       self.restaraunt = restsraunt_name
       self.cuisine = cuisine_type
       self.number = 0 
   
    def describe_restarant(self):
       'Описывает рестаран'
       print(f'\n{self.restaraunt},Уютное и милое место для ваших хороших воспоминаний: {self.cuisine}')

    def open_restarant(self):
       'Открытие ресторана'
    print("Рестаран открыт")
    
    def set_number_served(self,number):
          'Колтчество людей в обслуживании'
          self.number = number
          print(f'Количество обслуживаемых посетителей: {number}')
    
    def update_number(self,update):
        'Обновляет количетво людей в обслуживании'
        self.number = update
        print(f'Людей в обслуживании: {update}')
   
    def incremed_number_served(self, guest):
        'Подсчитывает общее количество людей за день'
        if guest > 0:
            self.number += guest
        else:
            print('Нельзя прибавить отрицательное значение людей')

#rest = Restarant('clod mone','Французская кухня',)
#rest.set_number_served(34)
#rest.set_number_served(132)
#rest.incremed_number_served(-21)
#print(f'Обслуженно к концу дня {rest.number}')


class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        random = randint(1, self.sides)
        print(random)
#
#model = Die(6)
#for i in range(10):
#    model.roll_die()

#d20 = Die(sides=20)
#for i in range(10):
#    d20.roll_die()

#rand = [2,3,67,42,76,0,73,20,567,324,795,'s','f','a','l','u']
#from random import choice
#tiket = []
#for i in range(4):
#    tiket.append(choice(rand))
#print(tiket)


from random import choice

tiket = [2,3,67,42,76,0,73,20,567,324,795,'s','f','a','l','u']
my_tiket = ['s',67,'f',20]
check = 0
current_ticket = []
while current_ticket != my_tiket:
    current_ticket = []
    check += 1 
    for i in range(4):
        random_element = choice(tiket)
        current_ticket.append(random_element)
   
p = f'Ура! Выигрышный билет: {current_ticket}. Попыток задействовано: {check}'
print(p)

