sol1 = 0
sol2 = 0
for x in range(1,101):
    sol1 += x*x
    sol2 += x
sol2 = sol2*sol2
print(sol2-sol1)
