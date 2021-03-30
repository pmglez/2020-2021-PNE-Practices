from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE}|-----")

IP = "127.0.0.1"
PORT = 12000
PORT_2 = 12300

c = Client(IP, PORT)
c_2 = Client(IP, PORT_2)

s = Seq()
s.seq_read_fasta("../P0/Sequences/FRAT1.txt")

count = 0
i = 0
while i < len(s.strbases) and count < 5:
    fragment = s.strbases[i:i+10]
    count += 1
    i += 10
    print("Fragment", count, ":", fragment)
    if count % 2 == 0:
        print(c_2.talk("Fragment" + str(count) + ": " + fragment))
    else:
        print(c.talk("Fragment" + str(count) + ": " + fragment))
