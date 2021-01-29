def calculator(num1, num2, op_num):
    # op_num = 1: add, 2: deduct, 3: multiply, 4: devide, 5: remain
    if op_num == 1:
        return num1 + num2
    if op_num == 2:
        return num1 - num2
    if op_num == 3:
        return num1 * num2
    if op_num == 4:
        return num1 / num2
    if op_num == 5:
        return num1 % num2
    
    
input_num1 = int(input("Left number: "))
input_num2 = int(input("Right number: "))
op_num = int(input("Choose an operator, 1: add, 2: deduct, 3: multiply, 4: devide, 5: remain => "))
print(calculator(input_num1, input_num2, op_num))
