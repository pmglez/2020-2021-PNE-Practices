import Seq0

folder = "./sequences/"

file = "U5.txt"

print("-----| Exercise 6 |------")
print("Gene U5:")

U5_seq = Seq0.seq_read_fasta(folder + file)
U5_reverse_seq = Seq0.seq_reverse(U5_seq)
print("Frag:", U5_seq[0:20])
print("Rev :", U5_reverse_seq[-20:])
