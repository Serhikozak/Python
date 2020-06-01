class Rectangle:

    def __init__(self, length_rec, width_rec):
        self.length_rec = length_rec
        self.width_rec = width_rec

    def perimeter(self):
        p = self.length_rec * 2 + self.width_rec * 2
        print(p)

    def area(self):
        a = self.length_rec * self.width_rec
        print(a)


result = Rectangle(5, 3)
result.perimeter()
result.area()

