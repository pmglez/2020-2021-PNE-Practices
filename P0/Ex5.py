import Seq0

folder = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 5 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(folder + gene + ".txt")
    print("Gene", gene, ":", Seq0.seq_count(sequence))
