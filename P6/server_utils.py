from Seq1 import Seq
import jinja2
import pathlib


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


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


def get(list_sequences, seq_number):
    sequence = list_sequences[int(seq_number)]
    context = {
        "number_sequence": seq_number,
        "sequence": sequence
    }
    contents = read_template_html_file("./html/get.html").render(context=context)
    return contents


def info(seq, opt):
    sequence = Seq(seq)
    percentage = Seq.percentage(sequence)
    operation = opt
    context = {
        "sequence": sequence,
        "operation": operation,
        "result": percentage
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def comp(seq, opt):
    sequence = Seq(seq)
    new_sequence = Seq.complement(sequence)
    operation = opt
    context = {
        "sequence": sequence,
        "operation": operation,
        "result": new_sequence
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def rev(seq, opt):
    sequence = Seq(seq)
    new_sequence = Seq.reverse(sequence)
    operation = opt
    context = {
        "sequence": sequence,
        "operation": operation,
        "result": new_sequence
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def gene(gene_name):
    folder = "./sequences/"
    sequence = Seq()
    sequence.seq_read_fasta(folder + gene_name + ".txt")
    context = {
        "gene_name": gene_name,
        "gene_contents": sequence.strbases
    }
    contents = read_template_html_file("./html/gene.html").render(context=context)
    return contents
