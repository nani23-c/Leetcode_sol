class Solution:
    def average(self, salary: List[int]) -> float:
        max = 0 
        min = 1000000 
        sum = 0 
        lenth = len(salary)
        for i in range(lenth):
            sum += salary[i]
            if salary[i]>max:
                max = salary[i]
            if salary[i] < min :
                min = salary [i]
        lenth -=2
        sum = sum-min-max
        return sum/lenth
        