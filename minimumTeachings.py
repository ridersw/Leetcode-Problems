def minimumTeachings(n, languages, friendships):

	noConversation = []
	
	for f1, f2 in friendships:
		temp1 = set(languages[f1-1])
		temp2 = set(languages[f2-1])
		
		if len(temp1.intersection(temp2)) < 1:
			noConversation.append(f1)
			noConversation.append(f2)
	
	noConversation = set(noConversation)
	#print(f"len(noConversation): {len(noConversation)}")
	
	if len(noConversation) < 1:
		return 0

	dict = {}
	
	for person in noConversation:
		for lang in languages[person-1]:
			if lang in dict:
				dict[lang] += 1
			else:
				dict[lang] = 1
		
	#print(f"max(dict.values()): {max(dict.values())}")
	
	return len(noConversation) - max(dict.values())
		
if __name__ == "__main__":
	n = 11
	languages =  [[3,11,5,10,1,4,9,7,2,8,6],[5,10,6,4,8,7],[6,11,7,9],[11,10,4],[6,2,8,4,3],[9,2,8,4,6,1,5,7,3,10],[7,5,11,1,3,4],[3,4,11,10,6,2,1,7,5,8,9],[8,6,10,2,3,1,11,5],[5,11,6,4,2]]
	friendships = [[7,9],[3,7],[3,4],[2,9],[1,8],[5,9],[8,9],[6,9],[3,5],[4,5],[4,9],[3,6],[1,7],[1,3],[2,8],[2,6],[5,7],[4,6],[5,8],[5,6],[2,7],[4,8],[3,8],[6,8],[2,5],[1,4],[1,9],[1,6],[6,7]]
	result = minimumTeachings(n, languages, friendships)
	print(f"Result: {result}")
	
	
#1733. Minimum Number of People to Teach

#On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

#You are given an integer n, an array languages, and an array friendships where:

#There are n languages numbered 1 through n,
#languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
#friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
#You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

#Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

#Example 1:

#Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
#Output: 1
#Explanation: You can either teach user 1 the second language or user 2 the first language.

#Example 2:

#Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
#Output: 2
#Explanation: Teach the third language to users 1 and 3, yielding two users to teach.