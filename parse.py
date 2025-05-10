global file 
with open("text.txt", "r", encoding="utf-8") as f:
    file = f.read()

print(file.replace("\n", "<br>").replace('"', "\\\""))