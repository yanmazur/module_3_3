def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(5, 'pyramid', False)
print_params(765, 'try')
print_params(b = 'rog')
print_params(b = 25)
print_params(c = [1, 2, 3])

value_list = (3, 'run', False)
value_dict = {'a':3, 'b':'cry', 'c':True}
print_params(*value_list)
print_params(**value_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)