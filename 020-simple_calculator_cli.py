def simple_calculator_cli():
    userInput = str(input("Enter Equation to solve: "))
    try:
        print(f"{userInput} = {eval(userInput)}")
    except:
        print("!!! Something Went Wrong. The Wrong Valid !!!")


simple_calculator_cli()