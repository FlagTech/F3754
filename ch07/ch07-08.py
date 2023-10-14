interval1 = 0.1, 0.2
interval2 = 0.3, 0.5, 0.8
interval3 = interval1 * 2
print(interval3)
intervals = interval1 + interval2
print(intervals)
print(len(intervals))
print(intervals.count(0.1))

if 0.3 in intervals:
    print(intervals.index(0.3))

if 8 in intervals:
    print(intervals.index(8))