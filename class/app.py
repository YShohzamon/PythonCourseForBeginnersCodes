class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("moved")

    def drow(self):
        print("drow")


point1 = Point(332 , 321)
point1.x = 100
point1.y = 200
point1.move()
print(point1.x, point1.y)

point2 = Point(23 ,21)
print(point2.x, point2.y)
