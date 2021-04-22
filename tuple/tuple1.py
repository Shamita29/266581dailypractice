tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
l=[]
for i in tuplex:
	if i not in l:
		l.append(i)
		t1=tuple(l)
for j in t1:
	if j in tuplex:
		print(j,':',tuplex.count(j))