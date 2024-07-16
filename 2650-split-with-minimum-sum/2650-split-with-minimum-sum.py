class Solution:
    def splitNum(self, num: int) -> int:
        num = str(num)
        num = list(num)
        num.sort()
        num1 =num2 =""
        n = len(num)
        for i in range(n):
            if i%2==0:
                num1 += num[i]
            else:
                num2 += num[i]
        return int(num1)+int(num2)
        