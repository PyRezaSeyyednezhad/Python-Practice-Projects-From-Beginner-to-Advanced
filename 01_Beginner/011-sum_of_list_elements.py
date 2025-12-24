import numpy as np
np.random.seed(1)

def sum_of_list_elements(numbersList:list):
    try:
        total = 0
        for i in numbersList:
            total += float(i)
        print(f"Sum of {numbersList}: \n\t{total}")
    except:
        print(f"Something went wrong.")

# numbers_list = np.random.randint(1,100, 20)
# sum_of_list_elements(numbers_list)

