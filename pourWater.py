import math

class Solution:
    def pourWater(self, heights, volume, k):

        heights = [math.inf] + heights + [math.inf]
        print(heights[1:-1])    
        while volume > 0:
            
            if heights[k] < heights[k-1] and heights[k] < heights[k+1]:
                heights[k] += 1

            else:
                pointer1 = k-1
                pointer2 = k+1

                while True:
                    if heights[pointer1] < heights[pointer2]:
                        print(f'Found {pointer1} < {pointer2}')
                        heights[pointer1] += 1
                        break
                    elif heights[pointer1] > heights[pointer2]:
                        print(f'Found {pointer1} > {pointer2}')
                        heights[pointer2] += 1
                    else:
                        print('else')
                        pointer1 -= 1
                        pointer2 += 1 
            volume -= 1

        return heights[1:-1]

if __name__ == "__main__":
    obj = Solution()
    print(obj.pourWater(heights = [2,1,1,2,1,2,2], volume = 4, k = 3))