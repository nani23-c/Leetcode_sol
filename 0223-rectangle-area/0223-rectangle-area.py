class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def area(a,b,c,d):
            return (a-b)*(c-d)
        x2 = min(ax2,bx2)
        x1 = max(ax1,bx1)
        y2 = min(ay2,by2)
        y1 = max(ay1,by1)
        print(x2,y2)
        print(x1,y1)
        if ((bx2<=ax1) or (ax2<=bx1)) or((by2<=ay1) or (ay2<=by1)):
            return area(ax2,ax1,ay2,ay1)+area(bx2,bx1,by2,by1)
        return area(ax2,ax1,ay2,ay1)+area(bx2,bx1,by2,by1)-area(x2,x1,y2,y1)

        