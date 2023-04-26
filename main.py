denary = int(input("Number: "))
sizeOfInt = 256
binary = ""
for i in range(0,sizeOfInt):
    exponent = (sizeOfInt -1) - i
    number = 2**exponent
    result = denary - number
    if result >= 0:
        binary += "1"
        denary = result
    else:
        binary += "0"
print(binary)
