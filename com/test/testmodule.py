'''
test_int=1;
test_double=2.3;

def toplam(a,b):
    return a+b

print("toplam : " + str(toplam(test_int,test_double)))

'''
'''
count = 2
strs = ["Hacker","Rank"]
for i in range(count):
    line = strs[i]
    oddChar=""
    evenChar=""
    for lc in range(len(line)):
        if (lc%2==1):
            oddChar = oddChar + line[lc]
        else:
            evenChar = evenChar + line[lc]
    print(evenChar + " " + oddChar)
'''
'''
N = 12
strs = ["insert 0 5","insert 1 10","insert 0 6","print","remove 6","append 9","append 1","sort","print","pop","reverse","print"]
newList = []
    
for i in range(len(strs)):
    line = strs[i]
    words = line.split(sep=" ")
    command =words[0] 
    if(command =="insert"):newList.insert(int(words[1]), int(words[2]))
    elif(command=="print"):print(newList)
    elif(command=="remove"):newList.remove(int(words[1]))
    elif(command=="sort"):newList.sort()
    elif(command=="append"):newList.append(int(words[1]))
    elif(command=="pop"):newList.pop()
    elif(command=="reverse"):newList.reverse()
'''
'''
n = 10#int(input().strip())
arr = [3696,3739,3714,3719,3687,3732,3657,3664,3717,3702,3741,3683,3660,3648,3649,3721,3652,3683,3694,3647,3696,3673,3741,3732,3677,3738,3666,3741,3701,3723,3721,3648,3654,3706,3743,3733,3704,3668,3660,3741,3730,3710,3729,3739,3662,3647,3701,3713,3674,3663,3690,3696,3719,3690,3728,3653,3734,3718,3722,3721,3725,3723,3703,3665,3668,3669,3654,3692,3699,3691,3682,3646,3649,3712,3688,3646,3662,3724,3705,3714,3692,3680,3690,3741,3693,3729,3664,3692,3660,3652,3718,3723,3684,3650,3685,3725,3679,3734,3710,3735,3685,3711,3672,3715,3739,3687,3660,3735,3674,3672,3674,3705,3666,3714,3710,3740,3656,3667,3655,3707,3710,3730,3695,3661,3713,3708,3688,3646,3653,3652,3701,3689,3657,3654,3647,3648,3656,3696,3730,3721,3712,3735,3651,3657,3716,3742,3704,3742,3705,3673,3680,3720,3727,3658,3738,3684,3653,3669,3656,3711,3734,3741,3743,3742,3655,3709,3743,3709,3697,3648,3667,3726,3717,3673,3700,3655,3651,3654,3728,3724,3651,3704,3687,3659,3656,3721,3663,3727,3725,3723,3660,3666,3664,3683,3678,3665,3681,3737,3714,3723,3660,3662,3724,3672,3657,3690,3718,3726,3714,3742,3689,3725,3706,3719,3674,3736,3712,3681,3701,3715,3738,3719,3714,3664,3659,3692,3651,3647,3722,3691,3647,3675,3700,3646,3706,3687,3685,3722,3740,3730,3732,3703,3730,3667,3667,3718,3720,3695,3711,3679,3656,3680,3677,3744,3740,3668,3710,3690,3724,3695,3692,3647,3717,3717,3682,3741,3681,3717,3691,3700,3659,3673,3705,3673,3672,3691,3686,3737,3701,3702,3742,3689,3658,3680,3676,3679,3716,3696,3673,3669,3711,3726,3691,3703,3650,3669,3742,3697,3737,3665,3710,3723,3668,3690,3700,3725,3736,3723,3718,3701,3679,3714,3651,3736,3664,3705,3656,3722,3694,3665,3660,3656,3676,3664,3715,3654,3675,3666,3688,3660,3667,3726,3718,3736,3735,3684,3667,3703,3701,3664,3682,3678,3718,3687,3699,3726,3650,3730,3648,3695,3690,3730,3713,3711,3732,3692,3736,3654,3698,3735,3652,3711,3742,3712,3664,3671,3682,3645,3691,3716,3719,3738,3681,3720,3651,3680,3657,3733,3702,3673,3682,3651,3688,3646,3665,3743,3704,3669,3721,3742,3667,3730,3715,3653,3721,3704,3737,3729,3700,3648,3668,3696,3742,3700,3666,3735,3720,3657,3722,3684,3655,3692,3670,3671,3673,3744,3647,3701,3671,3713,3709,3674,3688,3715,3656,3686,3649,3737,3712,3696,3646,3677,3654,3669,3659,3723,3702,3687,3726,3737,3713,3646,3723,3704,3693,3710,3726,3649,3669,3645,3667,3683,3684,3662,3705,3669,3676,3715,3666,3677,3648,3738,3696,3678,3682,3655,3678,3678,3682,3676,3724,3720,3694,3740,3707,3737,3654,3698,3731,3683,3706,3687,3712,3735,3694,3708,3680,3675,3668,3660,3652,3656,3657,3649,3688,3681,3739,3716,3667,3680,3668,3670,3738,3716,3652,3711,3720,3744,3671,3677,3705,3668,3666,3744,3687,3692,3697,3687,3673,3722,3694,3709,3649,3725,3666,3681,3689,3721,3706,3721,3723,3722,3650,3696,3701,3725,3716,3648,3703,3709,3739,3687,3697,3647,3718,3660,3739,3657,3701,3651,3683,3731,3678,3645,3731,3654,3743,3702,3677,3645,3677,3698,3722,3722,3711,3724,3738,3663,3649,3697,3723,3655,3662,3715,3677,3729,3723,3689,3673,3678,3661,3737,3682,3675,3728,3652,3721,3650,3653,3744,3686,3738,3712,3685,3738,3660,3723,3660,3730,3723,3664,3698,3683,3685,3716,3741,3648,3731,3692,3659,3658,3669,3702,3724,3652,3675,3649,3657,3701,3678,3647,3719,3646,3655,3646,3708,3663,3725,3655,3660,3729,3702,3661,3712,3695,3668,3678,3648,3650,3733,3709,3666,3688,3687,3742,3682,3662,3704,3735,3697,3740,3727,3703,3692,3683,3700,3705,3649,3660,3738,3742,3679,3707,3721,3698,3675,3690,3676,3694,3744,3669,3658,3680,3654,3668,3706,3722,3667,3657,3744,3727,3710,3681,3672,3646,3692,3690,3723,3647,3732,3722,3689,3697,3683,3717,3686,3679,3646,3683,3708,3727,3673,3706,3647,3714,3652,3679,3687,3707,3660,3650,3723,3692,3717,3688,3660,3725,3699,3668,3733,3672,3737,3697,3704,3715,3665,3681,3677,3731,3734,3650,3708,3717,3716,3680,3735,3730,3698,3718,3694,3720,3648,3724,3690,3680,3670,3734,3698,3708,3656,3689,3726,3676,3683,3671,3671,3733,3709,3667,3680,3711,3687,3707,3720,3706,3728,3680,3683,3736,3659,3734,3721,3707,3720,3680,3662,3647,3656,3720,3658,3724,3717,3660,3704,3671,3662,3730,3734,3721,3712,3731,3737,3687,3740,3721,3674,3742,3645,3683,3717,3713,3653,3698,3718,3701,3645,3742,3681,3719,3720,3682,3652,3733,3707,3685,3675,3683,3701,3656,3645,3725,3655,3737,3681,3671,3711,3683,3715,3700,3732,3693,3705,3677,3701,3716,3683,3655,3676,3739,3650,3693,3666,3715,3726,3675,3683,3705,3672,3650,3654,3727,3647,3727,3668,3664,3734,3703,3650,3648,3700,3672,3673,3734,3666,3656,3693,3693,3684,3713,3704,3696,3658,3662,3726,3653,3692,3681,3729,3700,3703,3675,3696,3696,3678,3681,3678,3676,3682,3714,3659,3726,3662,3663,3675,3721,3741,3708,3695,3687,3694,3674,3725,3737,3691,3699,3665,3739,3703,3698,3669,3725,3663,3694,3741,3663,3673,3719,3652,3664,3734,3701,3647,3720,3675,3741,3732,3652,3686,3718,3655,3674,3732,3725,3722,3723,3678,3716,3669,3672,3673,3717,3650,3702,3690,3654,3692,3648,3728,3653,3702,3705,3712,3673,3685,3711,3697,3736,3691,3704,3725,3725,3727,3713,3728,3705,3674,3715,3662,3662,3739,3674,3700,3647,3718,3708,3678,3680,3715,3672,3726,3744,3704,3645,3742,3671,3663,3667,3674,3687,3679,3720,3690,3661,3650,3670,3657,3696,3654,3741,3731]#[int(arr_temp) for arr_temp in input().strip().split(' ')]
n2 = 13#int(input().strip())
arr2 = [3697,3674,3700,3652,3702,3718,3693,3724,3676,3657,3656,3654,3668,3721,3683,3704,3711,3695,3656,3715,3685,3688,3688,3728,3731,3732,3669,3717,3687,3654,3694,3689,3653,3682,3646,3674,3668,3719,3720,3657,3668,3722,3675,3674,3698,3690,3732,3650,3651,3696,3725,3683,3705,3710,3688,3727,3725,3716,3716,3721,3728,3722,3671,3670,3681,3645,3696,3713,3680,3717,3673,3675,3720,3741,3738,3669,3676,3679,3723,3727,3647,3713,3660,3681,3687,3707,3675,3678,3726,3649,3723,3726,3694,3701,3741,3718,3743,3720,3674,3738,3686,3706,3698,3723,3728,3648,3654,3742,3690,3709,3737,3704,3681,3725,3713,3724,3684,3648,3690,3650,3667,3741,3655,3718,3680,3665,3665,3727,3660,3655,3703,3692,3739,3649,3677,3724,3737,3683,3696,3708,3736,3744,3738,3742,3739,3703,3706,3652,3668,3648,3683,3654,3708,3688,3713,3669,3717,3675,3694,3709,3739,3702,3666,3681,3685,3673,3662,3645,3683,3691,3671,3652,3702,3659,3649,3652,3665,3721,3704,3739,3719,3715,3713,3729,3692,3703,3731,3645,3662,3734,3654,3667,3664,3646,3704,3680,3730,3737,3742,3683,3732,3701,3666,3673,3669,3715,3655,3675,3654,3720,3720,3678,3739,3726,3707,3738,3681,3720,3653,3669,3716,3700,3681,3668,3741,3731,3650,3705,3675,3687,3671,3738,3646,3661,3737,3744,3696,3690,3648,3719,3723,3670,3673,3666,3743,3714,3657,3725,3677,3704,3697,3703,3725,3682,3723,3662,3664,3647,3701,3723,3691,3710,3742,3704,3674,3691,3718,3682,3697,3664,3646,3683,3705,3682,3685,3702,3658,3648,3733,3702,3739,3742,3703,3742,3737,3649,3669,3683,3668,3653,3670,3723,3680,3681,3717,3732,3657,3734,3735,3714,3698,3650,3735,3656,3676,3712,3678,3739,3701,3735,3677,3672,3710,3646,3721,3652,3737,3686,3692,3682,3695,3662,3719,3736,3711,3672,3721,3676,3732,3698,3673,3667,3716,3648,3698,3648,3678,3723,3645,3742,3724,3678,3705,3678,3701,3649,3742,3717,3699,3677,3680,3700,3717,3691,3737,3672,3661,3702,3672,3740,3709,3649,3719,3742,3739,3668,3650,3737,3660,3691,3723,3679,3696,3696,3682,3738,3671,3687,3700,3722,3655,3701,3694,3723,3742,3667,3707,3652,3715,3711,3657,3718,3656,3663,3655,3720,3725,3674,3719,3715,3694,3676,3708,3737,3740,3690,3696,3675,3694,3660,3710,3667,3715,3717,3700,3695,3712,3687,3687,3726,3663,3733,3675,3735,3664,3662,3728,3711,3742,3718,3722,3646,3687,3680,3715,3664,3669,3654,3659,3686,3730,3666,3648,3713,3703,3712,3704,3701,3665,3679,3722,3682,3741,3650,3689,3735,3725,3657,3694,3728,3724,3685,3725,3731,3649,3651,3736,3694,3723,3677,3689,3685,3683,3682,3696,3718,3654,3673,3722,3718,3667,3658,3718,3683,3693,3705,3660,3694,3698,3650,3714,3657,3652,3656,3732,3668,3685,3734,3678,3689,3701,3666,3674,3646,3695,3692,3653,3705,3679,3654,3741,3666,3684,3645,3697,3735,3716,3735,3685,3730,3672,3656,3727,3695,3723,3714,3647,3681,3647,3713,3699,3696,3733,3722,3659,3652,3733,3683,3660,3736,3730,3687,3731,3704,3725,3733,3683,3692,3721,3657,3689,3668,3703,3723,3673,3711,3670,3725,3710,3655,3739,3666,3676,3681,3652,3667,3679,3723,3666,3712,3682,3692,3691,3668,3671,3720,3688,3658,3671,3687,3648,3716,3735,3649,3651,3720,3676,3705,3712,3673,3677,3722,3659,3683,3699,3679,3718,3650,3711,3722,3648,3662,3650,3656,3738,3672,3734,3740,3655,3664,3673,3667,3730,3700,3741,3729,3686,3647,3734,3730,3715,3651,3704,3696,3705,3650,3700,3664,3701,3714,3727,3702,3684,3659,3720,3655,3715,3706,3654,3698,3669,3728,3718,3663,3680,3696,3662,3688,3653,3645,3662,3687,3744,3709,3742,3680,3678,3742,3660,3679,3663,3671,3682,3674,3721,3712,3702,3703,3714,3651,3725,3738,3705,3709,3683,3654,3677,3684,3725,3663,3697,3689,3672,3738,3711,3678,3660,3660,3692,3646,3731,3726,3736,3657,3742,3686,3710,3708,3677,3680,3669,3723,3717,3667,3681,3732,3741,3676,3735,3684,3652,3677,3734,3718,3656,3687,3692,3677,3658,3683,3721,3660,3656,3717,3705,3719,3711,3667,3653,3672,3700,3705,3730,3647,3675,3708,3717,3650,3714,3650,3701,3715,3680,3659,3679,3675,3655,3723,3649,3678,3660,3721,3663,3707,3687,3714,3692,3658,3730,3722,3697,3680,3712,3697,3661,3692,3666,3678,3727,3708,3653,3673,3684,3662,3740,3743,3672,3726,3726,3681,3713,3719,3673,3715,3725,3698,3648,3653,3665,3669,3730,3708,3683,3730,3729,3645,3693,3678,3647,3736,3736,3732,3673,3660,3646,3691,3727,3712,3662,3656,3690,3673,3656,3724,3690,3716,3721,3741,3725,3721,3690,3647,3721,3690,3657,3655,3680,3692,3674,3706,3744,3741,3692,3729,3687,3744,3707,3664,3744,3656,3712,3680,3660,3701,3720,3664,3665,3737,3662,3667,3667,3647,3665,3648,3723,3693,3701,3702,3712,3720,3734,3724,3651,3734,3647,3654,3663,3724,3671,3738,3658,3740,3693,3678,3726,3656,3651,3669,3689,3733,3721,3716,3695,3720,3726,3697,3674,3698,3660,3688,3701,3652,3706,3687,3743,3711,3726,3706,3670,3666,3687,3741,3668,3660,3700,3710,3729,3646,3704,3690,3690,3729,3693,3714,3709,3706,3699,3700,3696,3721,3684,3650,3647,3700,3669,3716,3647,3716,3726,3664,3660,3660,3668,3647,3661,3674,3730,3705,3688,3692,3710,3724,3681,3715,3722,3726,3683,3677,3706,3645,3701,3721,3666,3737,3654,3744,3662,3720,3707,3734,3704,3711,3707,3647,3659,3740,3655,3697,3717,3692,3685,3708,3701,3680,3682,3648,3744,3687,3657,3663,3690,3731,3673,3674,3734,3652,3714,3725,3703,3651,3711,3664,3696,3722,3685,3741,3647,3646,3709,3695,3691,3673,3743,3671,3727,3704,3675,3672,3737]
leakList = []
dictCountArr1 = dict()

for i in arr:
    count = int(dictCountArr1.get(i)) if dictCountArr1.__contains__(i) else 0 
    count = count +1
    dictCountArr1.update(({i:count}))

for i in arr2:
    count = int(dictCountArr1.get(i)) if dictCountArr1.__contains__(i) else 0
    count = count - 1
    dictCountArr1.update(({i:count}))
    if(count < 0 and not leakList.__contains__(str(i))) :
            leakList.append(str(i))
            
leakList.sort()
print(leakList)
'''
'''
n = 2
nlist = list(map(int, "387 38 498 988 434 282 467 641 464 682 341 586 222 736 187 415 330 323 109 818 78 469 560 623 748 782 352 398 196 39 603 344 630 841 794 994 648 293 861 800 944 249 921 10 781 437 915 451 782 262".split(" ")))

tup=tuple(nlist)

print(hash(tup))
'''
'''
nlist = list(map(int, "1 1 1 2".split(" ")))

distance = []

Matrix=[]
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            if(i+j+k != 2):
                test = [i,j,k]
                Matrix.append(test)
                
print(Matrix)
'''
'''
def factorial(val):
    result=int(1)
    if val > 2 :
        result = int(val)*int(factorial(val-1))
    else :
        result = int((val))*int(val-1)
    val=int(val)-1
    return result
    
    
print(factorial(3))
'''
'''
#n=524283
#n=524275
#n=65535
n=524275
val= (bin(n)[2:])
print(val)

count=len(val)
strArr = [1 for a in range(0,count) if (a-1>=0 and val[a] == str(1) and val[a-1] == str(1))]
result=0
aa=1
for a in range(0,count):
    if val[a] == str(0) :
        aa=1
    if (a-1>=0 and val[a] == str(1) and val[a-1] == str(1)):
        aa=aa+1
        if(aa>result):
            result = aa 
    

print(result)
'''
'''
#x,y         x,y+1     x,y+2 
#          x+1,y+1     
#x+2,y     x+2,y+1   x+2,y+2 

def findHourglassSum(arr):
    sumArr=0
    arr_total=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):            
            if(i+2 < len(arr) and j+2< len(arr[i])):
                sumArr += arr[i][j] + arr[i][j+1] + arr[i][j+2]
                sumArr += arr[i+1][j+1]
                sumArr += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
                arr_total.append(sumArr)
                sumArr=0
                 
    return arr_total

val = "0 4 6 0 7 6 1 2 6 8 3 1 8 4 2 8 8 6 3 1 2 5 7 4 3 5 3 6 6 6 3 6 0 8 6 7"

arr=[]
for i in range(6):
    val2 = val[i*12:(i+1)*12]
    arr_t = [-1*int(a) for a in val2.rstrip().split(' ')]
    arr.append(arr_t)


arr_total=findHourglassSum(arr)

arr_total.sort(reverse=True)

print(arr_total[0])
'''
'''
val="57 57 -57 57"

#arr = list(val.split(' '))

arr = list(map(int, val.split(' ')))

maxVal=max(arr)

sMaxVal=min(arr)
for i in arr:
    sMaxVal= i if (i<maxVal and i>sMaxVal) else sMaxVal
    
print(sMaxVal)
'''
'''
import operator
arr = [["Harry" , 37.21] , ["Berry" ,37.21],["Tina" ,37.2],["Akriti",41],["Harsh",39]]

arr.sort(key=operator.itemgetter(1), reverse=False)
nameLst=[]
minP=arr[0][1]
sMinP=0
for lst in arr:
    if not minP == lst[1] and sMinP == 0:
        sMinP=lst[1]
    if not sMinP == 0 and sMinP == lst[1]:
        nameLst.append(lst[0]) 

nameLst.sort()
for name in nameLst:
    print(name)
'''
'''
class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores
        self.grade = "T"
    
    def calculate(self):
        avg = sum(scores) / len(scores)
        if avg >= 90:
            grade="O"
        elif avg>=80:
            grade="E"
        elif avg>=70:
            grade="A"
        elif avg>=55:
            grade="P"
        elif avg>=40:
            grade="D"
        else :
            grade="T"
        
        return grade
        
        
val="Heraldo Memelli 8135627"
line = val.split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int("2") # not needed for Python
scr="100 90"
scores = list( map(int, scr.split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
'''
'''
def split_and_join(line):
    result="-".join(line.split(" "))
    return result

print(split_and_join("this is a string"))
'''
'''
def count_substring(string, sub_string):
    count=0
    for i in range(0,len(string)):
        if(string[i:i+len(sub_string)]==sub_string):
            count +=1

    return count


print(count_substring("ABCDCDC", "CDC"))
'''
'''Abstract CLASS EXAMPLE'''
'''
from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass

class MyBook(Book) : 
    def __init__(self,title,author,price):
        super(MyBook, self).__init__(title,author)
        self.price = price
        
    def display(self):
        print("Title: %s" % self.title)
        print("Author: %s" % self.author)
        print("Price: %s" % self.price)


title="The Alchemist"
author="Paulo Coelho"
price=248
new_novel=MyBook(title,author,price)
new_novel.display()
'''
'''
cm="-"
c=".|."
N, M = map(int,"15 50".split())
for i in range(1,N,2): 
    print ((c*i).center(M,"-"))
print ("Welcome".center(M,"-"))
for i in range(N-2,-1,-2): 
    print ((c*i).center(M,"-"))
'''
'''
def print_formatted(number):
    
    size = len(bin(number)[2:])+1
    for i in range(1,number+1):
        binNum = str(bin(i)[2:])
        hexNum = str(hex(i)).upper()[2:]
        octNum = str(oct(i)[2:])
        print(str(i).rjust(size-1," ") + octNum.rjust(size," ") + hexNum.rjust(size," ") + binNum.rjust(size))

print_formatted(17)
'''
'''
def average(array):
    nSet = set(array)
    return sum(nSet)/len(nSet)

if __name__ == '__main__':
    val = "161 182 161 154 176 170 167 171 170 174"
    arr = list(map(int, val.split()))
    result = average(arr)
    print(result)
'''
'''
N , M = map(int,"4 4".split())
l1 = set(map(int,"2 4 5 9".split()))
l2 = set(map(int,"2 4 11 12".split()))

result = (l1.union(l2)).difference(l1.intersection(l2))


for i in sorted(result) :
    print(i)
'''
