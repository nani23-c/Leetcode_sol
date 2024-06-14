class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for alpha in s:
            if alpha.isalpha():
                res+=alpha.lower()
            if alpha.isdigit():
                res+=alpha
        if res==res[-1: :-1]:
            return True 
        else :
            return False