def manual_sort_list(number_list:list):
    min_num:int = min(number_list)
    max_num:int = max(number_list)
    count_of_min_number:int = number_list.count(min_num)
    count_of_max_number:int = number_list.count(max_num)
    print(f"numbers: {number_list}")
    if count_of_min_number == 1:
        number_list.remove(min_num)
    else:
        for count in range(1, count_of_min_number+1):
            number_list.remove(min_num)
    print(f"remove min numbers: {number_list}")
    if count_of_max_number == 1:
        number_list.remove(max_num)
    else:
        for count in range(1, count_of_max_number+1):
            number_list.remove(max_num)
    print(f"remove max numbers: {number_list}")
    list_len = len(number_list)
    while True:

        first_num = 0
        for i in range(first_num, list_len-1):
            print(f"{i}th Stage: {number_list}")
            for j in range(i+1, list_len):
                if number_list[i] >= number_list[j]:
                    print(f"\t{i}-{j}th Stage: {number_list}")
                else:
                    number_list[i], number_list[j] = number_list[j], number_list[i]
                    print(f"\t{i}-{j}th Stage: {number_list}")
        break
    print(f"Before append Min and Max: {number_list}")
    if count_of_min_number == 1:
        number_list.append(min_num)
    else:
        for min_number in range(count_of_min_number):
            number_list.append(min_num)
    if count_of_max_number == 1:
        number_list.insert(0, max_num)
    else:
        maxNumsList = []
        for max_number in range(count_of_min_number):
            number_list.insert(0, max_num)
    
    print(f"After append Min and Max: {number_list}")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print("----------------------------")
    print(f"final List: \n{number_list[::-1]}")

numbers = [1,25,6,3,9,25,1,1,8,9,25,4,5, 41, -1, 1.23, 1023, -569, 0.26]
print("Without Sorting Function: ")
manual_sort_list(numbers)

print("With Sorting Function: ")
print(sorted(numbers))