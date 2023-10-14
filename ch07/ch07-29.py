txt_animations = (
    (r'―\|/―\|/', 0.3, 0.2, 0.5),
    ('◑◒◐◓◑◒◐◓', 0.2)
)
for txt, *intervals in txt_animations:
    print(txt)
    for interval in intervals:
        print(f'\t{interval}')