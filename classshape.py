class shape:
    def area(self):
        pass
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14 * self.r ** 2
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
c=circle(5)
print("area of circle is",c.area())
r=rectangle(4,5)
print("area of rectangle is",r.area())

