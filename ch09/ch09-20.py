emails = '''
    hacker1@hackers.tw
    hacker2@hackers.tw
    hacker1@hackers.jp
    hacker2@hackers.jp
'''

domains = set(
    filter(lambda email: email.endswith('.tw'), 
        emails.strip().split())
)

for domain in domains:
    print(domain)