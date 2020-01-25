# TASK 3.5
"""---  write a recursive algorithm that would output each letter in a string, from the
beginning, one at a time. The string is passed as a parameter --- """
# AUTHOR : ZUBAYER AHMED SADID

# inStr : STRING
# L     : INTEGER

def outChars(inStr):
    L = len(inStr)
    
    if L == 1:
        print(inStr)
    else:
        print(inStr[0])
        inStr = inStr[-(L-1):]
        outChars(inStr)

outChars("example")
