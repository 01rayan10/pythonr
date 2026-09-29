n = int(input("Your number: "))
i = n
while i > 1:
    if n % i != 0:
        i -= 1
    else:
        print(f"{n} is a prime number")
        break
