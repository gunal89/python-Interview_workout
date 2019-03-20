from __future__ import print_function

#Largest Number:
numlist = [10,20,1,900,-20,2,1058,300,1000,901]
largest1=largest2=largest3 = int()
for lnum in numlist:
    if lnum > largest3:
        if lnum > largest1:
            largest1,largest2= lnum,largest1
        elif lnum > largest2:
            largest2, largest3 = lnum, largest2
        else:
            largest3 = lnum
print ("1st largest num",largest1)
print ("2nd largest num",largest2)
print ("3rd largest num",largest3)

#Smallest Number:
smallest1 = numlist[0]
smallest2 = int()
for snum in numlist:
    if snum < smallest2:
        if snum < smallest1:
            smallest1,smallest2 = snum,smallest1
        else:
            smallest2 = snum
print ("1st Smallest num",smallest1)
print ("2nd Smallest num",smallest2)

#Fibonnaci Number:
count =0
n1 = 0
n2 =1
while (count < 10 ):
    print(n1,end=',')
    nr = n1 + n2
    n1=n2
    n2=nr
    count +=1

#Sorting without default fun()
sortlist =list()
while numlist:
    first_val = numlist[0]
    for item in numlist:
        if item < first_val:
            first_val = item
    sortlist.append(first_val)
    numlist.remove(first_val)
print ('\n',sortlist)
print("--Sorting----")
#sort --> Sort is doing sorting with same List or Dict itself. It modifies original Data.
#sorted - Sorted is doing sorting the list and dict.It return another list.Not modify the original object
sortlist1 = [2,9,45,3,1]
print ("--",(sortlist1.sort())) #returns NONE
print (sortlist1)
#sorted
s1=[5,7,9,1,2,3]
s2 = sorted(s1)
print (s2)
print (s1)

#switch case in python
def switch(choice):
    switcher={
        'Ayushi':'Monday',
        'Megha':'Tuesday'
    }
    print(switcher.get(choice))
switch('Megha')

#Count the Number of Each Vowels:
vowels = 'aeiou'
# change this value for a different result
ip_str = 'Hello, have you tried our turorial section yet?'
ip_str = ip_str.lower()
# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
# count the vowels
for char in ip_str:
   if char in count: #counts have vowels letters
       count[char] += 1
print(count)

keys = {'a', 'e', 'i', 'o', 'u' }
v = 'aeio,'
vowel = dict.fromkeys(['gunal','sures'],1)
print(vowel)

#Change uppecase using ORD():
s='mari'
for char in s:
    s_val = (ord(char)-32)
    print (chr(s_val),end="")