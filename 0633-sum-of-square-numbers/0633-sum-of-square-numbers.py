class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left,right = 0,int(sqrt(c))
        while(left<=right):
            if left*left+right*right==c:
                return True 
            elif left*left+right*right>c:
                right = right-1 
            else:
                left = left+1 
        return False
                

        