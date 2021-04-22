#program to find minimum and maximum value in set

def Maximum(sets):
	return max(sets)

def Minimum(sets):
	return min(sets)
"""
setlist=set([2,3,5,6,8,28])
print(setlist)

print("Max in set is: ",Maximum(setlist))
print("Min in set is: ",Minimum(setlist))
"""

print("Enter elements to be added in set")
sets = set(map(int, input().split()))
#print(sets)
print("Maximum value in set is: ",Maximum(sets))
print("Minimum value in set is: ", Minimum(sets))