def count_item_frequency(user_list:list):
    delDuplicated = list(set(user_list))
    resList = []
    for item in delDuplicated:
        resList.append((item, user_list.count(item)))
    print(f"count_item_frequency (item, count): \n\t {resList}")

# count_item_frequency([1,2,5,"hello", "hel", "owl", "hellow", "hell", "hel", 2, "2", "hello", "owl", "owl"])