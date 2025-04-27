with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

a = []
for line in lines:
    numbers = line.strip().split() 
    a.extend(int(num) for num in numbers)  

if len(a) >= 2 and a[1] != 0:
    res = a[0] / a[1] + a[2]
else:
    res = "Ошибка: недостаточно данных или деление на ноль"

with open("output.txt", "w") as output_file:
    output_file.write(str(res))
