def get_domain(email):
    return email.split('@')[-1]

print(get_domain('hacker1@hackers.tw'))
print(get_domain('hacker2@badguys.jp'))