name = ["RAYAN", "REHAM"]
age = [16, 18]
for nm, age in zip(name, age):
    print(nm, "has", age, "years")
matieres = ["Maths", "Physics", "Tecno", "English"]
notes = [7, 8, 7.5, 9.5]
for i, notes in zip(matieres, notes):
    print(i, ": ", notes)
result = (7*5 + 8*5 + 7.5*5 + 9.5*2.5)/(5+5+5+2.5) 
print("Final result = ", result)