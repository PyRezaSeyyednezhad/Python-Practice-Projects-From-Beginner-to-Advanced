def phonebook_text_file():
    userInput = str(input("Phone Book App. \n1.\tCreate(c)\n2.\tRead(r)\n3.\tUpdate(u)\n4.\tDelete(d)\nWhat is your Purpose? "))
    if userInput == "c":
        username = str(input("Enter username: "))
        number = str(input("Enter number: "))
        new_member = f"{username} : {number}\n"
        with open("./files/phonebook_text_file.txt", 'a') as File1:
            File1.write(new_member)
    elif userInput == "r":
        with open("./files/phonebook_text_file.txt", 'r') as File1:
            print(File1.read())
    elif userInput == "u":
        username = str(input("Enter username (if username does not exist, then we added to phone book for new member): "))
        number = str(input("Enter number: "))
        with open("./files/phonebook_text_file.txt", 'r') as File1:
            get_text_file = File1.read()
            split_the_users = get_text_file.split("\n")
            print(split_the_users)
            for index, user in enumerate(split_the_users):
                if user == "":
                    continue
                else:
                    name, num = user.split(" : ")
                    # print(name, num)
                    if name == username:
                        user_update = f"{username} : {number}"
                        split_the_users[index] = user_update
                    else:
                        continue
            print(split_the_users)
            new_text = ""
        with open("./files/phonebook_text_file.txt", 'w') as File2:
            
    else:
        pass

phonebook_text_file()