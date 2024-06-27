calls = 0
def count_calls():
    global calls
    calls = calls + 1
count_calls()
def string_info(string):
    string1 = {len(string), string.upper(), string.lower()}
    print(string1)
string_info('Copibara')
count_calls()
def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = str(list_to_search)
    list_to_search = list_to_search.lower()
    print(string in list_to_search)
is_contains('Urban', ['urBAN', 'BaNaN', 'ban'])  #Urban ~ urBAN
count_calls()
def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = str(list_to_search)
    list_to_search = list_to_search.lower()
    print(string in list_to_search)
is_contains('Armagedon', ['Mags', 'Don', 'uragan']) #No matches
count_calls()
print(calls)