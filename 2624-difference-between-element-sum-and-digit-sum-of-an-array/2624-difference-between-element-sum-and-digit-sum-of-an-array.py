class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        numbers = 0 
        digits = 0 
        n= len(nums)
        for i in range(n):
            numbers += nums[i]
            string = str(nums[i])
            string == list(string)
            for _ in range(len(string)):
                digits += int(string[_])
        return abs(numbers-digits)
        