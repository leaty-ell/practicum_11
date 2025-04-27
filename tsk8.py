with open("input.txt", "r") as input_file:
    steps = [int(line.strip()) for line in input_file.readlines()]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

monthly_averages = []

current_day = 0

for days in days_in_month:
    monthly_steps = sum(steps[current_day:current_day + days])
    average_steps = monthly_steps / days
    monthly_averages.append(average_steps)
    current_day += days

with open("output.txt", "w") as output_file:
    for average in monthly_averages:
        output_file.write(f"{average:.2f}\n") 

