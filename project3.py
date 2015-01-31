n = 600851475143
y = 2
while y*y<n:
    while n%y==0:
        n=n/y
    y+=1
print (n)
