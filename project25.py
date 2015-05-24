x = 1
nums = []
pos = 0
count = 3
go = True
while go:
	nums.append(x)
	pos+=1
	x=nums[pos-1]+nums[pos-2]
	if len(str(x)) == 1000:
		go = False
	count+=1
print(count-1)