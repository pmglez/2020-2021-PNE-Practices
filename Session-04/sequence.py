from pathlib import Path

FILENAME = "ADA.txt"

file_contents = Path(FILENAME).read_text()
seq = file_contents[file_contents.find("\n") + 1:].replace("\n", "")

print("The total number of bases is: ", len(seq))
