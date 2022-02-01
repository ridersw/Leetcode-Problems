class Solution:
    def nextGreaterElement(self, n):
        if n>=2**31-1:
            return -1
        a=list(str(n))
        temp=None
        for i in range(len(a)-1,0,-1):
            if a[i]>a[i-1]:
                temp=a[i-1]
                idx=i-1
                break
        if not temp:
            return -1
        for i in range(len(a)-1,-1,-1):
            if a[i]>temp:
                a[i],a[idx]=a[idx],a[i]
                break
        res=int("".join(a[:idx+1]+sorted(a[idx+1:])))
        if res>2**31-1:
            return -1
        else:
            return res
if __name__ == "__main__":
    obj = Solution()

    print(obj.nextGreaterElement(n = 230241))

#1234
#1243