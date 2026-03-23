#bicycle = ['горный','городской','трековый','шоссейный']
#mesage = f'мой первый велосипед это {bicycle[0].title()}' 
#print(mesage)

#Friend = ['вова','рита','любава','вика',]
#message = f'мой друг это {Friend[3].title()}'
#print(message)


#motorcycles = ['honda', 'yamaha','suzuki']
#print(motorcycles)
#motorcycles.append('ducati')
#print(motorcycles)

#motorcycles = ['honda', 'yamaha','suzuki']
#motorcycles.insert(-2, "dygati")
#del motorcycles[2]
#print(motorcycles)


#motorcycles = ['honda', 'yamaha','suzuki']
#print(motorcycles)
#poppend_motorcycle = motorcycles.pop()
#print(motorcycles)
#print(poppend_motorcycle)

#motorcycles = ['honda', 'yamaha','suzuki']
#last = motorcycles.pop(0)
#message = f'первый проданный мотоцикл был {last.title()}'
#print (message)


#motorcycles = ['honda', 'yamaha','suzuki','dugati']
#print(motorcycles)
#motorcycles.remove('dugati')
#print(motorcycles)


#guestes = ["арсен маркарян", "руслан смн " ,"пошлая молли", "дмитрий уткин", "екатерина мезулина", "шаман" ,"гитлер" ]
#message12 =  f'{guestes[2]} вы приглашены на концерт'
#guestes.pop()
#a = guestes.pop()
#del guestes[3]
#message = f'к сожалениюv {a} не сможет придти'
#print(message12)
#print(message)
#print(guestes)


#cars = ['bmw','aydi','tayota','subaru']
#print('оригинал')
#print(cars)

#print('2 вариант')
#print(sorted(cars))

#print('оригинал после')
#print(cars)


#cars = ['bmw','aydi','tayota','subaru']
#print(cars)
#cars.reverse()
#print(cars)

#cars = ['bmw','aydi','tayota','subaru']
#a = len(cars)
#print(a)


#country = ['Russa','USA','Germany','Britan','Polland','Belarus']
#print(country)
#sorted(country)
#print(reversed(country))


#magicians = ['alice','david','corolina']
#for magician in magicians:
#    print(f"{magician.title()}, очеь хороший маг")
#print("спасибо что пришли")


#pizza = ['пеперони','4 сыра','маргарита','гавайская']
#for pizza in pizza:
#    print(f'я люблю',{pizza.title()})
#print('я правда люблю пиццу')



def make_pizza (size,*toppings):
    print(f'/nMakig {size}pizza with follow toppiings:')
    for topping in toppings:
        print(f'{topping}')
make_pizza(16,'peperrooni')
make_pizza(12,'moshroms','extra chees','green peppers')
make_pizza(16,'peperrooni')
