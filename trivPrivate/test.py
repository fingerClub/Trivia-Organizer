import pdfplumber
import re
from strings import rules, sayings
form = r"\[R\s+\d+\s+Q\s+\d+\]"
path = "../../../../../Downloads/1.3.24.pdf"
write = "trivia.txt"
with open(write, "w") as file:
    for x in rules:
        file.write(x + "\n")
    with pdfplumber.open(path) as pdf:
        content = {
                "category" : [],
                "rowContent" : []
        }
        page = pdf.pages[0]
        text = page.extract_table()
        for i in range(2, len(text)):
            row = text[i]
            for j in range(0, len(row)):
                if row[j].isupper() == True and not re.match(form, row[j]) and row[j] != "TIE" and row[j] != "EXTRA":
                    content["category"].append(row[j])
                    content["rowContent"].append(row[j])
                elif j == len(row) - 1:
                    content["rowContent"] += [row[j], ""]
                else:
                    content["rowContent"].append(row[j])
        switch1 = False
        switch2 = False
        jumper = 0
        quParser = 0
        while switch2 == False:
            for key in content:
                llaves = content[key]
                if switch1 == False:
                    words = []
                    for i in range(jumper, jumper + 3):
                        words = llaves[i]
                        if words == "HALF":
                            file.write(words + "\n")
                            break
                        else:
                            file.write(words + "\n")
                    switch1 = True
                    if jumper > 18:
                            switch2 = True
                    elif words == "HALF":
                        jumper += 1
                    else:
                        jumper += 3
                    print(jumper)
                else:
                    words = []
                    for i in range(quParser, quParser + 15):
                        words = llaves[i]
                        if words == "HALF":
                            for half in sayings["half"]:
                                file.write(half + "\n")
                            for j in range(i, i + 4):
                                file.write(llaves[j] + "\n")
                            break
                        elif words == "FINAL":
                            for x in sayings["final"]:
                                file.write(x + "\n")
                            for j in range(i, i + 4):
                                file.write(llaves[j] + "\n")
                            break
                        else:
                            file.write(words + "\n")
                    if words in ("HALF", "FINAL"):
                        quParser += 4
                    else:
                        quParser += 15
                    switch1 = False
        print(content["rowContent"])
