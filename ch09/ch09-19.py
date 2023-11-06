emails = '''
    hacker1@hackers.tw
    hacker2@hackers.tw
    hacker1@hackers.jp
    hacker2@hackers.jp
'''

domains = {
    email.split('@')[-1] for email in emails.strip().split()
}

for domain in domains:
    print(domain)