'''
f = open('C:\\Temp\\test.txt', 'r+')
n = int(f.readline())

for i in range(n) :
    count = 0
    txt = f.readline()
    for j in range(0,len(txt)-1):
        count = (int(count+1) if txt[j] == txt[min(j+1,len(txt)-1)] else int(count) )
    print(count)
'''
'''
from _functools import reduce
from _operator import  add

f = open('C:\\Temp\\test.txt', 'r+')
m = int(f.readline())
n = int(f.readline())

def isSorted(txt): 
    return "".join(sorted(txt)) == txt;

arr=[]
for i in range(m) :
    txt = ""
    for j in range(n) :
        txt = txt + reduce(add,sorted(f.readline().replace("\n","")))
    
    print("YES" if isSorted(txt) else "NO")
'''
'''        
f = open('C:\\Temp\\test.txt', 'r+')
T = int(f.readline())

all_grids = []
for t in range(T):
    N = int(f.readline())
    n = [''.join(sorted(f.readline().strip())) for i in range(N)]
    all_grids.append([N, n])

def check_condition(grid):
    answer = 'YES'
    for i in range(grid[0] - 1):
        for j in range(grid[0]):
            if grid[1][i][j] > grid[1][i+1][j]:
                answer = 'NO'
                return answer
    return answer

answers = []

for grid in all_grids:
    answers.append(check_condition(grid))

print('\n'.join(answers))
'''
'''
#!/bin/python3

from itertools import permutations


def controlForSeq(a):
    for i in range(1,len(a)) :
        if (a[i-1] == a[i]) :
            return False

    return True

#s_len = 10
#s = "beabeefeab"
#Test case 4
s_len = 375
s = "uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon"
uniqeS = ''.join(set(s))

tS = []
for i in permutations(uniqeS,len(uniqeS)-2):
    cStr = ''.join([c for c in s if c not in i])
    if (controlForSeq(cStr)) :
        tS.append(cStr)

print(len(max(tS)))
'''
'''

n = 5
for i in range(1,n+1):
    print(('#'*i).rjust(n,' '))

'''
'''
s = "(()(test))"
def controlParanthesis(cStr):
    return (s.count(("(")) - s.count((")"))) == 0 
'''
'''
1 2 3
4 5 6
7 8 9

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''
'''ARRAY ROTATOR
n=1
#lst = [[1,2,3],[4,5,6],[7,8,9]]
lst = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
lstT = list(map(list, zip(*lst)))

print(lstT)
lenT = (len(lstT))//2
for i in range(0,lenT+1) :
    if(n==1) :
        temp = lstT[i]
        lstT[i] = lstT[len(lstT)-1-i]
        lstT[len(lstT)-1-i] = temp
    else :
        lensd = len(lstT[i])//2
        for j in range(0,lensd) :
            temp = lstT[i][j]
            lstT[i][j] = lstT[i][len(lstT[i])-1-j] 
            lstT[i][len(lstT[i])-1-j] = temp

print(lstT)
'''
'''
s = "denemeaemened"

def isPalindromic(s) :
    for i in range(len(s)-1//2):
        if (not (s[i] == s[len(s)-1-i])) :
            return False
        
    return True

print(isPalindromic(s))
'''
'''
#!/bin/python3

import sys
from itertools import permutations

def controlForSeq(a):
    for i in range(1,len(a)) :
        if (a[i-1] == a[i]) :
            return False

    return True

#s_len = 10
#s = "beabeefeab"
#Test case 4
#s_len = 375
#s = "uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon"
#Test case 15
s_len = 63
s = "pvmaigytciycvjdhovwiouxxylkxjjyzrcdrbmokyqvsradegswrezhtdyrsyhg"
# output -> 6
uniqeS = ''.join(set(s))

tS = []
for i in permutations(uniqeS,2):
    cStr = ''.join([c for c in s if c in i])
    if (controlForSeq(cStr)) :
        tS.append(cStr)

print(0 if (tS is None or len(tS)<=0 )else len(max(tS, key=len)))k
 '''
'''Marc's Cakewalk
n = 3
calories = list(map(int, "1 3 2".strip().split(' ')))
calories.sort(key=None, reverse=True)

totalMile = 0
for i in range(len(calories)):
    totalMile += calories[i]*(2**i)
    
print(totalMile)
'''
'''Luck Balance
f = open('C:\\Temp\\test.txt', 'r+')
n,k = map(int,f.readline().strip(' ').split())
lc = [list(map(int,f.readline().strip().split(" "))) for _ in range(n) ]

lc.sort(key=lambda x: (x[1],x[0]), reverse=False)

ttL = 0
i=0
while (len(lc) > 0) :
    if (lc[i][1] == 0 ) :
        ttL += lc[i][0]
    else :
        if(len(lc)>k) :
            ttL -= lc[i][0]
        else :
            ttL += lc[i][0]
            
    lc.remove(lc[i])

print(ttL)
'''
'''Maximum Perimeter Triangle
#test 4 
#20
#9 2015 5294 58768 285 477 72 13867 97 22445 48 36318 764 8573 183 3270 81 1251 59 95094
#output -> 72 81 97

n = int("20")
l = sorted(int(i) for i in "9 2015 5294 58768 285 477 72 13867 97 22445 48 36318 764 8573 183 3270 81 1251 59 95094".split())

i = n-3
while i >= 0 and (l[i] + l[i+1] <= l[i+2]) :
    i -= 1

if i >= 0 :
    print(l[i],l[i+1],l[i+2])
else :
    print(-1)
'''
'''Equal Stacks
n1,n2,n3 = "5 3 4".strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in "3 2 1 1 1".strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in "4 3 2".strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in "1 1 4 1".strip().split(' ')]

def sumOfArray(arr,ind):
    return int(sum(arr[ind:arr.__len__()]))
 
h1s=[sumOfArray(h1,i) for i in range(n1)]
h2s=[sumOfArray(h2,i) for i in range(n2)]
h3s=[sumOfArray(h3,i) for i in range(n3)]

cl=[]
if n1 == min(n1,n2,n3) :
    cl = h1s
elif n2 == min(n1,n2,n3):
    cl = h2s
else :
    cl = h3s

for i in cl:
    if (i in h1s and i in h2s and i in h3s) :
        break
    
print(i) 
'''  
''' Equal Stacks exp. didnt code it
from collections import deque

def read_queue():
    return deque(map(int, input().strip().split()))

nstacks = 3
stacks = [deque([3,2,1,1,1]),deque([4,3,2]),deque([1,1,4,1])]
heights = list(map(sum, stacks))

while len(set(heights)) > 1:
    ihighest = heights.index(max(heights))
    heights[ihighest] -= stacks[ihighest].popleft()

print(heights[0])
'''     
    