# Чтение всего файла
#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#print(contents)


# Чтение файла построчно
#filename = 'pi_digits.txt'
#with open(filename) as file_object:
#    lines = file_object.readlines()
#for line in lines:
#    print(line.rstrip())
    

# Создание одной большой строки из файла
#filename = 'pi_digits.txt'
#with open(filename) as file_object:
#    lines = file_object.readlines()
#pi_string = ''
#for line in lines:
#   pi_string += line.rstrip()
#print(pi_string)
#print(len(pi_string))


#filename = 'learning.txt'
#with open(filename) as file_object:
    #contents = file_object.read()
#print(contents)


#filename = 'learning.txt'
#with open(filename) as file_object:
#    lines = file_object.readlines()
#for line in lines:
#    print(line.rstrip())

#filename = 'learning.txt'
#with open(filename) as file_object:
#    lines = file_object.readlines()
#string = ''
#for line in lines:
#    string += line.rstrip()
#print(string)
 
# Запись в файл
#file = 'programming.txt'
#with open(file, 'a') as file_object:
#    file_object.write("I also love finding meaning in large datasets.\n")
#    file_object.write("I love creating apps that can run in a browser.\n")
#print("Файл создан и записан успешно!")


#name = input("Введите ваше имя: ")
#filename = 'programming.txt'
#with open(filename, 'a') as file_object:
#    file_object.write(f'{name}')

    #while True:
#    file_name ='guest.txt'
#    name = input('Какое ваше имя:')
#    with open(file_name, 'a') as guest:
#        if name != 'quit':
#            guest.write(f'{name} \n')
#        else:
#            break

#while True:
#    fale_name = 'answer.txt'
#    answer = input('Почему вы любите программировать?')
#    with open(fale_name, 'a') as a:
#        a.write(f'{answer}\n')


#try:
#    print(5/0)
#except ZeroDivisionError:
#    print('Ты не можешь делить на ноль')


#print('give me two number and i devide them')
#print('enter q to quit')
#while True:
#    first_number = input('\n First number:')
#    if first_number == 'q':
#        break
#    second_number = input('\n Secomd number:')
#    if second_number == 'q':
#        break
#    try:
#        answer = int(first_number)/int(second_number)
#    except ZeroDivisionError:
#        print('you cant divide by 0')
#    except ValueError:
#        print('print number')
#   else:
#        print(answer)

#from docx import Document
#def count_word(file_name):
#    try:
#        if file_name.endswith('.txt'):
#            with open(file_name, 'r') as f:
#                contest = f.read()
#       elif file_name.endswith('.docx'):
#            doc = Document(file_name)
#            paragraphs = doc.paragraphs
#            texts = [p.text for p in paragraphs]
#            contest= ' '.join(texts)
#
#    except FileNotFoundError:
#        print(f'Sorry, the file {file_name} does not exist.')
#
#    else:
#            word = contest.split()
#            print(f'This file {file_name} has about word:',len(word))

#file_names = ['pi_digits.txt','programming.txt','wndf.txt','kurs.docx']
#for filenames in file_names:
#    count_word(filenames)


#def CatDog(file_name):
#    try:
#     with open(file_name,'r') as f:
#        content = f.read()
#
#    except FileNotFoundError:
#       pass
#    else:
#       print(f'{content}')

#doc = ['dog.txt','cat.txt','ds.txt']
#for file in doc:
#   CatDog(file)


#def found_word(file):
#    while True:
#        w = input('Введите слово:')
#        try:
#            with open(file, 'r',encoding='utf-8') as f:
#                content = f.read()
#                check = content.count(w)
#        except FileNotFoundError:
#            print('не найден файл')
#        else:
#            print(f'{check}')
#
#doc = ['kurs.txt']
#for file in doc:
#    found_word(file)

