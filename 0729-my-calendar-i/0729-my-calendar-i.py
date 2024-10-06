class MyCalendar:
    def __init__(self):
        self.slots =[]
        return 
    def book(self, start: int, end: int) -> bool:
        if len(self.slots)==0:
            self.slots.append([start,end-1])
            return True 
        else:
            a,b= start,end-1
            for i in self.slots:
                if (i[0]-a)*(i[1]-a)<=0 or (i[0]-b)*(i[1]-b)<=0:
                    return False 
                elif (a-i[0])*(b-i[0])<=0 or (a-i[1])*(b-i[1])<=0:
                    return False 
            self.slots.append([a,b])
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)