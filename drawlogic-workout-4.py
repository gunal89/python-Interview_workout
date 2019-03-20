from __future__ import print_function
#pyramid
num= input()
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,2*i+1):
        print ("*", end="")
    print()
#pyramid-2
rows = input()
for i in range(rows):
    print (" "*(rows-i-1)+"*"*(2*i+1))


