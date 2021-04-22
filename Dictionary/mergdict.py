
'''
d1={'name':"Shamita", 'lname':"C"}
d2={'Sfid':266581, 'age':21}

d1.update(d2)
print(d1)

'''

dict1={}
dict2={}
n=int(input())
for i in range(n):
	data = input().split(' ')
	dict1[data[0]] = str(data[1])

print("Now create another dictionary")
for i in range(n):
	data=input().split(' ')
	dict2[data[0]]= int(data[1])

dict1.update(dict2)
print(dict1)
