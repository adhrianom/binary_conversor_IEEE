import math

## FUNCTIONS
    



num = float(input("Enter a number: "))

binary_int= [] ## LIST TO STORE INTEGER BINARY VALUES
binary_decimal= [] ## LIST TO STORE DECIMAL BINARY VALUES

decimal = num - math.floor(num)
integer = math.floor(num)


while integer > 1:
    for i in range(integer):
        if integer >= 1:
            rest_of_integer = integer % 2 ## 1
            result_of_integer = integer // 2 ## 2.5
            integer = math.floor(result_of_integer)
            binary_int.append(rest_of_integer)

while decimal < 1:
    for i in range(decimal):
        if decimal != 1:
            result_of_decimal = decimal * 2 ## 1.5
            rest_of_decimal = math.floor(result_of_decimal) - result_of_decimal ## 0.5
            binary_decimal.append(rest_of_decimal)

for binary_int in binary_int:
    print(binary_int, end="")

for binary_decimal in binary_decimal:
    print(binary_decimal, end="")
