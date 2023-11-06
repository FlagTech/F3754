blacklist = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

whitelist = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com',
    'hacker1@hacker.com'
}

proper_list = blacklist - whitelist
for hacker in proper_list:
    print(hacker)
print('-' * 20)

blacklist.difference_update(whitelist)
for hacker in blacklist:
    print(hacker)
