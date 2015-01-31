n = 0
for x in range(999, 100, -1):
    for y in range(x, 100, -1):
        num = x * y
        if num > n:
            sm = str(x * y)
            if sm == sm[::-1]:
                n = x * y

print (n)
