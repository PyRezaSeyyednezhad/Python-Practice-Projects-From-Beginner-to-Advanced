def file_create():
    fileName = str(input("Enter file name: "))
    file_open = open(f"./files/{fileName}.txt", 'w')
    print("The File Created")
    print(f"Write what you want in '{fileName}.txt'")
    userText = str(input(">> "))
    with open(f"./files/{fileName}.txt", '+r') as file1:
        file1.write(userText)
        print(file1.read())
        
    
def file_read():
    with open("./files/example.txt", 'r') as file1:
        print(file1.read())

def file_write():
    print(f"Write what you want in 'example.txt'")
    userText = str(input(">> "))
    with open("./files/example.txt", 'w+') as file1:
        file1.write(userText)
        print(file1.read())

def file_edit():
    with open("./files/example.txt", 'a+') as file1:
        file1.readlines()
        userText = str(input(">> "))
        file1.write(userText)
        print(file1.read())

while True:
    userInput = str(input("What is your purpose? (create = c, read = r, write = w, edit == e, quite = q): "))
    if userInput == 'c':
        file_create()
    elif userInput == 'r':
        file_read()
    elif userInput == 'w':
        file_write()
    elif userInput == "e":
        file_edit()
    elif userInput == 'q':
        print("Application Closed.")
        break
    else:
        print("Something went Wrong.")