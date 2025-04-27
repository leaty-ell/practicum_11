with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

with open('output.txt', 'w') as output_file:
    for line in lines:
        if line.startswith('A') or line.startswith('a'):
            output_file.write(line)
