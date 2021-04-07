def print_coloured(message, color):
    import termcolor
    """import colorama
    colorama.init(strip="False")"""
    termcolor.colored(message, color)


def format_command(command):
    return command.replace("\n", "").replace("\r", "")


def ping():
    print_coloured("PING command!", "green")
