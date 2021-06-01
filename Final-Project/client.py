import http.client
import json
import termcolor
# from ensembl_class import Ensembl
from Seq1 import Seq

PORT = 8080
SERVER = "localhost"
JSON_PARAM = "&json=1"

termcolor.cprint(f"\nConnecting to server: {SERVER}:{PORT}\n", "green")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)
# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)


try:
    conn.request("GET", "/listSpecies?limit=10" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {r1.status} {r1.reason}\n", "green")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
species = json.loads(data1)
species_limit = species["species"][0:10]

print("LIST SPECIES: ")
print()
for s in species_limit:
    termcolor.cprint("Name: ", 'blue', end="")
    print(s["name"])

print("----------------------------------------------------------------------------------------------------")

try:
    conn.request("GET", "/karyotype?specie=human" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r2 = conn.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {r2.status} {r2.reason}\n", "green")

# -- Read the response's body
data2 = r2.read().decode("utf-8")
information = json.loads(data2)
karyotype = information["karyotype"]

print("LIST CHROMOSOMES: ")
print()
for k in karyotype:
    termcolor.cprint("Chromosome: ", 'red', end="")
    print(k)

print("----------------------------------------------------------------------------------------------------")

try:
    conn.request("GET", "/chromosomeLength?specie=human&chromo=21" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r3 = conn.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {r3.status} {r3.reason}\n", "green")

# -- Read the response's body
data3 = r3.read().decode("utf-8")
information = json.loads(data3)
info = information["top_level_region"]
names = []
lengths = []
for i in info:
    if i["coord_system"] == "chromosome":
        names.append(i["name"])
        lengths.append(i["length"])
info_dict = dict(zip(names, lengths))

print("LENGTH CHROMOSOME: ")
print()
termcolor.cprint("Length: ", 'yellow', end="")
print(info_dict["21"])

print("----------------------------------------------------------------------------------------------------")

try:
    conn.request("GET", "/geneSeq?gene=FRAT1" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r4 = conn.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {r4.status} {r4.reason}\n", "green")

# -- Read the response's body
data4 = r4.read().decode("utf-8")
information = json.loads(data4)
sequence = information["seq"]
print("GENE SEQUENCE: ")
print()
termcolor.cprint("Sequence: ", 'blue', end="")
print(sequence)

print("----------------------------------------------------------------------------------------------------")

try:
    conn.request("GET", "/geneInfo?gene=FRAT1" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r5 = conn.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {r5.status} {r5.reason}\n", "green")

# -- Read the response's body
data5 = r5.read().decode("utf-8")
information = json.loads(data5)
id = information["query"]
s = information["seq"]
s = Seq(s)
t_len = Seq.len(s)
description = information["desc"].split(":")

print("INFORMATION: ")
print()
termcolor.cprint("Start: ", "red", end=""), print(description[3])
termcolor.cprint("End: ", "red", end=""), print(description[4])
termcolor.cprint("Length: ", "red", end=""), print(t_len)
termcolor.cprint("id: ", "red", end=""), print(id)
termcolor.cprint("Chromosome: ", "red", end=""), print(description[2])

print("----------------------------------------------------------------------------------------------------")

try:
    conn.request("GET", "/geneCalc?gene=FRAT1" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r6 = conn.getresponse()

# -- Print the status line
termcolor.cprint(f"Response received!: {r6.status} {r6.reason}\n", "green")

# -- Read the response's body
data6 = r6.read().decode("utf-8")
information = json.loads(data6)
s = information["seq"]
s = Seq(s)
calculations = Seq.percentage(s)

print("CALCULATIONS: ")
print()
for l in calculations:
    m = l.split(":")
    termcolor.cprint(m[0] + ":", "blue", end="")
    print(m[1])
