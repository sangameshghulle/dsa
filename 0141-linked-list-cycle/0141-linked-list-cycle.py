# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow=head
        seen=set()
        while slow:
            if slow in seen:
                return True
            seen.add(slow)
            slow=slow.next
        return False
