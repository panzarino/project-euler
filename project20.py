import math
def numlen(num):
    return len(str(num))
n = math.factorial(100)
nstr = str(n)
nlen = numlen(n)
tot = 0
for x in range(nlen):
    tot=tot+int(nstr[x])
print (tot)
