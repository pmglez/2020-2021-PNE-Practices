from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")


def print_result(num, sequence):
    print("Sequence " + str(num) + ": ( Length: " + str(sequence.len()) + " ) " + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Comp:", sequence.complement())


folder = "../P0/Sequences/"
s1 = Seq()
s1.seq_read_fasta(folder + "U5.txt")

print_result("", s1)
