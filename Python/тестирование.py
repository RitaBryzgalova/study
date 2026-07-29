def get_formatted_name(first,last, middle=''):
    '''строит отформатированное полное имя.'''
    if middle:
        full_name =f"{first} {last} {middle}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def country_cities(country, cities, population=''):
    '''Возвращает отфарматированное сообщение городах и странах'''
    if population:
        full = f'{country}, {cities}, {population}'
    else:
        full = f'{country}, {cities}'
    return full.title()