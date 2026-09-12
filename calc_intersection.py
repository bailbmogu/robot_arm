import math

def calc_intersection(c1x, c1y, r1, c2x, c2y, r2):
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

    x1 = xmid - h * dy / d
    y1 = ymid + h * dx / d
    x2 = xmid + h * dy / d
    y2 = ymid - h * dx / d

    return [(round(x1, 2), round(y1, 2)), (round(x2, 2), round(y2, 2))]

    
print(calc_intersection(0, 0, 10, 4, -6.5, 5))