def add(a, b):
    return a + b
numbers = [(1, 1), (1, 2), (5, 10), (100, 1000)]
for a, b in numbers:
    print(f"{a} + {b} = {add(a, b)}")
