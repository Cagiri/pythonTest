'''
f = open('C:\\Temp\\text.txt', 'r+')

m,n = list(map(int,f.readline().split()))
clText = f.readline()
cl = list(map(int,clText.split()))
A = set(map(int,f.readline().split()))
B = set(map(int,f.readline().split()))

ch = ([(i in A ) - (i in B) for i in cl])

print(sum(ch))
'''
'''
class Difference:
    def __init__(self, a):
        self.__elements = a
        
    def computeDifference(self):
        self.maximumDifference = max(self.__elements) - min(self.__elements) 
        


# End of Difference class

n = 3
a = [int(e) for e in "1 2 5".split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
'''
'''
n = 9
s = set(map(int, "1 2 3 4 5 6 7 8 9".split())) 
cN = 10

func = getattr(s,"remove")
func(9)

print(s)
'''
'''
from collections import deque
f = open('C:\\Temp\\test.txt', 'r+')

count = int(f.readline())
textList = []
itemList = deque([])
for i in range(count):
    itemName = str(f.readline())[:-1]
    if(not textList.__contains__(itemName)):
        itemList.append(itemName)
    textList.append(itemName)    
    
print(len(itemList))
listr=""
for i in itemList :
    listr = listr + str(textList.count(i)) + " "
print(listr)
'''
'''
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
'''
'''
import cmath

cN="-1-5j"

print(abs(complex(cN)))
print(cmath.phase(complex(cN)))
'''
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
            
    def insert(self,head,data): 
        newNode = Node(data)
        
        if head == None :
            return newNode
        elif head.next == None  :
            head.next = newNode
        else :
            self.insert(head.next, data)
        
        return head

mylist= Solution()
T=list(map(int,"2 3 4 1".split()))
head=None
for data in T:
    head=mylist.insert(head,data)    
mylist.display(head);     
'''
'''
import math
AB = 56
BC = 54

MC = math.hypot(AB, BC)/2
degree_sign= u'\N{DEGREE SIGN}'

print(round(math.degrees(math.acos((MC * MC + BC * BC - MC * MC)/(2.0 * BC * MC)))))
print(str(int(round(math.degrees(math.atan2(AB, BC)))))+degree_sign)
'''
'''
from itertools import permutations

n = list(map(str,"Hack 2".split(' ')))

perL = list(permutations(n[0],int(n[1])))
pN = [''.join(i).upper() for i in perL]
pN.sort(key=None, reverse=False) 
for i in pN:
    print(i)
'''
'''
S = input().strip()

try:
    x = int(S)
    print(x)
except ValueError:
    print ("Bad String")
'''
'''
from collections import deque

class Solution:
    def __init__(self):
        self.queue = deque([])
        self.stack = []
    
    def pushCharacter(self,s):
        self.stack.append(s)
        
    def enqueueCharacter(self,s):
        self.queue.append(s)
        
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        return self.queue.popleft() 
        
s="racecar"
obj=Solution()   

l=len(s)
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
for i in range(l // 2):
    a = obj.popCharacter()
    b = obj.dequeueCharacter()
    if a != b:
        isPalindrome=False
        break
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")   
'''
'''
def swapValue(aList,i,j):
    aList[j], aList[i] = aList[i], aList[j]
        

n = int('3')
a = [int(a_temp) for a_temp in "1 2 3".strip().split(' ')]

count=0

for i in range(n) :
    for j in range(n-1) :
        if(a[j] > a[j+1]) :
            swapValue(a, j, j+1)
            count +=1

print (count)
'''
'''
from itertools import  combinations

s,n = "abcd 3".upper().split(' ')

comL=[]

for i in range(1, int(n)+1) :
    comL.append([''.join(j) for j in combinations(sorted(s), i) ] )

testL = []

for l in comL:
    testSl=[]
    for com in l:
        l = list(com)
        l.sort(key=None, reverse=False)
        testSl.append(''.join(l))
    testSl.sort()
    testL.append(testSl)

print("\n".join("\n".join(t for t in l) for l in testL))
'''
'''
import xml.etree.ElementTree as etree

def get_attr_number(node):
    attrCount = 0   
    for child in node:
        print (child.attrib)
        if(len(child.getchildren())>1):
            attrCount = attrCount + get_attr_number(child)
        else :
            attrCount = attrCount + len(child.attrib)
        
    
    
    return attrCount+1


if __name__ == '__main__':
    f = open('C:\\Temp\\text.txt', 'r+')
    xml = f.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
'''
    
    