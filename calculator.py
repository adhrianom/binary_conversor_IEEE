import math

## FUNCTIONS
    



num = float(input("Enter a number: "))

binary_int= [] ## LIST TO STORE INTEGER BINARY VALUES
binary_decimal= [] ## LIST TO STORE DECIMAL BINARY VALUES

decimal = num - math.floor(num) ## 5.75 - 5 = 0.75
integer = math.floor(num) ## 5

## BINARY FOR INTEGER PART
while integer > 1:
    for i in range(integer):
        if integer >= 1:
            rest_of_integer = integer % 2 ## 5 % 2 = 1 ; 2 % 2 = 0 ; 1 % 2 = 1
            result_of_integer = integer // 2 ## 2.5 ; 1.0 ; 0.5
            integer = math.floor(result_of_integer) ## 2 ; 1 ; 0
            binary_int.append(rest_of_integer) ## [1, 0, 1]

## BINARY FOR DECIMAL PART
while decimal > 0:
    for j in range(5): ## LIMIT TO 5 DECIMAL PLACES
        if decimal > 0:
            result_of_decimal = decimal * 2 ## 0.75 * 2 = 1.5 ; 0.5 * 2 = 1.0 ; 0.0 * 2 = 0.0
            if result_of_decimal >= 1:
                binary_decimal.append(1) ## [1, 1, 0]
                decimal = result_of_decimal - 1 ## 1.5 - 1 = 0.5 ; 1.0 - 1 = 0.0
            else:
                binary_decimal.append(0)
                decimal = result_of_decimal ## 0.5 ; 0.0


            


for binary_int in binary_int:
    print(binary_int, end="")

for binary_decimal in binary_decimal:
    print(binary_decimal, end="")
