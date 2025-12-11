import numpy as np
def random_number_generator(start:int, end:int, size:int, unique:bool):
    if unique == True:
        np.random.seed(1)
    return np.random.randint(start, end, size)

# print(random_number_generator(1,6,2,False))
# print(random_number_generator(1,6,2,False))

def random_number_guess_game():
    guess_number = random_number_generator(1,6,1,False)[0]
    user = int(input("Guess number from 1 to 6: "))
    if guess_number == user:
        print(f"You Won. \nYour Number: {user}\nGuess Number: {guess_number}")
        return True
    else:
        print(f"You Lose. \nYour Number: {user}\nGuess Number: {guess_number}")
        return False

while True:
    if random_number_guess_game() == True:
        break