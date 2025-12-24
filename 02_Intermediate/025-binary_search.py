# Implemented a recursive version of Binary Search algorithm using dynamic list partitioning (inspired by QuickSort pivot logic).
def binary_search(user_list:list, user_number):
    user_list.sort()
    if len(user_list) <= 1:
        if user_number in user_list:
            return True
        else:
            return False
    
    pivot = user_list[len(user_list) // 2]
    left = [x for x in user_list if x < pivot]      # عناصر کوچکتر از pivot
    middle = [x for x in user_list if x == pivot]   # عناصر برابر با pivot
    right = [x for x in user_list if x > pivot]
    
    if user_number in middle:
        return True
    elif user_number > pivot:
        return binary_search(right, user_number)
    elif user_number < pivot:
        return binary_search(left, user_number)
    

print(binary_search([5,10,5,6,7,9,8,1,9, 1, 2, 3, 4, 7, 6], 1))