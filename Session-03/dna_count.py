def correct_sequence(dna):
    for ch in dna:
        if ch != "A" and ch != "C" and ch != "G" and ch != "T":
            return False
    return True

def count_bases(dna):
    a, c, g, t = 0, 0, 0, 0
    for ch in dna:
        if ch == "A":
            a += 1
        elif ch == "C":
            c += 1
        elif ch == "G":
            g += 1
        elif ch == "T":
            t += 1
    return a, c, g, t

dna = input("Introduce a sequence: ")
correct_dna = correct_sequence(dna)
if correct_dna:
    print("Total length: ", len(dna))
    a, c, g, t = count_bases(dna)
    print("A", a)
    print("C", c)
    print("G", g)
    print("T", t)
else:
    print("Not a valid DNA sequence")