from collections import deque

def areSentencesSimilar(sentence1, sentence2):
	
	#print("\n\n")
	
	#sentence1 = sentence1.split(" ")
	#sentence2 = sentence2.split(" ")
	
	#count = 0
	
	#if len(sentence1) == len(sentence2):
	#	return sentence1 == sentence2
	
	#sentence1: ['My', 'name', 'is', 'Haley']
	#sentence2: ['My', 'Haley']
	
	#indices = []
	
	#if len(sentence1) < len(sentence2):
	#	sentence1, sentence2 = sentence2, sentence1
		
	#print(f"sentence1: {sentence1}")
	#print(f"sentence2: {sentence2}")
		
	#for swi in range(len(sentence1)):
	#	if sentence1[swi] in sentence2:
	#		indices.append(swi)
	#	else:
	#		count += 1
			
	#if count == 0:
	#	return False
	
	#print(f"Indices: {indices}")
	
	#if not indices:
	#	return False
	
	#refNumber = indices[0]
	
	#for num in indices:
	#	if num - refNumber != 0:
	#		return False
		
	#	refNumber += 1
	
	#return True
	
	s1 = deque(sentence1.split(" "))
	s2 = deque(sentence2.split(" "))
	
	print("======== Initial Sentences =========")
	
	print(f"s1: {s1}")
	print(f"s2: {s2}")
	
	while s1 and s2 and s1[0] == s2[0]:
		s1.popleft()
		s2.popleft()
		
	print("======== Pop Left =========")
	
	print(f"s1: {s1}")
	print(f"s2: {s2}")

	while s1 and s2 and s1[-1] == s2[-1]:
		s1.pop()
		s2.pop()
	
	print("======== Pop Right =========")
	
	print(f"s1: {s1}")
	print(f"s2: {s2}")

	return len(s1) == 0 or len(s2) == 0
	
if __name__ == "__main__":
	#print(areSentencesSimilar(sentence1 = "My name is Haley", sentence2 = "My Haley"))	#true
	#print(areSentencesSimilar(sentence1 = "of", sentence2 = "A lot of words"))			#false
	#print(areSentencesSimilar(sentence1 = "Eating right now", sentence2 = "Eating"))	#true
	#print(areSentencesSimilar(sentence1 = "Luky", sentence2 = "Lucccky"))				#false
	#print(areSentencesSimilar(sentence1 = "Luky", sentence2 = "Luky"))					#true
	#print(areSentencesSimilar(sentence1 = "UI wqhw Lf", sentence2 = "ezzXqqEQcS"))		#false
	print(areSentencesSimilar(sentence1 = "TjZ ScAi m xz PNWaKigqqY p IyJ B rok", sentence2 = "TjZ ScAi m LlbJhCf gL u m R pZpiH mSk a og xz PNWaKigqqY p IyJ B rok"))									#true
	
	
	
#A sentence is a list of words that are separated by a single space with no leading or trailing spaces. For example, "Hello World", "HELLO", "hello world hello world" are all sentences. Words consist of only uppercase and lowercase English letters.

#Two sentences sentence1 and sentence2 are similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. For example, sentence1 = "Hello my name is Jane" and sentence2 = "Hello Jane" can be made equal by inserting "my name is" between "Hello" and "Jane" in sentence2.

#Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

#Example 1:

#Input: sentence1 = "My name is Haley", sentence2 = "My Haley"
#Output: true
#Explanation: sentence2 can be turned to sentence1 by inserting "name is" between "My" and "Haley".
#Example 2:

#Input: sentence1 = "of", sentence2 = "A lot of words"
#Output: false
#Explanation: No single sentence can be inserted inside one of the sentences to make it equal to the other.
#Example 3:

#Input: sentence1 = "Eating right now", sentence2 = "Eating"
#Output: true
#Explanation: sentence2 can be turned to sentence1 by inserting "right now" at the end of the sentence.
#Example 4:

#Input: sentence1 = "Luky", sentence2 = "Lucccky"
#Output: false
 

#Constraints:

#1 <= sentence1.length, sentence2.length <= 100
#sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
#The words in sentence1 and sentence2 are separated by a single space.	