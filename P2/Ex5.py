from Client0 import Client
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE}|-----")

IP = "192.168.8.212"
PORT = 12000

c = Client(IP, PORT)
print(c.talk("Sending the U5 Gene to the server..."))
print(c.talk(Path("../P0/Sequences/U5.txt").read_text()))
