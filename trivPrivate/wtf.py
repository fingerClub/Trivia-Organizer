import pdfplumber
path = "../../../../Downloads/1.3.24.pdf"
write = "trivia.txt"
with open(write, "w") as file:
    rules = [
             "Let’s get into the rules for today",
             "At live prize trivia we have one answer per table," \  
             "with no help from cellphones, iPads, or any electronics that ",
             "could help you get an edge in this competition. answers are" \ 
             "final once you turn them in.",
             "",
             "If you look at our trivia sheet, you will notice we have two" \ 
             "halves with 3 rounds each . Each round has three ",
             "categories with three different questions. In each round" \
             "we have three different point differentials that you",
             'can wager 1, 3, and 5 with each one only allowed to be used once.' \
             'In the second half, these differentials', 
             'are increased by 1, meaning you can wager 2, 4, or 6 in that half.',
             "",
             "We have a special halftime question and a Final question. But I will" \
             "get to those when we encounter them. ",
             "There is a Daily double! I will announce the daily double when I announce the" \
             "categories of that round and ",
             "I’ll explain the rules when we encounter that. Alright everyone let’s" \
             "get started. If have been playing for a ",
             'long time and notice I have made a mistake, please be eager to let me' \
             "know and as soon as possible.',
             "",
             "For our questions, I like to give song hints. these may be tied to a" \
             "lyric in the song, the artist's name",
             "or something related to the content of the question. Some song" \ 
             "hints may be hard, and some may be easy.",
             "It is all dependent on if I can find a good hint for the corresponding" \ 
             "question.",
             "okay, let's get started!",
             ""
            ]
             for x in rules:
                file.write(x)
    with pdfplumber.open(path) as pdf:
        content = {
                "category" : [],
                "stuff0fLegend" : []
        }
        sayings = {
                "half" : ["HALF TIME QUESTION", "For the half time question, it is a four part answer,", "I do not give  song hints for this one. Each answer you get", "right, I will grant you 2 points.", ""],
                "final" : ["Alright guys it’s time for the final question.", "Here you can wager 0 to 15 points it is all or ", "nothing question and what you have to do is:"]
        }
        page = pdf.pages[0]
        text = page.extract_table()
        for i in range(2, len(text)):
            row = text[i]
            for j in range(0, len(row)):
                if row[j].isupper() == True and row[j] and row[j] != "TIE" and row[j] != "EXTRA":
                    ringer["category"].append(row[j])
                    ringer["stuff0fLegend"].append(row[j])
                elif: j == len(row) - 1:
                    ringer["stuff0fLegend"] += [row[j], ""]
                else:
                    ringer["stuff0fLegend"].append(row[j])
        jumper = 0
        quParser = 0
        for key in content:
            for i in range(jumper, jumper + 3):
                words = key[i]
                if words == "HALF":
                    for half in sayings["HALF"]:
                        file.write(half)
                    jumper += 1
                    break

                elif words == "FINAL":
                file.write(words)
                else:
                    file.write(words)
            for i in range(quParser, quParser + 15)
                words = key[i]
                
                file.write(words)
