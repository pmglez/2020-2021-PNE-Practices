from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE}|-----")

IP = "192.168.8.212"
PORT = 12000

c = Client(IP, PORT)
c.talk_colours("Message")
