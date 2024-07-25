#define a function to perform arthimatic calculations
def calculator(num1,num2,operator):
    if operator=='+':
        return num1+num2
    if operator=='-':
        return num1-num2
    if operator=='*':
        return num1*num2
    if operator=='/':
        if num2 != 0:
            return num1/num2
        else:
            return "Error: Division by zero"
#data should be entered by user
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
operator=input("Enter operator(+,-,*,/): ")
#calculations performed
result=calculator(num1,num2,operator)
#output
print(f"Result: {result}")