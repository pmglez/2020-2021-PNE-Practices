from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text()
file_contents = file_contents.split("\n")
head = file_contents[0]

print("First line of the RNU6_269P.txt file:\n" + head)
