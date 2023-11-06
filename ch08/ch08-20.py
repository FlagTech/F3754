blacklist1 = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

blacklist2 = {
    'hacker@hacker.com',
    'infiltrator@infiltrator.com',
    'hacker1@hacker.com'
}

proper_list = blacklist1 ^ blacklist2
for hacker in proper_list:
    print(hacker)
print('-' * 20)

blacklist1.symmetric_difference_update(blacklist2)
for hacker in blacklist1:
    print(hacker)
