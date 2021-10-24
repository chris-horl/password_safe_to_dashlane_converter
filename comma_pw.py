import csv

f = open("dashlane_import.csv", "w", newline='', encoding='utf-8')

with open("pw_safe_export.txt", "r") as file:
    lines = file.readlines()
    newlines = []
    for line in lines[1:]:
        values = line.strip().split("\t")
        newline = [values[0].split(".")[-1], values[3] if values[3] else 'http://a.b', values[1], values[2], values[21]]
        newlines.append(newline)
    writer = csv.writer(f)
    writer.writerow(["Name", "URL", "Username", "Password", "Note"])
    writer.writerows(newlines)
    f.close()