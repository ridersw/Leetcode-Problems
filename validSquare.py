def validSquare(p1, p2, p3, p4):
	points = [p1,p2,p3,p4]
	
	xMatch = []
	yMatch = []
	
	if p1[0] == p2[0]:
		xMatch.append(p1)
		xMatch.append(p2)
		yMatch.append(p3)
		yMatch.append(p4)
	elif p1[0] == p3[0]:
		xMatch.append(p1)
		xMatch.append(p3)
		yMatch.append(p2)
		yMatch.append(p4)
	elif p1[0] == p4[0]:
		xMatch.append(p1)
		xMatch.append(p4)
		yMatch.append(p2)
		yMatch.append(p3)
	else:
		return False
	
	xMatch.sort()
	yMatch.sort()
	print(f"xMatch: {xMatch}")
	print(f"yMatch: {yMatch}")
	
	tempX = xMatch[0]
	tempX1 = xMatch[1]
	tempY = yMatch[0]
	tempY1 = yMatch[1]
	
	if tempX[1] - tempY[1] == tempX1[1] - tempY1[1] and tempX1[0] - tempX[0] == tempY1[0] - tempY[0]:
		return True
	return False
	
	
if __name__ == "__main__":
	p1 = [1,0]
	p2 = [-1,0]
	p3 = [0,1]
	p4 = [0,-1]
	
	#p1 = [0,0]
	#p2 = [5,0]
	#p3 = [5,4]
	#p4 = [0,4]
	print(validSquare(p1,p2,p3,p4))
	
#Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

#The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

#A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

#Example 1:

#Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
#Output: true
#Example 2:

#Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
#Output: false
#Example 3:

#Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
#Output: true