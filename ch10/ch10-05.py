emails = (
    'hack1@hackers.tw',
    'hack2@hackers.jp',
    'hack1@hackers.tw',
)

blacklist = {}

def count_emails(emails):
    for email in emails:
        if email not in blacklist:
            # 這不是指派名稱, 所以仍然是使用全域的名稱
            blacklist[email] = 1
        else:
            blacklist[email] += 1

count_emails(emails)

for email, count in blacklist.items():
    print(f'{email}:{count}')