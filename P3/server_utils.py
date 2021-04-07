def print_coloured(message, color):
    import termcolor
    """import colorama
    colorama.init(strip="False")"""
    print(termcolor.colored(message, color))


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def ping(cs):
    print_coloured("PING command!", "green")
    response = "OK!"
    cs.send(str(response).encode())


def get(cs, list_sequences, argument):
    print_coloured("GET", "green")
    response = list_sequences[int(argument)]
    print(response)
    cs.send(str(response).encode())
