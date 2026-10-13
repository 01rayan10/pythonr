def new_alphabet(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = list(alphabet)
    new = []
    
    pos = 0
    while len(new) < 26:
        pos = (pos + n - 1) % len(letras)
        new.append(letras[pos])
        letras.pop(pos)
    return "".join(new)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = input().split()
n1 = int(n[0])
if len(n) > 1:
    n2 = int(n[1])
if n1 != 0:
    texto = input()
    texto = texto.upper()
    text = list(texto)
    new_text = ""
    new_alphabet = list(new_alphabet(n1))
    for i in text:
        if i in alphabet:
            position = alphabet.find(i)
            new_text = new_text + new_alphabet[position]
        else:
            new_text = new_text + i
    new_text = new_text.replace(" ", "").replace(",", "").replace(".", "")
    print(new_text)
else:
    texto = input()
    texto = texto.upper()
    text = list(texto)
    new_text = ""
    new_alphabet = list(new_alphabet(n2))
    for i in text:
        if i in new_alphabet:
            position = new_alphabet.index(i)
            new_text = new_text + alphabet[position]
    print(new_text)