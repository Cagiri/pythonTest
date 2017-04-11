'''
import xml.etree.ElementTree as etree

maxdepth = 1
def depth(elem, level):
    global maxdepth
    if(len(elem.getchildren())<=0 and level == -1) :
        maxdepth = 0
        return 
    for child in elem:
        if (level + 1 >= maxdepth):
                maxdepth = maxdepth + 1
        if (len(child.getchildren()) > 0):
            depth(child, level + 1)

if __name__ == '__main__':
    f = open('C:\\Temp\\test.txt', 'r+')
    xml = f.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
'''
'''
from itertools import combinations_with_replacement

s,n = "HACK 2".split()#raw_input().split(' ')

combList = list (''.join(tup) for tup in combinations_with_replacement(sorted(s),int(n)))
print('\n'.join(combList))
'''
''' BINARY SEARCH TREE
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if (root is None):
            return -1
        return 1 + max([self.getHeight(root.left),self.getHeight(root.right)])
                
T=list(map(int,"3 5 2 1 4 6 7".split(" ")))
myTree=Solution()
root=None
for data in T:
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  
'''
'''
from itertools import groupby 

s= "1222311"

l = groupby(s)
result = [(sumN(1 for _ in group),int(label)) for label, group in l]
print(" ".join("({}, {})".format(label, count) for label, count in result))
'''
'''
class B():
    def method(self,arg):
        print("test " + arg)

class C(B):
    def method(self, arg):
        super().method(arg)

c = C()
c.method("2 test")
'''
'''
class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
       
    def levelOrder(self,root):
        if root.data is None :
            return
        
        queue = [root]
    
        while queue:
            node = queue.pop()
            print(node.data, end=" ")
            
            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)
            
myTree=Solution()
root=None
for data in list(map(int,"3 5 4 7 2 1".split())) :
    root=myTree.insert(root,data)
myTree.levelOrder(root)
'''
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next
        
    def removeDuplicates(self,head):
        cK = {}        
        current = [head]
        
        newList=None
        while current:
            node = current.pop()
            if node.next: current.insert(0,node.next)
            if not cK.__contains__(node.data) :
                newList=self.insert(newList, node.data)
                cK[node.data] = node.data

        return newList

mylist= Solution()
head=None
for data in list(map(int,"1 2 2 3 3 4".split())) :
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
'''    
'''
import math

num = 1
divList = [i for i in range(1,int(math.sqrt(num))+1) if num%i==0]
if len(divList) < 2 and num!=1:
    print("Prime")
else :
    print("Not prime")
'''     
'''
from datetime import datetime

def calcFine(returned,expected):
    delay=int((returned - expected).days)
    
    if (delay <= 0 ):
        return 0
    
    if (not returned.year == expected.year) :
        return 10000
    elif (delay < 31) :
        return delay*15
    elif (delay < 365) :
        return 500 * (delay//31)
    
    return 0
    
d1 = ""
for i in "1 1 2010".split() :
    d1 += i + " " if len(i)>1 else i.rjust(2,"0") + " "
      
d2=""
for i in "31 12 2009".split() :
    d2 += i + " " if len(i)>1 else i.rjust(2,"0") + " "

    
returned = datetime_object = datetime.strptime(d1.strip(), '%d %m %Y' if len(d1)>9  else '%d %m %y')
expected = datetime_object = datetime.strptime(d2.strip(),'%d %m %Y' if len(d2)>9  else '%d %m %y')


print (calcFine(returned, expected))
'''
'''
from itertools import combinations

inArr = "b".split()

cl = list(combinations(inArr,1))

count=0

for tup in cl :
    count += 1 if('a' in tup) else 0 

print(round(count/len(cl),4))
'''
'''
def test(f):
    def fun(l):
        nl = ["+91 " + j[0:5] + " " + j[5:10] for j in [i[-10:] for i in l]]
        f(nl)
        return l
    return fun     




@test
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = ["919875641230","9195969878"]
    sort_phone(l)
'''
'''
def person_lister(f):
    def inner(people):
        t=[]
        people.sort(key=lambda x:x[2])
        for p in  people:
            txt = f(list(p))
            t.append(txt)
        return t
    return inner



@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = ["Mike Thomson 20 M".split() ,"Robert Bustle 32 M".split(), "Andria Bustle 30 F".split()]
    print(*name_format(people), sep='\n')
'''
'''
import itertools
f = open('C:\\Temp\\test.txt', 'r+')

n,m = map(int,f.readline().split())
aL = [list(map(int,f.readline().split()))[1:] for i in range(n)]

def getV(*nums):
    return sum(x*x for x in nums) % m

print (max(itertools.starmap(getV,itertools.product(*aL))))
'''
'''
def logger(func):
    def inner(*args, **kwargs): #1
        print ("Arguments were: %s, %s" % (args, kwargs))
        return func(*args, **kwargs)
    return inner

@logger
def foo1(x, y=1):
    return x * y

dct = {'x': 1, 'y': 2}
print(foo1(**dct))
lst = [8,10]
print(foo1(*lst))
'''
'''
import re

f = open('C:\\Temp\\test.txt', 'r+')
N = int(f.readline().strip())
lM = []
for a0 in range(N):
    firstName,emailID = map(str,f.readline().strip().split(' '))
    if (re.search("(?<=@)\w+", emailID).group(0) == "gmail") :
        lM.append(firstName)

lM.sort()
print("\n".join(lM))
'''
'''
import re
m = re.search('(?<=abc)\w+(?:.\w+)', 'abcdefans.awqe')
print(m.group(0))
'''
'''
from itertools import combinations

f = open('C:\\Temp\\test.txt', 'r+')
t = int(f.readline().strip())


def findMaxBitwiseControl(l,k):
     
    rslt = 0;
    for tub in l :
        sumt = None; 
        for i in tub:
            sumt = int(i) if sumt==None else sumt&int(i) 
        
        rslt  = sumt if (rslt<=sumt and sumt < k) else rslt 
        
    print(rslt)

for i in range(t) :
    n,k = map(int,f.readline().strip().split(" "))
    print(k-1 if ((k-1) | k) <= n else k-2)
    l = list(combinations([i for i in range(1,n+1)],k))
    findMaxBitwiseControl(l,k)
'''
'''
f = open('C:\\Temp\\test.txt', 'r+')
T = int(f.readline().strip())
for _ in range(T):
    n,k = map(int,f.readline().strip().split(" "))
    print(k-1 if ((k-1) | k) <= n else k-2)
'''
'''
def yieldtest(i):
    for i in range(i) :
        yield i

t = yieldtest(10)
print(list(t))
'''
'''
t1,t2,n = map(int,"0 1 10".split())

def getFibNum(n) :
    num = [t1,t2]
    for i in range(1,n) :
        num.append(int(num[i-1]) + int(num[i])**2)

    return num    

fibList = getFibNum(n+1)
print ( fibList[n-1])
'''
'''
#1 1 1000000000000 1000000000000 -> 1000000000000
#1 1 6 45 -> 16
#3 1 2 12 -> 3
#3 8 71 487 -> 18
#3 13 13 1000000000000 -> 10
#40#28 81 64143 93888052920 -> 2449
#m,w,p,n = map(int,"1 1 1000000000000 1000000000000".split(" "))
#m,w,p,n = map(int,"1 1 6 45".split(" "))
#m,w,p,n = map(int,"3 1 2 12".split(" "))
#m,w,p,n = map(int,"3 8 71 487".split(" "))
m,w,p,n = map(int,"28 81 64143 93888052920".split(" "))
#m,w,p,n = map(int,"3 13 13 1000000000000".split(" "))
def buyMachine() :
    global w,m,madeCand
    if(madeCand < p) :
        return
    buyCount = 0
    for _ in range(madeCand//p):
        buyCount += 1
        if (w < m) :
            w += 1
        else :
            m += 1
        
    madeCand -= buyCount*p

def makeCandie(seq) :
    global madeCand,m,w
    madeCand += seq*(m*w)


madeCand = 0
count = 0
seq = p
while (madeCand < n) :    
    makeCandie(seq)
    buyMachine()
    count += seq   
    
print(count)
'''
'''
madeCand = 0
def buyMachine() :
    global w,m,madeCand
    if(madeCand < p) :
        return
    buyCount = 0
    for _ in range(madeCand//p):
        buyCount += 1
        if (w < m) :
            w += 1
        else :
            m += 1
        
    madeCand -= buyCount*p

def makeCandie(seq) :
    global madeCand,m,w
    madeCand += seq*(m*w)

tw = m+w
count = max([p//(m*w),1])    
madeCand = (m*w)*count
while (madeCand < n) :
    if (madeCand*2 < 2) :
        buyMachine()
    seq = max([p//(m*w),1])
    makeCandie(seq)
    count +=seq

print (count)
'''
'''        
import string

def isPangram(txt) :
    d = dict.fromkeys(string.ascii_lowercase, 0)
    for i in txt.lower() :
        if (d.__contains__(i)) :
            d[i] = d[i]+1
    
    for i in d.values() :
        if i == 0 :
            return False      
    
    return True

txt = "We promptly judged antique ivory buckles for the next prize"    


print ("pangram" if isPangram(txt) else "not pangram")
'''    


