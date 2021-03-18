from Seq1 import Seq
print("-----| Practice 1, Exercise 10 |------")

folder = "../P0/Sequences/"
gene_list = ["U5", "ADA", "FRAT1", "FXN"]


def print_result():
    for gene in gene_list:
        sequence = Seq()
        sequence.seq_read_fasta(folder + gene + ".txt")
        max_base = sequence.most_frequent()
        print("Gene " + gene + ": Most frequent base: " + max_base)
        print("Bases:", sequence.count())


print_result()
