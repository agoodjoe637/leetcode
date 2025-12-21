# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        list_stack = []
        current = head

        while current:
            list_stack.append(current)
            current = current.next
        
        swap_count= len(list_stack) // 2

        current = head

        for _ in range(swap_count):
            nxt = current.next
            top_node = list_stack.pop()
            current.next = top_node
            top_node.next = nxt
            current = nxt
        
        current.next = None