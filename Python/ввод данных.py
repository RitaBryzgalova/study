#print('what car you want')
#car = input()
#print(f'I wont this {car}')

#print("How many people book table")
#namer = int(input())
#if namer > 8 :
#    print('To mach people, we should wait')
#else:
#    print('Good yours book ready')

#print('Print number')
#number= int(input())
#if number% 10 == 0:
#    print("this number multiple")
#else:
#    print('this number not multiple')

#current_number = 1
#while current_number <=5:
#    current_number += 1
#    print(current_number)


#promt = '\n Tell me sonething and i will repeat it back to you:' 
#promt += '\n Enter "qiut" to end the program'
#message = ''
#while message != 'quit':
#    message=input(promt)
#   print(message)


#promt = '\n Tell me sonething and i will repeat it back to you: ' 
#promt += '\n Enter "qiut" to end the program'
#message = ''
#active = True
#while active:
#    message= input(quit)

#    if message == "quit":
#        active = False
#    else:
#        print(message)


#promt = '\n Please enter the name of a city you have visited: ' 
#promt += '\n (Enter "qiut" when you a finished)'

#while True:
#    city = input(promt)
#   if city ==  "quit":
#       break
#    else:
#        print(f'I love to go {city.title()}! ')


#current_number = 0
#while current_number <10:
#    current_number += 1
#    if current_number%2 == 0:
#        continue
#    print(current_number)


#print("how toppings you have in pizza")
#toppings=[]
#in_pizza = input()
#while in_pizza != 'quit':
#     toppings.append(in_pizza)
#     print('Anything else')
#     print(f'In yours pizza this{toppings} toppings')
#     in_pizza = input()
        


#print("how toppings you have in pizza")
#toppings=[]
#in_pizza = input()
#active = True
#while active:
#    if in_pizza == "quit":
#        active = False
#    else:
#        toppings.append(in_pizza)
#        print(f'In yours pizza this {toppings} toppings')
#        print('About else')
#        in_pizza = input()


#unconfirmed_users = ['alice', 'brian','candace']
#confirmend_users = []
#while unconfirmed_users:
#    current_users = unconfirmed_users.pop()
#    print(f'verifiring user: {current_users.title()}')
 #   confirmend_users.append(current_users)
#print("\n the folloving users have been confirmend:")
#for confirmend_users in confirmend_users:
#    print(confirmend_users.title())


#pets = ['dog','cat','goldfish','rabbit','cat']
#print(pets)
#while 'cat' in pets:
#    pets.remove('cat')
#print(pets)
    

#responses = {}
#polling_active = True
#while polling_active:
#    name = input('\n What is your name ?')
#    response =input('which montain wousl you like to climb someday?')
#
#    responses[name] = response
#
#    repeat = input('would you like let another person respound (yes/no)')
#    if repeat == "no":
#        polling_active = False
#print("\n----Poll Results----")
#for name,response in responses.items():
#    print(f'{name} would like to climb {response}')

#sandvich_orders =['chikenburger','bigmak','big speshial','bighit','grand','gamburger']
#finished_sendvich = []
#for sandvich in sandvich_orders:
#    finished_sendvich.append(sandvich)
#    print(f'i made your {finished_sendvich}')
#print(finished_sendvich)


#sandvich_orders =['chikenburger','bigmak','pastrami','big speshial','bighit','pastrami','grand','gamburger']
#finished_sendvich = []
#while 'pastrami' in sandvich_orders:
#        sandvich_orders.remove("pastrami")
#active =True
#while active:
#    finished_sendvich.append(sandvich_orders)
#    print(f'i made your {finished_sendvich}')
#    active = False
#print(finished_sendvich)   


place = input('In how spend holidays')
print(place)