print("Dec2bin")
# Converting decimal to binary, octal and Hexadecimal by taking user input.
# Select input [1] for binary, [2] for octal, [3] for Hexadecimal.

decimal = int(input("Enter Decimal Value: \n"))
convert = int(input("Convert to: [1] Binary, [2] Octal, [3] Hexadecimal: \n"))

# if...elif ... else... function
if convert ==1: 
    print("Converted to Binary \n", bin(decimal))
elif convert ==2:
    print("Converted to Octal \n", oct(decimal))
elif convert ==3:
    print("Convert to Hexadecimal \n", hex(decimal))
else:
    print("Please Review Your Input")
