def hotel(arrive, depart, k):
    events = [(t, 1) for t in arrive] + [(t, 0) for t in depart]
    events.sort(key=lambda x: (x[0], x[1]))
    guests = 0
    for event in events:
        if event[1] == 1:
            guests += 1
        else:
            guests -= 1
        if guests > k:
            return 0
    return 1


res = hotel([1, 2, 3], [2, 3, 4], 1)
print res
