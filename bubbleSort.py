class Solution:
    def bubbleSort(self, array):
        
        for count in range(len(array)-1):
            isSwapped= False

            for swi in range(len(array)-1-count):
                if array[swi] > array[swi+1]:
                    array[swi], array[swi+1] = array[swi+1], array[swi]
                    isSwapped = True
            
            if isSwapped == False:
                break

        
        return array



if __name__ == "__main__":
    obj = Solution()

    array = [9,8,7,6,5,4,3,2,1]

    print(obj.bubbleSort(array))