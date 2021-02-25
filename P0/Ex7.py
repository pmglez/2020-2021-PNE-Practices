import Seq0

folder = "./sequences/"

file = "U5.txt"

print("-----| Exercise 7 |------")
print("Gene U5:")

U5_seq = Seq0.seq_read_fasta(folder + file)
U5_complement_seq = Seq0.seq_complement(U5_seq)
print("Frag:", U5_seq[0:20])
print("Comp:", U5_complement_seq[0:20])
