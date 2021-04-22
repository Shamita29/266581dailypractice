arr=[]
n = int(input())
for i in range(n):
    arr.append(int(input()))
arr.sort()
max1=arr[1]
print("Second smallest number is: ",max1)
#arr.sort(reverse=True)
'''for x in arr:
    if x!=max1:
        result = x
        print(result)
        break'''
    