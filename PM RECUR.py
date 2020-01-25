def outChars(inStr):
    L = len(inStr)
    
    if L == 1:
        print(inStr)
    else:
        print(inStr[0])
        inStr = inStr[-(L-1):]
        outChars(inStr)


outChars("example")