# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy=ListNode(0)
        ans=dummy
        n=0
        for i in lists:
            if i is not None:
                n+=1

        while n>0:
            
            smallest=min((i for i,node in enumerate(lists) if node is not None),key=lambda i:lists[i].val)
            
            ans.next=ListNode(lists[smallest].val)
            ans=ans.next
            
            lists[smallest]=lists[smallest].next
            
            if lists[smallest] is None:
                n-=1
            
        return dummy.next