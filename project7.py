import math

def prime(n):
    if n == 2:
        return True
    if n%2 == 0 or n <= 1:
        return False
    sqr = int(math.sqrt(n)) + 1
    for x in range(3, sqr, 2):
        if n%x == 0:
            return False
    return True

pnum = 0
num = 0
go = True
while go:
    if prime(num) == True:
        pnum += 1
    if pnum == 10001:
        go = False
        print (num)
    num += 1
