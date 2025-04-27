with open("input.txt", "r", encoding='utf-8') as input_file:
    lines = input_file.readlines()

with open("output.txt", "w", encoding='utf-8') as output_file:
    for line in lines:
        if len(line)>20:
            output_file.write(line)
