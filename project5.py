def gcf(x,y):
    return y and gcf(y, x%y) or x
def lcm(x,y):
    return x*y/gcf(x,y)

n = 1
for x in range(1,21):
    n=lcm(n,x)
print (n)
