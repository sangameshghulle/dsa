"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # if not head:
        #     return head
        
        # dummy=head
        # while dummy.next:
        #     while dummy  and not dummy.child:
        #         dummy=dummy.next
        #     if dummy is None:
        #         return head
        #     elif dummy.child:
        #         nextNode=dummy.next
        #         dummy.next=dummy.child
        #         node=dummy
        #         while not node.next:
        #             node.next=nextNode
        #             nextNode.prev=node
        #     dummy=dummy.next

        if not head:
            return head

        curr = head

        while curr:
            if curr.child:
                # Save the original next node
                next_node = curr.next

                # Attach child list after curr
                child = curr.child
                curr.next = child
                child.prev = curr

                # Find the tail of the child list
                tail = child
                while tail.next:
                    tail = tail.next

                # Connect child tail to original next
                tail.next = next_node

                if next_node:
                    next_node.prev = tail

                # Remove child pointer
                curr.child = None

            curr = curr.next

        return head
