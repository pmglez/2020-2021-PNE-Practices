import Client0
c = Client0.Client("192.168.8.212", 8082)
for i in range(0, 5):
    c.talk("Message " + str(i))
