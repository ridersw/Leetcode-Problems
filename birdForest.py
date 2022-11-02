class Solution:
    def program(self, forest, bird):
        res = []
        left = bird - 1
        right = bird +1
        temp_sum = 100
        

        while True:
            print(f'Left: {left} and Right: {right}')
            if temp_sum <= 0:
                break
            
            while forest[right] == 0:
                right += 1
            
            print(f'right: {right}')
            res.append(right)
            temp_sum -= forest[right]
            right += 1
        

            if temp_sum <= 0:
                res.sort
                break
            
            while forest[left] == 0:
                left -= 1
            
            print(f'left: {left}')
            res.append(left)
            temp_sum -= forest[left]
            left -= 1


        # res.sort()
        return res
            

if __name__ == "__main__":
    obj = Solution()

    forest = [25, 0, 50, 0, 0,0,0,15, 0,0,45]
    bird = 4

    print(obj.program(forest, bird))