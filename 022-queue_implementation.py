def queue_implementation():
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
                print(f"Removing Successful. {myList[0]} is Remove.")
                myList.pop(0)
        elif userInput == "s":
            if len(myList) == 0:
                print("The list is EMPTY!")
            else:
                print(f"The last item of list is: {myList[0]}")
        elif userInput == "q":
            print("Application Closed.")
            break
        else:
            print("Some thing Went Wrong.")


queue_implementation()

"""
Queue (صف)

English:
A Queue is a data structure that follows the FIFO (First In, First Out) principle.
This means that the first element added to the queue will be the first one to be removed.
You can think of it like a line of people waiting: the person who arrives first is served first.

Example:
Imagine a queue where you enqueue numbers in this order: 5, 10, 15

Enqueue 5 → Queue: [5]

Enqueue 10 → Queue: [5, 10]

Enqueue 15 → Queue: [5, 10, 15]

Dequeue → 5 is removed → Queue: [10, 15]

فارسی:
صف (Queue) یک ساختار داده است که از اصل FIFO (اولین ورودی، اولین خروجی) پیروی می‌کند.
یعنی اولین عنصری که وارد صف شده، اولین عنصری است که از آن خارج می‌شود.
می‌توان آن را مثل صف انتظار مردم تصور کرد: کسی که زودتر رسیده، زودتر خدمت می‌گیرد.

مثال:
فرض کنید یک صف دارید که اعداد را به ترتیب زیر وارد می‌کنید: 5, 10, 15

Enqueue 5 → صف: [5]

Enqueue 10 → صف: [5, 10]

Enqueue 15 → صف: [5, 10, 15]

Dequeue → عدد ۵ حذف می‌شود → صف: [10, 15]
"""