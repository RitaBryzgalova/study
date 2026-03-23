from классы import Privrleges as P
from test2 import Admin as A

priveleges = P('Rita','Bryzgalova','26.03.2008','555777999',0,['Разрешенно добавлять сообщения','Разрешенно банить пользователей','Разрешенно удалять пользователей'])
priveleges.show_priveleges()

admin = A()
admin.show_admin()