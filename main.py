import math

def solve_quadratic(a, b, c):
    d = b * b - 4 * a * c
    if d < 0:
        return 0, []
    elif d == 0:
        x = -b / (2 * a)
        return 1, [x]
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b - sqrt_d) / (2 * a)
        x2 = (-b + sqrt_d) / (2 * a)
        if x1 == x2:
            return 1, [x1]
        return 2, [x1, x2]