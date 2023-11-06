emails = '''
    hacker1@hackers.tw
    hacker2@hackers.tw
    hacker1@hackers.jp
    hacker2@hackers.jp
'''

domains = {
    email for email in emails.strip().split() 
        if email.endswith('.tw')
}

for domain in domains:
    print(domain)