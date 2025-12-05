try:
    print(10/0)
except NameError:
    print("Variable x is not defined.")
except:
    print("An unexpected error occurred.")