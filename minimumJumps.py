class Solution:
	def minimumJumps(self, forbidden, a, b, x):
		backwardJump = False
		alreadyVisited = []

		ableToReach = True
		jumpInNegative = False
		
		currentPosition = 0
		
		minJumps = 0

		while ableToReach:
			if currentPosition == x:
				break
		
			print(f'Current Position: {currentPosition}')
			#print(f'')
			#print(f'{currentPosition > x} and {(currentPosition - b) not  in forbidden} and {backwardJump}')
			if currentPosition < x and (currentPosition + a) not  in forbidden:
				currentPosition += a
				print(f'Forward Jump')
				minJumps += 1
				if backwardJump:
					backwardJump = False
				
			elif currentPosition > x and (currentPosition - b) not  in forbidden and not backwardJump:	
				currentPosition -= b
				backwardJump = True
				print(f'Backward Jump')
				minJumps += 1
			else:
				ableToReach = False

		if not ableToReach:
			return -1
		return minJumps

		#def moveForward(self, forbidden, a, b, x):
			
		
		
if __name__ == "__main__":
	forbidden 	= [14,4,18,1,15] #should not land on 
	a 			= 3	 #forward jump
	b			= 15 #backward Jump
	x			= 9	 #home location
	
	#forbidden = [8,3,16,6,12,20]
	##a = 15
	#b = 13
	#x = 11
	
	#forbidden = [1,6,2,14,5,17,4]
	#a = 16
	#b = 9
	#x = 7
	
	forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
	a = 29
	b = 98
	x = 80
	
	obj = Solution()
	
	print(obj.minimumJumps(forbidden, a, b, x))
	
#A certain bug's home is on the x-axis at position x. Help them get there from position 0.

#The bug jumps according to the following rules:

#It can jump exactly a positions forward (to the right).
#It can jump exactly b positions backward (to the left).
#It cannot jump backward twice in a row.
#It cannot jump to any forbidden positions.
#The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

#Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

 

#Example 1:

#Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
#Output: 3
#Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
#Example 2:

##Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
#Output: -1
#Example 3:

#Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
#Output: 2
#Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.	