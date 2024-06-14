class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        n=len(moves)
        a=0 #to store empty digits
        b=0 #to store pogress
        for i in range(n):
            if moves[i]=="R":
                b +=1
            elif moves[i]=="L":
                b -=1 
            else:
                a +=1 
        return abs(b)+a
        