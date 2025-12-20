# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        current1 = head
        current2 = head.next

        while current1 != current2:
            if not current2 or not current2.next:
                return False
            current1 = current1.next
            current2 = current2.next.next
        
        return True 
            

            

        