# محاسبه میانگین سه عدد

def mean_of_three(a, b, c):
    return (a + b + c) / 3
# توضیحات تابع mean_of_three:
# این تابع سه عدد را به عنوان ورودی می‌گیرد و میانگین آنها را محاسبه و برمی‌گرداند.




def infinity_mean():
    user_numbers_list = []
    sum_numbers = 0
    while True:
        user_number = str(input("please enter a number (or 'q' to quit): "))
        if user_number == 'q':
            print("exiting input loop.")
            break
        else:
            user_numbers_list.append(float(user_number))
    if len(user_numbers_list) != 0:
        for number in user_numbers_list:
            sum_numbers += number
        mean = sum_numbers / len(user_numbers_list)
        print(f"The mean of the {user_numbers_list} is: {mean}")
        

# توضیحات تابع infinity_mean:
# این تابع به کاربر اجازه می‌دهد تا تعداد نامحدودی عدد وارد کند و سپس میانگین آنها را محاسبه و چاپ می‌کند.
# شما می‌توانید این کد را در هر محیط برنامه‌نویسی پایتون اجرا کنید.
# پایان برنامه

# This program calculates the mean of three numbers.
# The function mean_of_three takes three numbers as input and returns their mean.
# The function infinity_mean allows the user to input an unlimited number of numbers and then calculates and prints their mean.
# You can run this code in any Python programming environment.
# End of the program

# اجرای تابع mean_of_three با اعداد نمونه
result = mean_of_three(10.5, 20.2, 30.7)
# print("میانگین سه عدد 10، 20 و 30 برابر است با:", result)

# اجرای تابع infinity_mean برای گرفتن ورودی از کاربر
infinity_mean()