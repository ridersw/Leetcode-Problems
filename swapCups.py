
# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

def minSwaps(labels):
	n = len(labels)
	labelspos = [*enumerate(labels)]
	labelspos.sort(key = lambda it : it[1])
	vis = {k : False for k in range(n)}
	
	# Initialize result
	ans = 0
	for i in range(n):
		if vis[i] or labelspos[i][0] == i:
			continue
		cycle_size = 0
		j = i
		
		while not vis[j]:
			
			vis[j] = True
			
			j = labelspos[j][0]
			cycle_size += 1
			
		if cycle_size > 0:
			ans += (cycle_size - 1)
			
	return ans

# Driver Code	
labels = [3,1,2,5,4]
print(minSwaps(labels))

# This code is contributed
# by Dharan Aditya
