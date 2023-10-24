black_list = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

new_list1 = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com'
}

new_list2 = {'hacker1@hacker.com'}

whole_list = black_list.union(new_list1, new_list2)
for hacker in whole_list:
    print(hacker)
print('-' * 20)

for hacker in black_list:
    print(hacker)
print('-' * 20)

black_list |= new_list1 | new_list2
for hacker in black_list:
    print(hacker)
