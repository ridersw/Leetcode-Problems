class Solution:
    def problem(self, str, k):

        # if len(str) < k:
        #     return str

        # for ele in range(len(str)-(k-1)):
        #     if len(set(str[ele:ele+k])) == 1:
        #         new_str = str[:ele] + str[ele+k:]
        #         return self.problem(new_str, k)
        
        # return str      
        stck = [['$', 0]]     # a placeholder to mark stack is empty. This eliminates the need to do an empty check later
        
        for c in str:
            if stck[-1][0] == c:
                stck[-1][1]+=1 # update occurences count of top element if it matches current character
                if stck[-1][1] == k:
                    stck.pop()
            else:
                stck.append([c, 1])            
        
        return ''.join(c * cnt for c, cnt in stck)
            

if __name__ == "__main__":
    obj = Solution()
    # str = "abbcccb"
    # k = 3

    str = "baac"
    k = 2

    # str = "aba"
    # k = 2
    print(obj.problem(str, k))