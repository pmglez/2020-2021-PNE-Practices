import requests
import sys
import jinja2
import pathlib

SERVER = "http://rest.ensembl.org"


def read_template_html_file(filename):
    content = jinja2.Template(pathlib.Path(filename).read_text())
    return content


def list_species(limit_species):
    ext = "/info/species?"
    r = requests.get(SERVER + ext, headers={"Content-Type": "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    decoded = r.json()
    s = decoded["species"]

    LIST_NAMES = []
    for e in s:
        name = e['common_name']
        LIST_NAMES.append(name)
    limit_list = LIST_NAMES[:int(limit_species)]
    context = {
        "total_length": len(LIST_NAMES),
        "limit": limit_species,
        "listSpecies": limit_list
    }
    contents = read_template_html_file("./html/listSpecies.html").render(context=context)
    return contents


def information_karyotype(specie):
    r = requests.get(SERVER + "/info/assembly/" + specie + "?", headers={"Content-Type": "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    decoded = r.json()
    s = decoded['karyotype']
    context = {
        "karyotype": s
    }
    contents = read_template_html_file("./html/karyotype.html").render(context=context)
    return contents


def chromosome_length(specie):
    r = requests.get(SERVER + "/info/assembly/" + specie + "?", headers={"Content-Type": "application/json"})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    decoded = r.json()
    s = decoded["top_level_region"]
    for i in s:
        if i["coord_system"] == "chromosome":
            s_dict = {
                i["name"]: i["length"]
            }
            print(s_dict)
    contents = read_template_html_file("./html/karyotype.html").render(context=context)
    return contents


server = "https://rest.ensembl.org"
ext = "/info/assembly/human?"

r = requests.get(server + ext, headers={"Content-Type": "application/json"})
if not r.ok:
    r.raise_for_status()
    sys.exit()
decoded = r.json()
s = decoded["top_level_region"]
s_dict = {}
for i in s:
    if i["coord_system"] == "chromosome":
        s_dict = {
            i["name"]: i["length"]
        }
        print(s_dict)