#from классы import Privrleges as P
#from test2 import Admin as A

#priveleges = P('Rita','Bryzgalova','26.03.2008','555777999',0,['Разрешенно добавлять сообщения','Разрешенно банить пользователей','Разрешенно удалять пользователей'])
#priveleges.show_priveleges()

#admin = A()
#admin.show_admin()

from тестирование import get_formatted_name 

#print("Enter 'q' at any time to quit. ")
#while True:
#    first = input("\n Please give me a firs name:")
#    if first == 'q':
#        break
#    last = input('\n Please give me a last name:')
#    if last == 'q':
#        break
#    formatted_name = get_formatted_name(first,last)
#    print(f'\n Neatly formatted name: {formatted_name}')


import unittest
from тестирование import get_formatted_name
class NamesTestCase(unittest.TestCase):
    '''Тест для файла'тестирования'. '''
    def test_first_last_name(self):
        '''Имена вида Rita Bryzgalova'''
        formatted_name = get_formatted_name('rita','bryzgalova')
        self.assertEqual(formatted_name, 'Rita Bryzgalova')

    def test_first_Last_middle_name(self):
        '''роботают ли такие имена как 'Rita Bryzgalova Dmitrievna'.'''
        formatted_name = get_formatted_name('Rita','Dmitrievna','Bryzgalova')
        self.assertEqual(formatted_name, 'Rita Dmitrievna Bryzgalova')

#if __name__ == '__main__':
#    unittest.main()

from тестирование import country_cities
class TestCountryCity (unittest.TestCase):
    '''тест country_cities'''

    def test_country_cities(self):
        '''формат страна город'''
        full_n = country_cities('russia','moscou',)
        self.assertEqual(full_n, 'Russia, Moscou')

    def test_country_cities_population(self):
        '''тест формата страна, город, население'''
        full_n = country_cities('Nizny Novgorod', 'russia', '1 200 00')
        self.assertEqual(full_n,'Nizny Novgorod, Russia, 1 200 00')

if __name__ == '__main__':
    unittest.main()
