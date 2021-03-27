def routePairs(maxTravelDist, forwardRouteList, returnRouteList):
	plan = []
	sum = []
	
	for swi in range(len(forwardRouteList)):
		for swj in range(len(returnRouteList)):
			if forwardRouteList[swi][1] + returnRouteList[swj][1] <= maxTravelDist:				
				plan.append([swi+1, swj+1])
				sum.append(forwardRouteList[swi][1] + returnRouteList[swj][1])
			
	print(plan)
	print(sum)
	
	finalPlan = []
	
	if maxTravelDist in sum:	
		for swi in range(len(sum)):
			if int(sum[swi]) == maxTravelDist:
				print(f"int(sum[swi]): {int(sum[swi])}")
				print(f"maxTravelDist: {maxTravelDist}")
				finalPlan.append(plan[swi])
		print(f"finalPlan: {finalPlan}")
	else:
		plan = plan[::-1]
		sum = sum[::-1]
		
		for swi in range(0, len(plan)):
			if sum[swi] == sum[0]:
				finalPlan.append(plan[swi])
		
	if len(finalPlan) > 0:
		return finalPlan
	else:
		return [[]]
	
	
if __name__ == "__main__":
	maxTravelDist = 9000
	forwardRouteList = [[1, 3000],[2, 5000],[3, 7000],[4, 10000]]
	returnRouteList = [[1, 2000], [2, 3000], [3, 4000], [4, 5000]]
	
	result = routePairs(maxTravelDist, forwardRouteList, returnRouteList)
	
	print(f"result: {result}")
	
#find a optimal flight plan (combination of sum of forwardRouteList and returnRouteList) so that it is less than or equal to the maxTravelDist