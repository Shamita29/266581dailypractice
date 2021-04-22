y=int(input('year:'))
m=int(input('month:'))
d=int(input('day:'))
ml=(1,2,3,4,5,6,7,8,9,10,11,12)
if d>28 and m ==2:
	print("enter valid dates for february")
	#print(1,'/',m+1,'/',y)
elif d==30 and m in(4,6,9,11):
	print(1,'/',m+1,'/',y)
elif d==31 and m in(1, 3, 5, 7, 8, 10):
	print(1,'/',m+1,'/',y)
elif d==31 and m==12:
	print(1,'/',1,'/',y+1)
elif m not in ml:
	print('error in month name')
else:
	print(d+1,'/',m,'/',y)