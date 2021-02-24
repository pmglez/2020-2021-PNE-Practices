import Seq0

folder = "./sequences/"
# FOLDER = "../Session-04/"
file = "U5.txt"

U5_seq = Seq0.seq_read_fasta(folder + file)     # directory (Path to that folder)
print("DNA file:", file)
print("The first 20 bases are:\n" + U5_seq[0:20])

# U05_seq = Seq0.seq_read_fasta(FOLDER + file)
# print("The first 20 bases are:\n" + U05_seq[0:20])
