def buddyStrings(a, b):
	if len(a) != len(b):
		return False
		
	notSimilarA = []
	notSimilarB = []
	
	for swi in range(len(a)):
		if a[swi] != b[swi]:
			notSimilarA.append(a[swi])
			notSimilarB.append(b[swi])
			
	print(f"notSimilarA: {notSimilarA}")
	print(f"notSimilarB: {notSimilarB}")
	
	if len(notSimilarA) > 2:
		return False
		
	if not notSimilarA:
		if len(set(a)) == len(a):
			return False
	else:
		for swi in range(len(notSimilarA)):
			if notSimilarA[swi] not in notSimilarB:
				return False
				
	return True
	
	
if __name__ == "__main__":
	
	#a = "ab"
	#b = "ba"
	
	#a = "ab"
	#b = "ab"
	
	#a = "aa"
	#b = "aa"
	
	#a = "abcaa"
	#b = "abcbb"
	print(buddyStrings(a, b))