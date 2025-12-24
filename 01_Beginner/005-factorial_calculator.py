# محاسبه فاکتوریل عدد
def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# توضیحات تابع factorial:
# این تابع یک عدد صحیح غیر منفی را به عنوان ورودی می‌گیرد و ف
#اکتوریل آن را محاسبه و برمی‌گرداند.
# This program calculates the factorial of a number.
# The function factorial takes a non-negative integer as input and returns its factorial.
# You can run this code in any Python programming environment.
# End of the program
# اجرای تابع factorial با عدد نمونه
number = 5
fact_result = factorial(number)
print(f"The factorial of {number} is: {fact_result}")