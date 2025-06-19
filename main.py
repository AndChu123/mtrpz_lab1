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

def print_equation(a, b, c):
    print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")

def interactive_mode():
    while True:
        a = input("a = ")
        try:
            a_val = float(a)
            if a_val == 0:
                print("Error. a cannot be 0")
                continue
            break
        except ValueError:
            print(f"Error. Expected a valid real number, got {a} instead")
    while True:
        b = input("b = ")
        try:
            b_val = float(b)
            break
        except ValueError:
            print(f"Error. Expected a valid real number, got {b} instead")
    while True:
        c = input("c = ")
        try:
            c_val = float(c)
            break
        except ValueError:
            print(f"Error. Expected a valid real number, got {c} instead")
    print_equation(a_val, b_val, c_val)
    n_roots, roots = solve_quadratic(a_val, b_val, c_val)
    print(f"There are {n_roots} roots" if n_roots > 0 else "There are 0 roots")
    if n_roots > 0:
        for i, x in enumerate(roots, 1):
            print(f"x{i} = {x}")

if __name__ == "__main__":
    interactive_mode()