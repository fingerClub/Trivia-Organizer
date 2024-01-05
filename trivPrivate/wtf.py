#pdfplumber is a module used to extract pdf data
import pdfplumber
import re
from strings import rules, sayings
form = r"\[R\s+\d+\s+Q\s+\d+\]"
#path to pdf
path = "../../../../../Downloads/1.3.24.pdf"
#trivia document to write on
write = "trivia.txt"
#opening .txt file to write
with open(write, "w") as file:
    #part of script, made into list to print each string as a line on .txt file for readability
    #write script onto .txt file
    for x in rules:
        file.write(x + "\n")
    #opening pdf with pdfplumber
    with pdfplumber.open(path) as pdf:
        #content and sayings are string dictionaries to hold categories and PDF
        content = {
                "category" : [],
                "rowContent" : []
        }
        page = pdf.pages[0]
        text = page.extract_table()
        #append categories and row content in dicitonary lists, loop through each row
        for i in range(2, len(text)):
            row = text[i]
            #loop through each cell in row
            for j in range(0, len(row)):
            #if statements decide where to append each cell in its proper list
                #first if appends categories to "category" and also appends categories to "rowContent"
                #so category can be also written when writing rows onto .txt file
                #to be appended to "category", the string in the cell must be in all caps.
                if row[j].isupper() == True and not re.match(form, row[j]) and row[j] != "TIE" and row[j] != "EXTRA":
                    content["category"].append(row[j])
                    content["rowContent"].append(row[j])
                #elif checks if j loop has reached end of row, and adds a space
                elif j == len(row) - 1:
                    content["rowContent"] += [row[j], ""]
                else:
                    content["rowContent"].append(row[j])
        switch1 = False
        switch2 = False
        jumper = 0
        quParser = 0
        #loops through "category" and "rowContent"
        while switch2 == False:
            for key in content:
                llaves = content[key]
                #jumper is used to print only the three categories for each round
                if switch1 == False:
                    for i in range(jumper, jumper + 3):
                        words = llaves[i]
                        #if the string is is equal to half 
                        if words == "HALF":
                            for half in sayings["half"]:
                                file.write(half + "\n")
                            switch1 = True
                            jumper += 1
                        elif jumper > 18:
                            switch2 = True
                        else:
                            file.write(words + "\n")
                            switch1 = True
                        jumper += 3             
                else:
                    for i in range(quParser, quParser + 11):
                        words = llaves[i]
                        if words == "HALF":
                            for j in range(i, i + 4):
                                file.write(llaves[j] + "\n")
                            quParser += 4
                        elif words == "FINAL":
                            for x in sayings["final"]:
                                file.write(x + "\n")
                            for j in range(i, i + 4):
                                file.write(llaves[j] + "\n")
                            quParser += 4
                        else:
                            file.write(words + "\n")
                    switch1 = False
                    quParser += 11