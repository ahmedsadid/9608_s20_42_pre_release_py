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
        self.pointer = None

class LinkedList: 
    def __init__(self):  
        self.head = None

    def insert(self,inData):
        #   inData :  STRING
        new = Node(inData)
        if not self.head: 
            self.head = new
        else:
            end = self.head
            while end.pointer:
                end = end.pointer
            end.pointer = Node(inData)
            

    def find(self,sData):
        #   sData :  STRING
        node = self.head
        while node:
            if node.data == sData:
                return True
            else:
                node = node.pointer
        
        return False

#=======(unnecessarry)=======================
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data)
            temp = temp.pointer
#=======(^unnecessarry^)=====================



# hashTab : ARRAY[0:listLen] of Node
hashTab = [LinkedList() for _ in range(listLen)]

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

searchTab("AA0001") #positive
searchTab("KK6969") #negative 


print(hashTab[1].head.data)
print(hashTab[0].head.data)
"""
