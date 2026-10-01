while True:
   
    while True:
        try:
            raw = input("Enter results (separated by spaces): ").strip()
            results = [float(x) for x in raw.split()] if raw else []
            if not results:
                print("You must enter at least one result. Try again.\n")
                continue
            break
        except ValueError:
            print("Error: please enter only numbers for results (e.g. 10 9 8.5). Try again.\n")

    while True:
        try:
            raw = input("Enter coefficients (whole integers, separated by spaces): ").strip()
            coeffs_raw = [float(x) for x in raw.split()] if raw else []
            if not coeffs_raw:
                print("You must enter at least one coefficient. Try again.\n")
                continue

            coeffs = []
            bad = False
            for v in coeffs_raw:
                if not v.is_integer(): 
                    print(f"Invalid coefficient '{v}': coefficients must be whole integers (e.g. 3 or 3.0). Try again.\n")
                    bad = True
                    break
                coeffs.append(int(v)) 
            if bad:
                continue

            break
        except ValueError:
            print("Error: please enter only numbers for coefficients (e.g. 5 3 2). Try again.\n")

    if len(results) != len(coeffs):
        print("Error: number of results and coefficients must be the same. Please enter both again.\n")
        continue

    if sum(coeffs) == 0:
        print("Error: sum of coefficients is zero (would cause division by zero). Please re-enter coefficients.\n")
        continue

    total = sum(r * c for r, c in zip(results, coeffs))
    average = total / sum(coeffs)
    print(f"Your average is: {average:.4f}")
    break