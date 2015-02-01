import math

a = 0
b = 0
c = 0
go = True
while go:
    for x in range (1,500):
        a = x
        for x in range(1,500):
            b = x
            c = math.sqrt(a*a+b*b)
            if a+b+c == 1000:
                go = False
                print(a*b*c)
