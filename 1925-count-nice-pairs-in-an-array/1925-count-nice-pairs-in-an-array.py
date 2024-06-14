class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def reverse(number):
            if number ==0:
                return 0
            numbers = []
            while(number!=0):
                numbers.append(number%10)
                number = number//10 
            n = len(numbers)
            new_number = 0
            k = n-1
            for i in range(n):
                new_number += numbers[i]*(10**(k-i))
            return new_number
       
        n = len(nums)
        Rev_int = []
        max_out = 0
        for i in range(n):
            Rev_int.append(reverse(nums[i]))
        for i in range(n):
            Rev_int[i]=nums[i]-Rev_int[i]
        Dict = { }
        for i in range(n):
            if Rev_int[i] in Dict:
                Dict[Rev_int[i]] +=1
            else:
                Dict[Rev_int[i]] = 1
        for i in Dict:
                temp =  (Dict[i])*(Dict[i]-1)
                temp = temp//2
                max_out += temp
        return max_out%(10**9+7)