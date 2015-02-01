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

sum = 0
for x in range(1,2000000):
    if prime(x) == True:
        sum+=x
print (sum)
