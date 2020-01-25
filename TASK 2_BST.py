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



class Node:
    def __init__(self, data):
        #   data :  STRING
        self.data = data
        self.left = None
        self.right = None

    def insert(self, inData):
        #   inData :  STRING
        if self.data != None:
            if inData < self.data:
                if self.left is None:
                    self.left = Node(inData)
                else:
                    self.left.insert(inData)
            elif inData > self.data:
                if self.right is None:
                    self.right = Node(inData)
                else:
                    self.right.insert(inData)          
        else:
            self.data = inData


    def find(self,sData):
        #   sData :  STRING
        if self.data == sData:
            return True
        elif sData < self.data and self.left:
            return self.left.find(sData)
        elif sData > self.data and self.right:
            return self.right.find(sData)
        else: 
            return False


# hashTab : ARRAY[0:listLen] of Node

hashTab = [Node(None)]*listLen

def insertHash(id):
    # id      : STRING
    # key     : INTEGER
    key = Hash(id)
    hashTab[key].insert(id)




#=====================================================================================================



##  T A S K 2.6

def searchTab(searchID):
    # searchID  : STRING
    # key       : INTEGER
    key = Hash(searchID)
    if hashTab[key].find(searchID):
        print("ID found")
    else:
        print("ID not found")


"""
insertHash("CC0110")
insertHash("AA0001")
insertHash("ZZ9999")
insertHash("BB2222")

searchTab("AA0001")
searchTab("KK6969")
"""

