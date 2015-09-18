most = 0
total = 0
soluton = 0
for x in range(1,1000000):
    total = 0
    y=x
    while(y>1):
        if(y%2==0):
            y=y/2
            total+=1
        else:
            y=3*y+1
            total+=1
    if(total>most):
        most=total
        solution=x
print(solution)