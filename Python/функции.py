#def greet_users(username):
#    '''выводит приветствие'''def
#    print(f'Hello {username.title()}')
#greet_users("rita")

#def display_message(function):
#    print(f'I learning python {function}')
#display_message("def")


#def favirite_book(title):
#    title = input('Hoe your favorite book')
#    print(f'my favoritebook is {title}')
#favirite_book('')


#def discrible_pet(pet_name,animal_type='cat'):
#    print(f'\nI have a {animal_type}')
#    print(f"My {animal_type}'s name is {pet_name.title()} ")
#discrible_pet(pet_name='Stepan')

#def make_shirt(size,text= 'loh'):
#    print(f"size {size} T'shirt")
#    print(f"text {text.title()} T'shirt")
#make_shirt(text ='I love Python',size="l")


#def descrobe_city(city,country='Russia'):
#    print(f'{city} in {country}')
#descrobe_city(city='Novosybirsk'


#def get_formatted_name(first_name,last_name,middle_name =''):
#    if middle_name:
#        full_name= f"{first_name} {middle_name} {last_name}"
#    else:
#        full_name= f'{first_name} {last_name}'
#    return full_name.title()
#musican = get_formatted_name('jimi','hendrix',)
#print(musican)
#musican = get_formatted_name('joh','hooker','lee')
#print(musican)
#name = get_formatted_name('rita', 'dmitrievna','bryzgalova')
#print(name)

#def build_person(first_name, last_name,age =''):
#	person = {'firsts':first_name, 'last':last_name}
#	if age:
#		person ['age'] = age
#	return person
#musican = build_person('jimmix', 'hendrix','12')
#print(musican)


#def get_formatted_name(first_name,last_name,middle_name =''):
#    full_name= f"{first_name} {middle_name} {last_name}"
#    return full_name.title()
#while True:
#    print("\nPlease tell me your name:")
#    print ('Enter "q" at any time to quit')
#    f_name = input('first name:')
 #   if f_name =="q":
#        break
#		
#    l_name = input('last name:')
#   if l_name == "q":
#        break
#    formatted_name = get_formatted_name(f_name,l_name)
#    print(f'\nhello, {formatted_name}!')
    

#def citu_coutry(city,country):
#    full_name = f'{city},{country}'
#    return full_name
#full_name = citu_coutry("Moskow","Russia")
#print(full_name)
#full_name = citu_coutry('Washington', 'USA')
#print(full_name)
#full_name = citu_coutry('Barselona', 'Ispania')
#print(full_name)


#def make_album (executor,name_album,many_song=''):
#    info ={'executors':executor,'name_album':name_album,}
#    if many_song:
#        info ['many_songs'] = many_song
#    return info
#name = make_album('ladu gaga','the fame','12')
#print(name)


#def make_album (executor,name_album,many_song=''):
#     info ={'executors':executor,'name_album':name_album,}
#     if many_song:
#          info ['manu_song'] = many_song
#     return info
#while True:
#    print('Executors:')
#    exe = input()
#    if exe == "q":
#         break
#    print("Name album:")
#    name = input()
#    if name == "q":
#         break
#    print('How many songs in thi album:')
#    many = input()
#    if many == 'q':
#         break    
#    album = make_album(exe,name,many)    
#    print(album)


#def greet_users(names):
#    for name in names:
#        msg = f'hello, {name.title()}!'
#        print(msg)
#usernames =  ['hannah','ty','margot']
#greet_users(usernames)


#def print_models(unprinted_designs,completed_models):
 #   while unprinted_designs:
 #       current_design = unprinted_designs.pop()
#        print(f'printing model:{current_design}')
#        completed_models.append(current_design)
#
#def show_completed_models(completed_models):
#    print('\n the following models havebeen printed:')
#    for model in completed_models:
 #       print(model)
#unprinted_design = ['phone case','robot pedant','dodecahedron']
#completed_models = []
#print_models(unprinted_design, completed_models)
#show_completed_models(completed_models)
#
# unprinted_design = ['dsojfs','asdfdaf','sdfsd','sdfsdfs']
#completed_models=[]
#print_models(unprinted_design,completed_models)
#show_completed_models(completed_models)

#def show_message(message):
#    for messag in message:
#        text = f'{messag}'
#        print(text)
#mes = ['ok','hello']
#show_message(messgse)


#def sent_message(message,sent_message):
#    while message:
#        this_message = message.pop(0)
#        print(this_message)
 #       sent_message.append(this_message)
#
#messager = ['sdf','helllo']
#sent_messager = []

#sent_message(messager,sent_messager)

#print(messager)
#print(sent_messager)


#def make_pizza (size,*toppings):
#    print(f'/nMakig {size}pizza with follow toppiings:')
#    for topping in toppings:
#        print(f'{topping}')
#make_pizza(16,'peperrooni')
#make_pizza(12,'moshroms','extra chees','green peppers')


#def build_profile(first,last,**user_info):
#    user_info['first_name'] = first
#    user_info['last_name'] = last
#    return user_info
#user_profile = build_profile('albert','enstein', location= 'princeton',field='physics')
#print (user_profile)


#def sendeich(*components):
#    for comp in components:
#        print(f"your sandwich {comp} ready")
#
#sendeich('potatoo')
#sendeich('meat')


#def prifile(first_name,last_name,**late):
#    late['first'] = first_name
#    late['last'] = last_name
#    return late
#prof =prifile('rita','bryzgalova', college='cool',age=17,love_food= 'shayrma')
#print(prof)


#def car_info(*name,**car):
#    car['name']=name
#    return car  
#carr =car_info('subaru','outback',color='black',tow_package='True')
# print(carr)


#def find_unique_words():
#    print('Введите слова')
#    text = input()
#    word_list= text.lower().split()
#    enique_words = []
#    for word in word_list:
#        clear_word = word.strip('.!,')
#        if word_list.count(word) == 1:
#            enique_words.append(clear_word)
#    return clear_word    
#
#print(find_unique_words())


#def code_name(fist_name,last_name):
#    print('Напишите имя и Фамилию')
#    code_last_name =last_name[::-1]
#    code_first_name = fist_name[0]
#    full_name = code_first_name +"_"+code_last_name
#    print(full_name.upper())
#
#code_name('Катя','Королева')


#def calculate_price(price,discount):
#    print('Ваша Цена')
#    if discount > 100 or discount <0:
#        return('ошибка')
#    final_price = price - (price * discount / 100)
#    print(final_price)
#    return final_price
#
#calculate_price(1000,15)
   

def print_check(items,discount):
    if discount < 0 or discount > 100:
        print('Ошибка')
        return
    print('Сумма оплаты')
    summ_items= sum(items)
    finel_discount = summ_items -(summ_items*discount/100)
    print(finel_discount)
    return finel_discount

items = [43,423,56,345,2133]
print_check(items,55)


#def get_total_bill(discount,**cart):
#    if discount > 100 or discount < 0:
#        return'Ошибка'
##    name_card=[]
#   
# for name in cart.items():
#       name_card.append(name)
#    
#   full_price = summ_cart - (summ_cart*discount/100)
#   print('Вот ваша продуктовая корзина')
#   print(f'{name_card}')
#   print('К оплате')#  print(f'{full_price}')
#  return full_price
#result = get_total_bill(10, milk=80, bread=50, candy=120)


#def get_total_bill(discount, **cart):
#    if discount > 100 or discount < 0:
#        return 'Ошибка: неверная скидка'
#    
#    print('--- Ваш чек ---')
#    # Распаковываем словарь на Ключ (товар) и Значение (цена)
#    for product, price in cart.items():
#        print(f"🔹 {product}: {price} руб.")
#    
#    print('----------------')
#    
#    summ_cart = sum(cart.values())
#    full_price = summ_cart - (summ_cart * discount / 100)
#    
#    print(f"Итого со скидкой {discount}%: {full_price} руб.")
#    return full_price

#cart={}
#while True:
#    print('Напиши название товара')
#    name = input()
#    if name == 'q': 
#        break
#    print('Напиши цену')
#    price = int(input())
#    
#    cart[name] =price
#
#get_total_bill(10,**cart)

security_list = {"Ivan": 25, "Oleg": 16}

def check_guest(name,guest_list):
    if name not in guest_list:
        print('Отказано в доступе: вас нет в списках')
        return
    age = guest_list[name]
    if age < 18:
        return(print('Отказанно в доступе:слишком молод'))
    else:
        return(print('Добро пожаловать'))

while True:
    print('Введите имя, если это новый гость напишите admin')
    name =input()
    if name == 'security_list':
        print(security_list)  
        continue
    if name == 'Выход':     
        break
    
    if name == 'admin':
        print('Введите новое имя что бы добавить гостя в список')
        new_name =input()
        print('Введите возраст')
        new_age = int(input())
        
        security_list[new_name] = new_age
        print(f'Новый гость {new_name} добавлен в базу')
        continue
    
    check_guest(name, security_list) 
     

