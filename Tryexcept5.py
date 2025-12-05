try:
    x=-1
    if x < 0:
        raise NameError("Sorry, no numbers below zero")
except NameError as e:
    print(e)