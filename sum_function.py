# You need to create a sum function that takes two numbers as input to the function and add the first number to the second number.
def sum_function(num1, num2):
    return num1 + num2


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))


result = sum_function(first_number, second_number)
print(result)
