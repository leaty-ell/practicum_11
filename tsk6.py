try:
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    if len(lines) < 1:
        raise ValueError("Файл пуст.")

    string = lines[0].strip()

    try:
        N = int(string)
    except ValueError:
        with open("output.txt", "w") as output_file:
            output_file.write("ERROR")
        exit()

    if len(lines) - 1 == N:
        result = "YES"
    else:
        result = "NO"

except Exception as e:
    result = "ERROR"

with open("output.txt", "w") as output_file:
    output_file.write(result)
