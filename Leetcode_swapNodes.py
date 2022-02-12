# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        count = 0
        
        while temp:
            count += 1
            temp = temp.next
            
        # print(f'count: {count}')
        front = k
        back = count - k + 1
        
        # print(f'front: {front} and back: {back}')
        
        pointer1 = None
        pointer2 = None
        
        count = 1
        
        temp = head
        
        while temp:
            if count == front:
                pointer1 = temp
                
            if count == back:
                pointer2 = temp
                
            temp = temp.next
            count += 1
            
        pointer1.val, pointer2.val = pointer2.val, pointer1.val
        
        return head

        
                
        
        
# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]
 

# Constraints:

# The number of nodes in the list is n.
# 1 <= k <= n <= 105
# 0 <= Node.val <= 100