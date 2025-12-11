# Factorial Calculation with recursive_functions
def recursive_functions(n):
    if n == 1:
        return 1
    else:
        return (n * recursive_functions(n-1))

print(recursive_functions(5))

"""
Recursive Function Example – Factorial Calculation
Implemented a recursive Python function to calculate the factorial of a number.
This project demonstrates understanding of base cases and recursive logic,
where a function repeatedly calls itself to solve a smaller instance of the same problem.
"""