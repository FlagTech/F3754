black_list = {
    'hacker@hacker.com',
    'badboy@badbadguy.com'
}

print(len(black_list))
print('-' * 20)
black_list.add('hacker@hacker.com')
black_list.add('infiltrator@infiltrator.com')
black_list.add('hacker1@hacker.com')
for hacker in black_list:
    print(hacker)
print('-' * 20)

if 'hacker@hacker.com' in black_list:
    print('hacker@hacker.com 要過濾掉')
print('-' * 20)
black_list.remove('hacker@hacker.com')
black_list.discard('badboy@badbadguy.com')
for hacker in black_list:
    print(hacker)
print('-' * 20)
print(black_list.pop())
print(black_list)
print('-' * 20)
black_list.clear()
print(black_list)