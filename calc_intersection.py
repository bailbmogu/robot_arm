import math

def calc_intersection(c1x, c1y, r1, c2x, c2y, r2, roundto):
    dx = c2x - c1x
    dy = c2y - c1y
    d = math.hypot(dx, dy)

    #* If centers are same
    if d == 0:
        if r1 != r2:
            return[]
        raise ValueError("Same circle, infinite intersections")

    l = (r1**2 - r2**2 + d**2) / (2*d)
    h = math.sqrt(r1**2 -l**2)

    xmid = c1x + l * dx/d
    ymid = c1y + l*dy/d

    if h ==0:
        return[(xmid,ymid)]

    x1 = xmid + h * dy / d
    y1 = ymid - h * dx / d
    x2 = xmid - h * dy / d
    y2 = ymid + h * dx / d

    return [(round(x1, roundto), round(y1, roundto)), (round(x2, roundto), round(y2, roundto))]


#! Test cases
if calc_intersection(6, 7, 67, -6, -7, 67, 2) != [(-50.39, 43.19), (50.39, -43.19)]:
     print("Test 1 failed")

if calc_intersection(0, 0, 10, 4, -6.5, 5, 2) != [(0.42, -9.99), (8.73, -4.88)]:
        print("Test 2 failed")

if calc_intersection(-50, 50, 25, 50, 50, 30, 2) != []:
    print ("test 3 failed")

if calc_intersection(100, 67, 55, 37, 31.4, 60, 1) != [(50.0, 90.0), (93.9, 12.3)]:
    print("test 4 failed")

if calc_intersection(400, 800, 100, 400, 650, 50, 0) != [(400,700), (400,700)]:
    print("test 5 failed")