from Seq1 import Seq


def print_result(num, sequence):
    print("Sequence " + str(num) + ": ( Length: " + str(sequence.len()) + " ) " + str(sequence))
    a, c, g, t = sequence.count_bases()
    print("A: " + str(a) + ", C: " + str(c) + ", G: " + str(g) + ", T: " + str(t))


print("-----| Practice 1, Exercise 5 |------")

# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_seq = [s1, s2, s3]

for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])
