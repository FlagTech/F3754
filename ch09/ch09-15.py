emails_tw = '''
    hacker1@hackers.tw
    hacker1@hackers.tw
'''

emails_jp = '''
    hacker1@hackers.jp
    hacker2@hackers.jp
'''

def filter_email(emails_str, blacklist=None):
    if blacklist is None:
        blacklist = set()
    for email in emails_str.strip().split('\n'):
        blacklist.add(email.strip())
    return blacklist


blacklist_tw = filter_email(emails_tw)
blacklist_jp = filter_email(emails_jp)

print(blacklist_tw)
print(blacklist_jp)