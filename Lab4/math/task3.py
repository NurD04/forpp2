import math
def area_polygon(len_side, num):
    area = (num * (len_side ** 2)) / (4 * math.tan(math.pi / num))
    return area
print("Area of regular polygon is :", area_polygon(int(input("length of sides: ")), int(input("number of side: "))))