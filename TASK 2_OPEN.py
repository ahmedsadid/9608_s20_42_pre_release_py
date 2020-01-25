""" 9608_s20_PM SOLUTION
    ~ ZUBAYER AHMED SADID ~ """
#=====================================================================================================

##  T A S K 2.3
 
# listLen  : INTEGER
# cust     : STRING
# x , i, v : INTEGER
 
 
listLen = int(input("Length of table : "))
 
def Hash(cust):
    x = ""
    for i,v in enumerate(cust):
        if i<2: x += str(ord(v))
        else:   x += str(v)
             
    return ((int(x)-65650001)%listLen)
 
#testing#
#Hash("ZZ9999")
 
 
 
#=====================================================================================================
 
 
 
##  T A S K 2.4
 
# HashTab : ARRAY[0:listLen] of STRING
# filled  : BOOLEAN
# hashed  : INTEGER
# index   : INTEGER
 
 
HashTab = [""]*listLen
 
 
def insert(id):
    filled = False
    hashed = Hash(id)
    index = hashed
 
    while not filled and HashTab[index]!="":
        index += 1
        if index>(listLen-1):
            index = 0
 
        if index == hashed:
            filled = True
 
    if not filled:
        HashTab[index]=id
    else:
        print("ERROR : Table is full")
 
############################(unnecesarry)################################
def Gen():
    import random
    x = ""
    for i in range(6):
        if i<2:  x = x + chr(random.randrange(65,90))
        else  :  x = x + str(random.randrange(0,9))
 
    return x
############################(^unnecesarry^)###############################
 
def foo():
    for i in range(10):
        insert(Gen())
         
    #print(HashTab)
 
#testing#
def bar():
    insert("AA0001")
    insert("BB0100")
    insert("ZZ9999")
    print(HashTab)
 
 
 
#=====================================================================================================
 
 
 
##  T A S K 2.6

# end       : BOOLEAN
# ind       : INTEGER
# ind1      : INTEGER
# searchID  : STRING

 
def Search(searchID):
    ind1 = Hash(searchID)
    ind = ind1
    end = False
 
    while not end and HashTab[ind]!=searchID:
        ind += 1
        if ind>(listLen-1):
            ind = 0
 
        if ind == ind1:
            end = True
             
    if not end:
        print("The location is : ",ind)
    else:
        print("ID not found!")
 
 
 
#=====================================================================================================
 
 
##  T A S K 2.7

"""
Search("BB0100")   #positive
Search("AA0001")   #positive
Search("XX1111")   #negative
"""
 
 
#=====================================================================================================