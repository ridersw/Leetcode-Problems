class Solution:
    def selectionSort(self, array):
        
        for swi in range(len(array)):
            ref_index = swi
            for swj in range(swi+1, len(array)):
                if array[ref_index] > array[swj]:
                    ref_index = swj

            array[swi], array[ref_index] = array[ref_index], array[swi]

        return array


if __name__ == "__main__":
    obj = Solution()

    array = [64, 25, 12, 22, 11]

    print(f'Sorted Array: {obj.selectionSort(array)}')


#reference- https://www.youtube.com/watch?v=g-PGLbMth_g

# Important Things to Remember- 

# 1. Time Complexity- O(n^2)
# 2. Space Complexity- 1 (Since we are not creating new array, just sorting the existing one)
# 3. Advantages- It is an in-place algorithm. It does not require a lot of space for sorting. Only one extra space is required for holding the temporal variable. It performs well on items that have already been sorted.
# 4. Disadvantage- The primary disadvantage of the selection sort is its poor efficiency when dealing with a huge list of items. Similar to the bubble sort, the selection sort requires n-squared number of steps for sorting n elements.
