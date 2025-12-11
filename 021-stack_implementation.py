def stack_implementation():
    myList = []
    while True:
        userInput = str(input("What is your purpose? (a = adding, r = removing, s = last stack, q = quit): "))
        if userInput == "a":
            userAddingItem = input("What will be add? ")
            myList.append(userAddingItem)
            print(f"{userAddingItem} is added to list.")
        elif userInput == "r":
            if len(myList) == 0:
                print("The list is EMPTY!")
            else:
                print(f"Removing Successful. {myList[-1]} is Remove.")
                myList.pop()
        elif userInput == "s":
            if len(myList) == 0:
                print("The list is EMPTY!")
            else:
                print(f"The last item of list is: {myList[-1]}")
        elif userInput == "q":
            print("Application Closed.")
            break
        else:
            print("Some thing Went Wrong.")

stack_implementation()

"""
Stack (پشته)

English:
A Stack is a data structure that follows the LIFO (Last In, First Out) principle.
This means that the last element added to the stack will be the first one to be removed.
You can think of it like a stack of plates: you put a plate on top, and when you take one, you take the top plate first.

Example:
Imagine a stack where you push numbers in this order: 5, 10, 15

Push 5 → Stack: [5]

Push 10 → Stack: [5, 10]

Push 15 → Stack: [5, 10, 15]

Pop → 15 is removed → Stack: [5, 10]

فارسی:
پشته (Stack) یک ساختار داده است که از اصل LIFO (آخرین ورودی، اولین خروجی) پیروی می‌کند.
یعنی آخرین عنصری که وارد پشته شده، اولین عنصری است که از آن خارج می‌شود.
می‌توانید آن را مثل یک پشته بشقاب تصور کنید: بشقاب جدید را روی بالای پشته می‌گذارید، و وقتی می‌خواهید بردارید، همیشه بالایی‌ترین بشقاب برداشته می‌شود.

مثال:
فرض کنید یک پشته دارید که اعداد را به ترتیب زیر اضافه می‌کنید: 5, 10, 15

Push 5 → پشته: [5]

Push 10 → پشته: [5, 10]

Push 15 → پشته: [5, 10, 15]

Pop → عدد ۱۵ حذف می‌شود → پشته: [5, 10]

"""