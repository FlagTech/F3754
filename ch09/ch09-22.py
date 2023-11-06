emails = (
    'hacker1@hackers.tw',
    'hacker1@hackers.jp',
    'hacker2@hackers.jp',
    'hacker2@hackers.tw'
)

for email in sorted(
    emails, 
    key = lambda email: email.split('.')[-1]):
    print(email)