num1 = int(input ("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation ( +, -, *, /): ")

match operation:
    case "+":
        addition = int(num1 + num2)
        print("The result is ", addition, ".")
    case "-":
        subtract = int(num1 - num2)
        print("The result is ", subtract, ".")
    case "*":
        multiply = int(num1 * num2)
        print("The result is ", multiply, ".")
    case "/":
        if num2 == 0:
          print("Cannot divide by zero.")
        else:
          divide = int(num1 / num2)
          print("The result is ", divide, ".")
    case _:
        print("Invalid operation selection")

