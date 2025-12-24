import numpy as np
def max_min_in_list(numbers_list:list):
    return f"max num: {max(numbers_list)}\n min num: {min(numbers_list)}"
np.random.seed(1)
numbers = np.random.randint(1, 200, 50)

# print(f"numbers = {numbers} \n {max_min_in_list(numbers)}")

def max_min_online():
    numbersList = []
    while True:
        userInput = str(input("Enter an Integer number (Enter 'q' for break the loop):"))
        if userInput == 'q':
            break
        elif userInput == "":
            numbersList.append(0)
        elif userInput.isalpha():
            print(f"\t!!!  Enter An Integer Number.  !!!\t")
            break
        else:
            numbersList.append(int(userInput))
    print(f"numbersList: {numbersList}\n Max.: {max(numbersList)}\n Min.: {min(numbersList)}")


max_min_online()