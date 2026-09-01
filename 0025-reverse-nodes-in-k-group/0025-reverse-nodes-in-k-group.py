# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        current = dummy

        while True:

            # Find kth node
            node = current

            for _ in range(k):
                if node.next is None:
                    return dummy.next

                node = node.next

            # Save important boundaries
            group_prev = current
            group_head = current.next
            group_next = node.next

            # Reverse k nodes
            prev = group_next
            curr = group_head

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Reconnect
            group_prev.next = prev

            # Old head becomes new tail
            current = group_head