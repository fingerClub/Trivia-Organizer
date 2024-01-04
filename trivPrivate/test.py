import pdfplumber
path = "../../../../Downloads/1.3.24.pdf"
with pdfplumber.open(path) as pdf:
    dictionary0fCum = {
        "category": [], 
        "round": [], 
        "question": [], 
        "answer": []
     }
    page = pdf.pages[0]
    text = page.extract_table()
    for i in range(0, len(text)):
        catList = []
        row = text[i]
        for j in range(0, len(row)):
            if "[" in row[j] and "R" in row[j] and "Q" in row[j] and "]" in row[j] and ("Q" + "u") not in row[j]:
                dictionary0fCum["round"].append(row[j])
                print(row[j])
            if row[j] != "FINAL" or row[j] != "HALF" or "TIE" or "EXTRA":
                for x in str(j):
                    if "?" in row[j]:
                        dictionary0fCum["question"].append(row[j])
                        print(row[j])
                    elif (ord(x) < 97 and ord(x) > 32) and (ord(x + 1) < 97 and ord(x + 1) > 32):
                        dictionary0fCum["category"].append(row[j])
                        print(row[j])
                        break
                    else:
                        dictionary0fCum["answer"].append(row[j])
                        print(row[j])
    print(dictionary0fCum["category"])
                
        

            
        

