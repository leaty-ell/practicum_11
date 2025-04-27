with open("input1.txt", "r") as input_file:
    lines = input_file.readlines()

stroki = [x.strip() for x in lines]

ind = 0
a = []

for ind in range(len(stroki)):
    if ind%2!=0:
        a.append(stroki[ind])

with open("output.txt", "w") as output_file:
    output_file.write("\n".join(a))

