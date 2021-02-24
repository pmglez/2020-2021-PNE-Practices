from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text()
body = file_contents[file_contents.find("\n") + 1:]

print("Body of the U5.txt file:\n" + body)
