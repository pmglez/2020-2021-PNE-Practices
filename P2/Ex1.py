from Client0 import Client      # cd P2 <<enter>> python Ex2.py
                                # for printing in the terminal

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE}|-----")

# IP always a string, Port always integer
IP = "127.0.0.1"
PORT = 12000
# IP always a string, Port always integer

c = Client(IP, PORT)

c.advanced_ping()
c.ping()

print(f"IP: {c.ip}, {c.port}")
