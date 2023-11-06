blacklist = {
    'hacker@hacker.com',
    'badboy@badbadguy.com',
    'hacker@hacker.com',
    'infiltrator@infiltrator.com'
}

config = {'start': 20}
for i, hacker in enumerate(blacklist, **config):
    print(i, hacker) 
