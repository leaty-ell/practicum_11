with open('input1.txt', 'r') as input_file:
    current_date_str = input_file.readline().strip()
    n = int(input_file.readline().strip())
    
    current_day, current_month = map(int, current_date_str.split('.'))
    
    cells = []
    
    for _ in range(n):
        line = input_file.readline().strip()
        cell_number, baggage_date_str = line.split()
        cell_number = int(cell_number)
        
        baggage_day, baggage_month = map(int, baggage_date_str.split('.'))
        
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        total_current_days = sum(days_in_month[:current_month]) + current_day
        total_baggage_days = sum(days_in_month[:baggage_month]) + baggage_day
        
        if total_current_days - total_baggage_days > 3:
            cells.append(cell_number)

with open('output.txt', 'w') as file:
    for cell_number in cells:
        file.write(f"{cell_number}\n")
