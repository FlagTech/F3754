blacklist = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

print(len(blacklist))
print('-' * 20)
blacklist.add('hacker@hacker.com')
blacklist.add('infiltrator@infiltrator.com')
blacklist.add('hacker1@hacker.com')
for hacker in blacklist:
    print(hacker)
print('-' * 20)

if 'hacker@hacker.com' in blacklist:
    print('hacker@hacker.com 要過濾掉')
print('-' * 20)
blacklist.remove('hacker@hacker.com')
blacklist.discard('badboy@badbadguy.com')
for hacker in blacklist:
    print(hacker)
print('-' * 20)
print(blacklist.pop())
print(blacklist)
print('-' * 20)
blacklist.clear()
print(blacklist)