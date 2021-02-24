from pathlib import Path

def seq_ping():
    print("OK")

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    print(sequence)

a, c, g, t = 0, 0, 0, 0
for ch in U5_seq:
    if ch == "A":
        a += 1
    elif ch == "C":
        c += 1
    elif ch == "G":
        g += 1
    elif ch == "T":
        t += 1