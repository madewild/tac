"""Convert newlines into spaces"""

import re

infile = "data/all.txt"
outfile = "data/oneliner.txt"

with open(outfile, 'w', encoding="utf-8") as output:
    with open(infile, encoding="utf-8", errors="backslashreplace") as f:
        for line in f:
            newline = line.replace("\r", "")
            newline = newline.replace("\n", "")
            newline = re.sub(" +", " ", newline)
            if not newline.endswith(" "):
                newline += " "
            output.write(newline)
