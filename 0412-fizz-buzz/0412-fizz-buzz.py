class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        a=[]
        for i in range(n):
            k=i+1
            if( k%15==0):
                a.append("FizzBuzz")
            elif(k%5==0):
                a.append("Buzz")
            elif(k%3==0):
                a.append("Fizz")
            else:
                h=str(k)
                a.append(h)
        return a

            