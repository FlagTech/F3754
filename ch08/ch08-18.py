black_list = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

new_list = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com',
    'hacker1@hacker.com'
}

proper_list = black_list & new_list
for hacker in proper_list:
    print(hacker)
print('-' * 20)

black_list.intersection_update(new_list)
for hacker in black_list:
    print(hacker)
