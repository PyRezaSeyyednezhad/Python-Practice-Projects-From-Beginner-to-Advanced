""" Write a function that takes a user's name and prints it. If no name is given, print "Guest" instead. """
def introducing(user_name="Guest"):
    print(f"Hello {user_name}, Welcome to My Channel.")

introducing("Reza") # Hello Reza, Welcome to My Channel.
introducing() # Hello Guest, Welcome to My Channel.

""" Create a function that raises a number to a given power. If the power is not provided, use 2 as the default value. """
def number_power(base, power=2):
    print(base ** power)

number_power(2,5) # 32
number_power(5) # 25


""" Design a function that greets based on the time of day (morning, afternoon, or evening). If no time is given, use "morning" as the default. """
def get_time(hour=6):
    GoodMorning = [5,6,7,8,9,10]
    GoodAfternoon = [11,12,13,14,15]
    GoodEvening = [16,17,18,19,20]
    GoodNight = [21,22,23]
    GoodMidNight = [0,1,2,3,4]
    if hour in GoodMorning:
        print("Good Morning.")
    elif hour in GoodAfternoon:
        print("Good Afternoon.")
    elif hour in GoodEvening:
        print("Good Evening.")
    elif hour in GoodNight:
        print("Good Night.")
    elif hour in GoodMidNight:
        print("Good Mid Night.")
    else:
        print("Good Time. :)")

get_time(5)
get_time(8)
get_time(12)
get_time(19)
get_time(45)
get_time()
get_time(2)


"""
Write a function that calculates the sum of three numbers, where the third number is optional (default value is 0).
"""
"""
Write a function that converts temperature between Celsius and Fahrenheit. The target unit should be optional.

"""