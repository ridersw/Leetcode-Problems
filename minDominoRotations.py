from tabnanny import check


class Solution:
    def minDominoRotations(self, tops, bottoms):

        def check(x):
            rotations_a, rotations_b = 0, 0
            
            for swi in range(n):
                if tops[swi] != x and bottoms[swi] != x:
                    return -1
                
                elif tops[swi] != x:
                    rotations_a += 1
                    
                elif bottoms[swi] != x:
                    rotations_b += 1
                    
            return min(rotations_a, rotations_b)
            
        n = len(tops)
        rotations = check(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return check(bottoms[0])


if __name__ == "__main__":
    obj = Solution()

    print(obj.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
    #print(obj.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))
    #print(obj.minDominoRotations(tops = [1,2,2,1,2,1,2,1,2], bottoms= [1,2,1,1,1,1,2,1,2]))
    #print(obj.minDominoRotations(tops = [2,1,1,3,2,1,2,2,1], bottoms = [3,2,3,1,3,2,3,3,2]))