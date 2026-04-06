class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        posibilities = [[0,1],[1,0],[0,-1],[-1,0]]
        n_p = 0
        x,y = 0,0 
        ans = 0 
        obstacle_set = set(map(tuple, obstacles))
        n = len(commands)
        for i in range(n):
            a,b = x,y
            if commands[i]>=0:
                for j in range(commands[i]):
                    a += posibilities[n_p][0]
                    b += posibilities[n_p][1]
                    if (a,b) in obstacle_set:
                        a = a - posibilities[n_p][0]
                        b = b - posibilities[n_p][1]
                        break
                x = a
                y = b
                ans = max(ans,x**2+y**2)
            elif commands[i]== -1:
                n_p +=1 
                n_p = n_p %4 
            else:
                n_p -=1 
                n_p = n_p %4 
        return ans


            

        