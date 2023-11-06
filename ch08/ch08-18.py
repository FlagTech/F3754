blacklist = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

new_list = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com',
    'hacker1@hacker.com'
}

proper_list = blacklist & new_list
for hacker in proper_list:
    print(hacker)
print('-' * 20)

blacklist.intersection_update(new_list)
for hacker in blacklist:
    print(hacker)
