class circle:
    pi=0
    r=0
    def __init__(self):
        self.pi=3.14
        self.r=5
    def area(self):
        print(self.r)
        return self.pi*self.r**2
ob=circle()
print(ob.area())
