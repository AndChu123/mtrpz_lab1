import sys
import math
import os

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
    print(f"Quadratic equation: ({a}) x^2 + ({b}) x + ({c}) = 0")

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

def file_mode(filename):
    if not os.path.exists(filename):
        print(f"file {filename} does not exist")
        sys.exit(1)
    try:
        with open(filename, 'r') as f:
            line = f.readline()
            if not line.endswith('\n'):
                print("invalid file format")
                sys.exit(1)
            parts = line.strip().split(' ')
            if len(parts) != 3:
                print("invalid file format")
                sys.exit(1)
            a, b, c = parts
            a = float(a)
            b = float(b)
            c = float(c)
            if a == 0:
                print("Error. a cannot be 0")
                sys.exit(1)
    except ValueError:
        print("invalid file format")
        sys.exit(1)
    except Exception:
        print("invalid file format")
        sys.exit(1)
    print_equation(a, b, c)
    n_roots, roots = solve_quadratic(a, b, c)
    if n_roots == 0:
        print("There are 0 roots")
    else:
        print(f"There are {n_roots} roots", end=' ')
        for i, x in enumerate(roots, 1):
            print(f"x{i} = {x}", end=' ')
        print()

def main():
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 2:
        file_mode(sys.argv[1])
    else:
        print("Usage: python main.py [input_file]")
        sys.exit(1)

if __name__ == "__main__":
    main()