class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        if not target:
            return []
        i=1
        j=0
        op=[]

        t=len(target)

        while i<=n and j<t:

            op.append("Push")

            if i!=target[j]:
                op.append("Pop")

            else:
                j+=1
            i+=1

        return op