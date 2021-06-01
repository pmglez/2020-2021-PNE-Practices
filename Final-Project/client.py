import http.client
import json
import termcolor
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
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
species = json.loads(data1)
species_limit = species["species"][0:10]

termcolor.cprint("LIST SPECIES:", "yellow")

for s in species_limit:
    termcolor.cprint("Name: ", 'blue', end="")
    print(s["name"])

print()
termcolor.cprint("------------------------------------------------------------------------------------------", "yellow")

try:
    conn.request("GET", "/karyotype?specie=human" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r2 = conn.getresponse()
print(f"Response received!: {r2.status} {r2.reason}\n")

data2 = r2.read().decode("utf-8")
information = json.loads(data2)
karyotype = information["karyotype"]

termcolor.cprint("LIST CHROMOSOMES:", "yellow")

for k in karyotype:
    termcolor.cprint("Chromosome: ", 'blue', end="")
    print(k)

print()
termcolor.cprint("------------------------------------------------------------------------------------------", "yellow")

try:
    conn.request("GET", "/chromosomeLength?specie=human&chromo=21" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r3 = conn.getresponse()
print(f"Response received!: {r3.status} {r3.reason}\n")

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

termcolor.cprint("LENGTH CHROMOSOME:", "yellow")

termcolor.cprint("Length: ", 'blue', end="")
print(info_dict["21"])

print()
termcolor.cprint("------------------------------------------------------------------------------------------", "yellow")

try:
    conn.request("GET", "/geneSeq?gene=FRAT1" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r4 = conn.getresponse()
print(f"Response received!: {r4.status} {r4.reason}\n")

data4 = r4.read().decode("utf-8")
information = json.loads(data4)
sequence = information["seq"]

termcolor.cprint("GENE SEQUENCE:", "yellow")

termcolor.cprint("Sequence: ", 'blue', end="")
print(sequence)

print()
termcolor.cprint("------------------------------------------------------------------------------------------", "yellow")

try:
    conn.request("GET", "/geneInfo?gene=FRAT1" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r5 = conn.getresponse()
print(f"Response received!: {r5.status} {r5.reason}\n")

data5 = r5.read().decode("utf-8")
information = json.loads(data5)
id = information["query"]
s = information["seq"]
s = Seq(s)
t_len = Seq.len(s)
description = information["desc"].split(":")

termcolor.cprint("INFORMATION:", "yellow")

termcolor.cprint("Start: ", "blue", end=""), print(description[3])
termcolor.cprint("End: ", "blue", end=""), print(description[4])
termcolor.cprint("Length: ", "blue", end=""), print(t_len)
termcolor.cprint("id: ", "blue", end=""), print(id)
termcolor.cprint("Chromosome: ", "blue", end=""), print(description[2])

print()
termcolor.cprint("------------------------------------------------------------------------------------------", "yellow")

try:
    conn.request("GET", "/geneCalc?gene=FRAT1" + JSON_PARAM)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

r6 = conn.getresponse()
print(f"Response received!: {r6.status} {r6.reason}\n")

data6 = r6.read().decode("utf-8")
information = json.loads(data6)
s = information["seq"]
s = Seq(s)
calculations = Seq.percentage(s)

termcolor.cprint("CALCULATIONS:", "yellow")

for l in calculations:
    m = l.split(":")
    termcolor.cprint(m[0] + ":", "blue", end="")
    print(m[1])
