calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(_string: str):
    count_calls()
    tuple_of_string = (len(_string), _string.upper(), _string.lower())
    return tuple_of_string


def is_contains(string: str, list_to_search: list):
    count_calls()
    new_list_to_search = []
    for i in list_to_search:
        new_list_to_search.append(i.upper())
    return string.upper() in new_list_to_search


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
print(string_info('november'))
print(string_info('Кукарача'))
print(is_contains('Зелен', ['зелен', 'ГрАд', 'желудок']))
print(is_contains('Чижик', ['пыжик', 'где', 'ты', 'был']))
print(calls)
