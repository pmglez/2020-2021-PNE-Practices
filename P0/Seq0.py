from pathlib import Path


def seq_ping():
    print("OK")


def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")


def seq_read_fasta(filename):
    return take_out_first_line(Path(filename).read_text())


def seq_len(seq):
    return len(seq)


def seq_count_base(seq, base):
    return seq.count(base)


def seq_count(seq):                 # def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0             # gene_dict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for ch in seq:                      # for ch in seq:
        if ch == "A":                       # gene_dict[ch] += 1
            a += 1                      # return gene_dict
        elif ch == "C":
            c += 1
        elif ch == "G":
            g += 1
        elif ch == "T":
            t += 1
    return {"A": a, "C": c, "G": g, "T": t}


def seq_reverse(seq):
    seq_list = list(seq)
    reverse_list = seq_list[:: -1]
    reverse_seq = ("".join(reverse_list))
    return reverse_seq


def seq_complement(seq):
    gene_list = []
    for ch in seq:
        if ch == "A":
            ch = "T"
            gene_list.append(ch)
        elif ch == "C":
            ch = "G"
            gene_list.append(ch)
        elif ch == "G":
            ch = "C"
            gene_list.append(ch)
        elif ch == "T":
            ch = "A"
            gene_list.append(ch)
    complement_seq = ("".join(gene_list))
    return complement_seq


def seq_count_max_base(seq):
    gene_dict = seq_count(seq)
    max_base = max(gene_dict, key=gene_dict.get)
    return max_base
