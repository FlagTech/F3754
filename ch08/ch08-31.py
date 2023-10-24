black_list = {
    'hacker@hacker.com',
    'badboy@badbadguy.com',
    'hacker@hacker.com',
    'infiltrator@infiltrator.com'
}

config = {'start': 20}
for i, hacker in enumerate(black_list, **config):
    print(i, hacker) 
