emails = '''
    hacker1@hackers.tw
    hacker2@hackers.tw
    hacker1@hackers.jp
    hacker2@hackers.jp
'''

domains = set(
    map(lambda email: email.split('@')[-1], 
        emails.strip().split())
)

for domain in domains:
    print(domain)