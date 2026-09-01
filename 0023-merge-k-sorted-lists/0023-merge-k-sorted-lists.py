# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None:
            return None
        dummy=ListNode(0)
        ans=dummy
        while True:
            available = [node for node in lists if node is not None]

            if not available:
                break

            smallest=min((i for i,node in enumerate(lists) if node is not None),key=lambda i:lists[i].val)
            ans.next=ListNode(lists[smallest].val)
            ans=ans.next
            lists[smallest]=lists[smallest].next
            
        return dummy.next