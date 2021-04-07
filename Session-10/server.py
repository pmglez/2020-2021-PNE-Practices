import socket

# Configure the Server's IP and PORT
PORT = 8082
IP = "192.168.8.212"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

count_connections = 0
client_address_list = []
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        client_address_list.append((client_ip_port))
        count_connections += 1
        print("Connection " + str(count_connections) + ". Client IP, PORT: " + str(client_ip_port))

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-readable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Message received: {msg}")

        # -- Send a response message to the client
        response = int(msg) ** int(msg)

        # -- The message has to be encoded into bytes
        cs.send("We need a number".encode())

        # -- Close the socket
        cs.close()

        if count_connections == 5:
            for i in range(0, len(client_address_list)):
                print("Client " + str(i) + ": Client IP, PORT: " + str(client_address_list[i]))
            exit(0)
