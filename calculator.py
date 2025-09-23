import math

num = float(input("Enter a number: "))

binary_int= [] ## LIST TO STORE INTEGER BINARY VALUES
binary_decimal= [] ## LIST TO STORE DECIMAL BINARY VALUES

decimal = num - math.floor(num) ## 5.75 - 5 = 0.75
integer = math.floor(num) ## 5

# SINAL
if num > 0:
    sinal = 0 ## POSITIVE
else:
    sinal = 1 ## NEGATIVE

## BINARY FOR INTEGER PART
while integer > 1:
    rest_of_integer = integer % 2
    result_of_integer = integer // 2
    integer = result_of_integer
    binary_int.append(rest_of_integer)
binary_int.append(integer)

binary_int.reverse() ## REPLACE THE LIST TO GET THE RIGHT ORDER

## BINARY FOR DECIMAL PART
count = 0
while decimal != 0 and count < 5: ## LIMIT TO 5 DECIMAL PLACES
    result_of_decimal = decimal * 2
    if result_of_decimal >= 1:
        binary_decimal.append(1)
        decimal = result_of_decimal - 1
    else:
        binary_decimal.append(0)
        decimal = result_of_decimal
    count += 1

## BINARY FOR STRING
binary_str = ''.join(str(bit) for bit in binary_int) + '.' + ''.join(str(bit) for bit in binary_decimal)

## NORMALIZE THE NUMBER.   ## FORMAT IEEE 754 -> 1.xxxxx * 2^E
binary_str = binary_str.replace('.', '')  ## REMOVE THE DOT
binary_str = '1.' + binary_str[1:] ## ADD THE DOT AFTER THE FIRST 1
exponent_real = math.floor(math.log2(num))  ## REAL EXPONENT
ieee = binary_str + ' * 2^' + str(exponent_real) ## IEEE 754 FORMAT

## EXPONENTIAL BIAS
bias = 127
exponent_biased = exponent_real + bias
exponent= [] ## LIST TO STORE EXPONENT BINARY VALUES
while exponent_biased > 1:
    rest_of_exponent = exponent_biased % 2
    result_of_exponent = exponent_biased // 2
    exponent_biased = result_of_exponent
    exponent.append(rest_of_exponent)
exponent.append(exponent_biased)
exponent.reverse() ## REPLACE THE LIST TO GET THE RIGHT ORDER

## EXPONENT BINARY STRING
exponent_str = ''.join(str(bit) for bit in exponent)

## MANTISSA (23 BITS)
mantissa = binary_str[2:] ## REMOVE '1.'
if len(mantissa) < 23:
    mantissa = mantissa + '0' * (23 - len(mantissa)) ## ADD ZEROS TO THE RIGHT
else:
    mantissa = mantissa[:23] ## LIMIT TO 23 BITS

## FINAL OUTPUT
ieee32 = f"{sinal} {exponent_str} {mantissa}"
print(ieee32)

