import sys
with open(sys.argv[1]) as data:
    lines = []
    for line in data.read().splitlines():
        lines.append(line.split("\t"))
    lines.sort()
number = 1
with open(sys.argv[2],"w") as output:
    for i in lines:
        if i[1] == "0":
            output.write(f"Massage {number}\n")
            number += 1
        for j in i:
            output.write(f"{j}\t")
        output.write("\n")

        