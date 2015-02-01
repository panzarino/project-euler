def numlen(num):
    return len(str(num))
n = 2**1000
nlen = numlen(n)
nstr = str(n)
tot = 0
for x in range(nlen):
    tot+=int(nstr[x])
print (tot)
