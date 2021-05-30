import requests
import sys
import jinja2
import pathlib
from Seq1 import Seq

SERVER = "http://rest.ensembl.org"

DICT_GENES = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


def read_request(endpoint, argument):
    r = requests.get(SERVER + endpoint + argument + "?", headers={"Content-Type": "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    decoded = r.json()
    return decoded


def list_species(limit_species):
    ext = "/info/species"
    decoded = read_request(ext, "")
    s = decoded["species"]
    list_names = []
    for e in s:
        name = e['common_name']
        list_names.append(name)
    limit_list = list_names[:int(limit_species)]
    context = {
        "total_length": len(list_names),
        "limit": limit_species,
        "listSpecies": limit_list
    }
    contents = read_template_html_file("./html/listSpecies.html").render(context=context)
    return contents


def information_karyotype(specie):
    ext = "/info/assembly/"
    decoded = read_request(ext, specie)
    s = decoded['karyotype']
    context = {
        "karyotype": s
    }
    contents = read_template_html_file("./html/karyotype.html").render(context=context)
    return contents


def chromosome_length(specie, chromosome):
    ext = "/info/assembly/"
    decoded = read_request(ext, specie)
    s = decoded["top_level_region"]
    keys = []
    values = []
    for i in s:
        if i["coord_system"] == "chromosome":
            keys.append(i["name"])
            values.append(i["length"])
    s_dict = dict(zip(keys, values))
    if chromosome in keys:
        length = s_dict[chromosome]
        context = {
            "length": length
        }
        contents = read_template_html_file("./html/chromosomeLength.html").render(context=context)
        return contents
    else:
        contents = read_template_html_file("./html/Error.html").render()
        return contents


def gene_seq(gene):
    ext = "/sequence/id/"
    if gene in DICT_GENES.keys():
        id = DICT_GENES[gene]
        decoded = read_request(ext, id)
        s = decoded["seq"]
        sequence = Seq(s)
        context = {
            "gene_name": gene,
            "gene_contents": sequence
        }
        contents = read_template_html_file("./html/geneSeq.html").render(context=context)
    else:
        contents = read_template_html_file("./html/Error.html").render()
    return contents


def gene_info(gene):
    ext = "/sequence/id/"
    if gene in DICT_GENES.keys():
        id = DICT_GENES[gene]
        decoded = read_request(ext, id)
        s = decoded["seq"]
        c = decoded["desc"].split(":")[2]
        start = decoded["desc"].split(":")[3]
        end = decoded["desc"].split(":")[4]
        sequence = Seq(s)
        t_length = Seq.len(sequence)
        context = {
            "gene_name": gene,
            "start": start,
            "end": end,
            "length": t_length,
            "id": id,
            "chromosome": c
        }
        contents = read_template_html_file("html/geneInfo.html").render(context=context)
    else:
        contents = read_template_html_file("./html/Error.html").render()
    return contents


def gene_calc(gene):
    ext = "/sequence/id/"
    if gene in DICT_GENES.keys():
        id = DICT_GENES[gene]
        decoded = read_request(ext, id)
        s = decoded["seq"]
        sequence = Seq(s)
        calc_seq = Seq.percentage(sequence)
        context = {
            "gene_name": gene,
            "information": calc_seq
        }
        contents = read_template_html_file("html/geneCalc.html").render(context=context)
    else:
        contents = read_template_html_file("./html/Error.html").render()
    return contents
