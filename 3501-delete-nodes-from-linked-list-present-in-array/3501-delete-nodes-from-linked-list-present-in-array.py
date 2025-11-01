class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List, Optional


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        numsSet = set()

        for x in nums:
            numsSet.add(x)

        dummy = ListNode(0, head)
        current = dummy.next
        previous = dummy
        while current:

            if current.val in numsSet:
                previous.next = current.next

            else:
                previous = current
            current = current.next

        return dummy.next
