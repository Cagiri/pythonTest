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
#!/bin/python3

from itertools import permutations


s_len = 10
s = "beabeefeab"
uniqeS = ''.join(set(s))

for i in permutations(uniqeS,3):
    tS = s.replace(c for c in i, "");
    print(tS)




