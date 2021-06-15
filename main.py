import os

files = [file for file in os.listdir() if file.endswith(".txt")]

names = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        flag = False
        for line in f:
            if line.startswith("Sortiert nach Nachname:"):
                flag = True
            elif flag:
                names.append(line.strip("\n"))

names = list(set(names))

names = [name.split(" ")[-1] + ", " + " ".join(name.split(" ")[:-1]) for name in names]
names.sort()

for name in names:
    name = name.split(", ")
    print(name[1] + " " + name[0])
