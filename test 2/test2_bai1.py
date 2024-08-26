def calculate_sum_from_string(input_string):
    total_sum = 0
    current_number = 0
    is_negative = False

    for char in input_string:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '-':
            is_negative = True
        else:
            # End of a number, add it to the total sum
            if current_number != 0:
                total_sum += current_number * (-1 if is_negative else 1)
                current_number = 0
                is_negative = False

    # Add the last number (if any)
    total_sum += current_number * (-1 if is_negative else 1)

    return total_sum

# Nhập chuỗi từ bàn phím
user_input = input("Nhập chuỗi ký tự: ")

# Tính tổng và in ra màn hình
result = calculate_sum_from_string(user_input)
print(f"Tổng các số trong chuỗi là: {result}")
