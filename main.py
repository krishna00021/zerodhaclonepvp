while True:
    try:
        a=int(input("Enter a number 1: "))
        b=int(input("Enter a number 2: "))
        print(f"The sum is: {a+b}")
    except:
        print("Please enter a valid number.")
