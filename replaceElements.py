class Solution:
    def replaceElements(self, arr):

        if len(arr) == 1:
            return [-1]

        newArr = []
        
        pointer, refPointer = 0, 1
        newArr.append(max(arr[1:]))
        
        print(f'newArr: {newArr}')

        while refPointer < len(arr)-1:
            print(f'In array: {arr[refPointer:]} refPointer: {max(arr[refPointer+1:])}')
            temp = [max(arr[refPointer+1:])] * (arr.index(max(arr[refPointer+1:])) - refPointer)
            newArr.extend(temp)
            print(f'newArr: {newArr}')
            refPointer = arr.index(max(arr[refPointer+1:]))
            
            
        newArr.extend([-1])
        return newArr

if __name__ == "__main__":
    obj = Solution()

    print('newArr: ', obj.replaceElements(arr = [17,18,5,4,6,1]))
    print('newArr: ', obj.replaceElements(arr = [400]))
            