# تشخیص عدد زوج یا فرد
try:
    while True:
        userInput = str(input("Please enter a number (type 'q' to end the loop): "))
        if userInput.lower() == 'q':
            print("Exiting the program.")
            break
        if int(userInput) % 2 == 0:
            print(f"The number {userInput} is Even.")
        else:
            print(f"The number {userInput} is Odd.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
    
