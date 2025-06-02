def perform_operation(num1, num2, operation):
    match operation:
        case 'subtract':
            return num1 - num2
        case 'add':
            return num1 + num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                return"Error: Division by zero."
        case _:
            return "Invalid Operation!"

