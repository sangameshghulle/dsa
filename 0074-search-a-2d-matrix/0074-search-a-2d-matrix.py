class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col,row=0,len(matrix)-1
        mat=-1
        while col<=row:
            m=(col+row)//2
            if matrix[m][0]<=target<=matrix[m][-1]:
                mat=m
                break
            
            elif matrix[m][0]>target:

                row=m-1

            else:
                col=m+1

        if mat==-1:
            return False

        l,r=0,len(matrix[mat])-1
        while l<=r:
            mid=(l+r)//2
            if matrix[mat][mid]==target:
                return True
            
            elif matrix[mat][mid]<target:
                l=mid+1
            
            else:
                r=mid-1
        
        return False
            
        
                