#aliens_0 = {'color': 'green'}
#print(aliens_0["color"])

#aliens_0 ['color'] = 'yelow'
#print(aliens_0['color'])


#aliens_0 = {'x_position':0, 'y_position':25,'speed':'fast'}
#if aliens_0['speed'] == 'slow':
#    x_increment = 1
#elif aliens_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    x_increment = 3
#aliens_0 ['x_position'] = aliens_0['x_position'] + x_increment

#print(aliens_0['x_position'])



#удаление из словаря 
#aliens_0 = {'color': 'green', 'points':5}
#print(aliens_0)

#del aliens_0['points']
#print(aliens_0)


#famous_person = {'name':'Vladimir', 'city':'Moskow', 'work':'president'}
#print(famous_person['name'])
#print(famous_person['city'])
#print(famous_person['work'])


#favorite_nambers = {
#    'rita':[5432,46,47,4,782,865645,453,],
#      'roma':[34,7,978,34,9,1231,],
#        'dima':[2446,654,345,8,54,45,346],
#          'tanya':[124,6,9087,546,2432],
#            'dasha':[43,241,234,565,6,35]}
#print(favorite_nambers)


#words ={
#    'print':'print \n Печатает информацию',
#    '.append':'append \n Метод добавляет значение в список',
#    'if else':'if else \n условие если то',
#    'for':'for \n цикл',
#    'summ':'summ \n Складывает значения'
#    }
#for key, value in  words.items():
#   print(f'\n Key:{key}')
#   print(f'Value:{value}')


#user0 ={
#  'username': 'efermy',
#   'first': 'enrico',
#    'last':'fermi'
#}
#for key, value in user0.items():
# print(f'\n Key:{key}')
#  print(f'Value:{value}')

#faworite_languages={
#    'jen': 'python',
#    'sarah':'c',
#    'edvard': 'ruby',
#    'phil':'pyphon',
#}
#friends = ['sarah', 'phil']
#for name in faworite_languages.keys():
#    print(name.title())

#    if name in friends:
#        language = faworite_languages[name].title()
#       print(f'\t{name.title()}, I se yu like {language}!')


#faworite_languages={
#   'jen': 'python',
#   'sarah':'c',
#   'edvard': 'ruby',
#   'phil':'pyphon',
#}
#print('the following have been mentioned')
#for language in set(faworite_languages.values()):
#    print(language.title())


#words ={
#    'print':'print \n Печатает информацию',
#    '.append':'append \n Метод добавляет значение в список',
#    'if else':'if else \n условие если то',
#    'for':'for \n цикл',
#    'summ':'summ \n Складывает значения'
#    }

#for key, values in words.items():
#    print(f'\nkey {key}')
#    print(f'values {values}')
    

#river = {
#   'Volga;':'Nizny Novgorod',
#    'Neva':'Saint Peterburg',
#    'Moskva':'Moscow',
#    'Lena':'Yakutsk',
#   'Amur':'Khabarovsk',
#    'Ob':'Novosibirsk',
#    'Amazonka':'Manaus'
#}
#for key,value in river.items():
#    print(f'In the city {value} runs {key}')

#people_to_poole = ['jen','edvard','sarah','phil','rita','dima','roma']
#faworite_languages={
#   'jen': 'python',
#   'sarah':'c',
#   'edvard': 'ruby',
#   'phil':'pyphon',
#}
#for person in people_to_poole:
#    if person in faworite_languages:
#        print(f'{person.title()} Thank you ')
#    else:
#        print(f'{person} Lets go')


#aliens = []
#for alien_nambers in range(30):
#    new_alien= {'color':'green', 'points':5, 'speed':'slow'}
#    aliens.append(new_alien)
#for alien in aliens[0:10]:
#    if alien ['color']:
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['point'] = '10'
#    elif alien['color'] == 'yellow':
#        alien['color'] = 'red'
#        alien['speed'] = 'fast'
#        alien['points'] = 15
#print(aliens)


#pizza = {
#    'crust':'thick',
#    'toppins':['moshroom','exstra cheese']
#}
#print(f'You order {pizza['crust']} - crust pizza')

#for toppings in pizza['toppins']:
#    print('\t' + toppings)


#user = {
#    'eainstane':{
#        "first":'albert',
#        'last':'einstein',
#        'location':'pinceton'
#    },

#    'mcure' : {
#        'first':'marie',
#        'last':'curie',
#        'location':'paris'
#    }
#}

#for user_name, user_info in user.items():
#    print(f'Username {user_name}')
#    ful_name = f'{user_info['first']} {user_info['last']}'
#    location = f'{user_info['location']}'
#    print(f'\nfull name {ful_name}')
#    print(f' location {location}')


#famous_person = {
#    'VPutin' : {
#    'name':'Vladimir',
#    'city':'Moskow', 
#    'work':'president',  
#    },

#    'LGAGA' : {
#        'name':'Stephany Joan Angelina Jermanota',
#        'city':'Los Angeles',
#        'work':'singer'
#    },

#    'CMN':{
#       'name':'Rusla Tushentsov',
#        'city':'Moskow',
#        'work':'singer'
#   },

#  'Ovi' :{
#       'name':'Alexander Ovechkin',
#       'city':'Washington',
#      'work':'Hokey player'
#   }
#}

#for user_name ,user_info in famous_person.items():
#    print(f'\nUser_name: { user_name}')
#    print(f'Full name: {user_info['name']}')
#    print(f'City: {user_info['city']}')
#    print(f'Work: {user_info['work']}')
    
#cat_styopa = {
#        'nickname':'styopa',
#        'master':'Rita',
#        'color':'grey'
#    }
#cat_rizik={
#    'nickname':'rizik',
#    'master':'Dasha',
#    'color':'orange'
#}
#cat_muska = {
#    'nickname':'muska',
#    'master':'Valua',
#    'color': 'grey'
#    }
#cat_manka = {
#    'nickname':'manka',
#    'master':'Valua',
#    'color':'grey'
#}
#pets = [cat_styopa,cat_rizik,cat_muska]
#for pets_info in pets:
#    print(pets_info) 



#faforite_place = {
#    'rita':{
#        'name': 'rita',
#        'place': ['Los Angeles','Moscow','Sochi'],
 #   },
#      'name' : 'roma',
#      'place' :['magazine','Sea',''] 
#  },
#  'dima' : {
#     'name': 'dima',
#     'place':['village','dalnee constantinovo','Home'] 
#  },
#  'tanya' :{
#      'name':'tanya',
#      'place':['gym','home']
 # }
#}

#for info_name, info_place in faforite_place.items():
#    print(f'name {info_name}')
#    print(f'love place {info_place ['place']}')


cityes ={
    'Shanghai':{
    'country':'China',
    'population':'20 000 000',
    'facts':'Its port is one of the bisiest in the worl'
    },
    'Mosow':{
      'country':'Russia',
      'population':'12 000 000',
      'facts':'Its copital of Russia'
    },
    'Sanit piterspurg' : {
        'country': 'Russia',
        'population':'8 000 000',
        'facts': 'Biuld in 1702 ears'
    }
}
for name, name_info in cityes.items():
    print(f'\nname {name}')
    print(f'country {name_info['country']}')
    print(f'population {name_info['population']}')
    print(f'Facts {name_info['facts']}')