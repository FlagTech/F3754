chars = tuple('hello')
chars_tuple = tuple(chars)
print(chars_tuple)
print(f'chars is chars_tuple: {chars is chars_tuple}')
chars_list = list(chars)
chars_list1 = list(chars_list)
print(chars_list1)
print('chars_list is chars_list1:'
      f' {chars_list is chars_list1}')