def main():
    #prompt for arithmatic expression
    expression = input("Enter Expression: ")

    #split expression & assign into variables (x is first integer, y is operation, z is second integer)
    x, y, z = expression.split(" ")

    #may be unecessary, but makes sure values are integers instead of strings.
    num1 = int(x)
    operator = (y) #aside from this, which doesn't need it
    num2 = int(z)

    #calculate expression & store result in "result" variable
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    #print result as float to 1 decimal point
    print(f"{result:.1f}")

main()
