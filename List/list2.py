lst = [2,4,6,8,10,12]
new = lst[:]
for y in range(0,len(lst)-1,2):
	new[y], new[y+1] = new[y+1], new[y]
print("list: ", lst) 
print("new list:", new) 