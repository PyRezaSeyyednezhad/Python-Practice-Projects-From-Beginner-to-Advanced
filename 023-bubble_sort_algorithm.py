import numpy as np

def bubble_sort_algorithm(user_list:list):
    print(f"Before: {user_list}")
    total_swap = 0
    i = 0
    while True:
        j = i+1
        if i == len(user_list)-1:
            if total_swap == 0:
                break
            else:
                total_swap = 0
                i = 0
        else:
            if user_list[i] > user_list[j]:
                user_list[i], user_list[j] = user_list[j], user_list[i]
                total_swap +=1
                i += 1
            else:
                i += 1
                continue
    print(f"After: {user_list}")

# bubble_sort_algorithm([5, 2, 9, 1])
random_list = np.random.randint(0,100,20)
bubble_sort_algorithm(random_list)