import Seq0

folder = "./Sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "G", "T"]

print("-----| Exercise 4 |------")
for gene in gene_list:
    sequence = Seq0.seq_read_fasta(folder + gene + ".txt")
    print("GENE", gene)
    for base in base_list:
        print(base + ":", Seq0.seq_count_base(sequence, base))
