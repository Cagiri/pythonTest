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



