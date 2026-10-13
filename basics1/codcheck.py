def rev_alphabet(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letras = list(alphabet)
    rev = []
        
    pos = 0
    while len(rev) < 26:
        pos = (pos - n - 1) % len(letras)
        rev.append(letras[pos])
        letras.pop(pos)
    return "".join(rev)
print(rev_alphabet(5))