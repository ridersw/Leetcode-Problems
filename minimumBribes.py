def minimumBribes(q):
	bribes = 0
    for i in range(len(q)-1,-1,-1):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return
        for j in range(max(0, q[i] - 2),i):
            if q[j] > q[i]:
                bribes+=1
    print(bribes)
	
def sorting(q, tempArray, num):
	for swi in range(0, len(q)):
		if q[swi] > q[swi+1]:
			q[swi], q[swi+1] = q[swi+1], q[swi]
			if q != tempArray:
				num += 1
				#print("Sorting q: ", q)
				return sorting(q, tempArray, num)
			else:
				num += 1
				return num
			
	
	
	

	
	
if __name__ == "__main__":
   #q = [1, 2, 3, 4, 5, 6, 7, 8]
	q = [1, 2, 5, 3, 7, 8, 6, 4]
   #q = [1, 2, 5, 3, 4, 6, 7, 8]
   #q = [1, 2, 5, 3, 7, 4, 6, 8]
   #q = [1, 2, 5, 3, 7, 8, 4, 6]
   #q = [1, 2, 5, 3, 7, 8, 6, 4]
	minimumBribes(q)
	#print("Change in Position: ", result)