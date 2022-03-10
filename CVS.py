# Bonus homework 3.1

with open("people.cvs","r") as f:
    text=f.read()
    row_text=text.split("\n")

    for i in range(1,len(row_text)):
        line=row_text[i]
        element=line.split(",")
        print(element[0],"is",element[1],"years old and",element[2])
        print()
