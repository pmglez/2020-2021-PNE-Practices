from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE}|-----")

IP = "192.168.8.212"
PORT = 12000

c = Client(IP, PORT)
c.talk("Message")

# Other ways of doing it

"""response = c.talk("Message")
   print("Response:", response)

   print("Response:", c.talk("Message"))"""
