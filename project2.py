val1 = 1
val2 = 2
total1 = 0
total2 = 2 #2 is from 1+2
go = True
while go:
    total1 = val1+val2
    if total1%2==0:
        total2+=total1
    val1 = val2
    val2 = total1
    if total1>=4000000:
        go = False
print (total2)
