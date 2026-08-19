class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans=0
        seen={'T':0,'F':0}
        l,r=0,0
        countT,countF=0,0
        n=len(answerKey)
        while r<n:
            if answerKey[r]=='T':
                countT+=1
            else:
                countF+=1
            while countT>k and countF>k:
                if answerKey[l]=='T':
                    countT-=1
                else:
                    countF-=1
                l+=1
            if ans<countT+countF:
                ans=countT+countF
            r+=1

        return ans