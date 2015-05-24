ones = ['one','two','three','four','five','six','seven','eight','nine','ten']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
tot = 0
name = None
for x in range(1,1000):
	if x<=10:
		name = ones[x-1]
	elif x>10 and x<=19:
		name = teens[x-11]
	elif x>20 and x<100:
		name = tens[(x//10)-2]
		if x%10!=0:
			name = name + ones[x%10-1]
	elif x>=100:
		name = ones[(x//100)-1] + 'hundred'
		if x%100!=0:
			name = name + 'and'
		if x%100<20 and x%100>10:
			name = name + teens[x%100-11]
		elif x%100<=10 and x%100>0:
			name = name + ones[x%100-1]
		elif x%100==20:
			name = name + tens[0]
		elif x%100==30:
			name = name + tens[1]
		elif x%100==40:
			name = name + tens[2]
		elif x%100==50:
			name = name + tens[3]
		elif x%100==60:
			name = name + tens[4]
		elif x%100==70:
			name = name + tens[5]
		elif x%100==80:
			name = name + tens[6]
		elif x%100==90:
			name = name + tens[7]
		elif x%100<100 and x%100>20:
			name = name + tens[int((((x/100)-(x//100))*10)-2)]
			if x%10!=0:
				name = name + ones[x%10-1]
	print (name)
	tot += len(name)
print(tot+9)