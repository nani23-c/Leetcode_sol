class Solution:
    def findComplement(self, num: int) -> int:
        X = len(bin(num))-2
        return 2**X-num-1
        