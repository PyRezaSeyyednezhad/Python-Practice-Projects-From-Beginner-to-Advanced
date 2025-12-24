def remove_duplicates_from_list(userList:list):
    # First Method
    # print(f"User List: \n\t{userList}")
    # for i in userList:
    #     if userList.count(i) == 1:
    #         continue
    #     else:
    #         userList.pop()
    # print(f"Remove Duplicated Items:  \n\t{userList}")
    # Second Method
    print(f"The main list: {userList}\n Remove Duplicates: {list(set(userList))}")



remove_duplicates_from_list([1,2,5,"hello", "hel", "owl", "hellow", "hell", "hel", 2, "2"])
