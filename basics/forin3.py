p = {"n" : "r", "a": 16, "c" : "ndr"}
for key in p:
    print(key, ":", p[key])
for value in p.values():
    print(value)
for key, value in p.items():
    print(key, ":", value)