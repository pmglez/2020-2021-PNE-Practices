from Seq01 import Seq, generate_seqs
import termcolor

seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

termcolor.cprint("List 1:", "blue")
Seq.print_seqs_blue(seq_list1)

termcolor.cprint("List 2:", "green")
Seq.print_seqs_green(seq_list2)
