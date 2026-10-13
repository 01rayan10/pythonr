def comp(a ,b):
    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} es igual a {b}")

a = int(input("1er número:  "))

comp(a ,10)