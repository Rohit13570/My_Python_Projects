class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __mul__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return x,y
    def str(self):
        return"{0},{1}".format(self.x,self.y)
p1=point(1,4)
p2=point(2,9)
print(p1*p2)