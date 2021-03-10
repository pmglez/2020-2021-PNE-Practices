import Seq1

print("-----| Practice 1, Exercise 6 |------")


def print_result(num, sequence):
    print("Sequence " + str(num) + ": ( Length: " + str(sequence.len()) + " ) " + str(sequence))
    print("Bases:", sequence.count())


# We create the test sequences
list_seq = list(Seq1.test_sequences())

for i in range(0, len(list_seq)):
    print_result(i, list_seq[i])
