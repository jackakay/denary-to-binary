def intToBin():
    denary = int(input("Number: "))
    sizeOfInt = 8
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
    return binary

def binToInt(newBin):
    newBin = newBin[::-1]
    newInt = 0
    
    #reversed
    for i in range(len(newBin)):
        if newBin[i] == "1":
           newInt += 2**i
    return newInt

def intToHex():
    sumOf1 = 0
    sumOf2 = 0
    string = []
    characters = ["a", "b", "c", "d", "e", "f"]
    binary = intToBin()
    if len(binary) % 2 == 0:
        sumOf1 = binToInt(binary[0:4])
        
        sumOf2 = binToInt(binary[4:8])
        
        if sumOf1 < 10:
            string.append(str(sumOf1))
            
        else:
            remainedOf1 = sumOf1 - 10
            char = characters[remainedOf1]
            string.append(char)
        if sumOf2 < 10:
            string.append(str(sumOf1))
            
        else:
            remainedOf1 = sumOf2 - 10
            char = characters[remainedOf1]
            string.append(char)
    return ' '.join(string)

print(intToHex())           
    
