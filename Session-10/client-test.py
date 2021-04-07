import Client0
c = Client0.Client("192.168.8.212", 8088)
for i in range(0, 5):
    c.talk_colors("Message " + str(i))
