def perform_operation(num1, num2, operation):
    # match operation:
    #     case 'subtract':
    #         return num1 - num2
    #     case 'add':
    #         return num1 + num2
    #     case 'multiply':
    #         return num1 * num2
    #     case 'divide':
    #         if num2 != 0:
    #             return num1 / num2
    #         else:
    #             return"Error: Division by zero."
    #     case _:
    #         return "Invalid Operation!"

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operation"