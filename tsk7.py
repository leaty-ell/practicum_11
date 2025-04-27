with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

s = []

a = [int(x.strip()) for x in lines]

for num in a:
    if num!=100:
        s.append(str(num))

res = "\n".join(s)

with open("output.txt", "w") as output_file:
    output_file.write(res)
