def divide_numbers(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        return f"Cannot Divide {a}/{b}, Cause b = 0."
    except TypeError:
        return f"a or b are not NUMBER."
    else:
        return f"Result: {result}\n The Progress Successful."
    finally:
        print("-------------------------")

print(divide_numbers(1,2))
print(divide_numbers(1,3))
print(divide_numbers(1,1))
print(divide_numbers(1,100))
print(divide_numbers(1,0))
print(divide_numbers(1,"0"))