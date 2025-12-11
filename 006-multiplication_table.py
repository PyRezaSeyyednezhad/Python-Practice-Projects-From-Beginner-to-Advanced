#  نوشتن برنامه جدول ضرب عدد دلخواه

def multiplication_table():
    user_input_number = int(input("Please enter a number to generate its multiplication table: "))
    user_input_upto = int(input("Please enter the range up to which you want the multiplication table: "))
    i = 1
    while i <= user_input_upto:
        result = user_input_number * i
        print(f"{user_input_number} x {i} = {result}")
        i += 1 

# توضیحات تابع multiplication_table:
# این تابع از کاربر یک عدد و یک بازه می‌گیرد و جدول ضرب آن
# عدد را تا بازه مشخص شده چاپ می‌کند.
# This program generates the multiplication table of a user-defined number.
# The function multiplication_table takes a number and a range from the user and prints the multiplication table of that number up to the specified range.
# You can run this code in any Python programming environment.
# End of the program

# اجرای تابع multiplication_table برای گرفتن ورودی از کاربر
multiplication_table()