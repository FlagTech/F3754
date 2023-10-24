black_list = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

white_list = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com',
    'hacker1@hacker.com'
}

proper_list = black_list - white_list
for hacker in proper_list:
    print(hacker)
print('-' * 20)

black_list.difference_update(white_list)
for hacker in black_list:
    print(hacker)
