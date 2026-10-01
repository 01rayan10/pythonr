def check_number(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "0"
while True:
    try:
        x = int(input("Give me a number: "))
        if x == 0:
            print("your number is 0, umm.. its not a positive number neither a negative one...")
        else:
            print(f"{x} is a {check_number(x)} number.")
        break
    except:
        print("Incorrect input. Please type an integer (a real number).")     