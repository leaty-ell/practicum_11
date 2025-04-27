with open("input.txt", "r", encoding="utf-8") as input_file:
    lines = input_file.readlines()

result_word = ''.join(line[0] for line in lines if line)

with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(result_word)

        
