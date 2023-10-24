black_list1 = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

black_list2 = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com',
    'hacker1@hacker.com'
}

proper_list = black_list1 ^ black_list2
for hacker in proper_list:
    print(hacker)
print('-' * 20)

black_list1.symmetric_difference_update(black_list2)
for hacker in black_list1:
    print(hacker)
