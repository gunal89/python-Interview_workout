import json
# 42 is an instance of the type int.   42 is an int object

''' A hash function takes a message of arbitrary length and generates a fixed length code.A hash function may give the same hash value for distinct messages.'''
#Verify STRING has balanced parenthesis:
st = 'dagsj(gdad)))sdsss(dssdgunal sta;lin prasanna suresh(()('
count1 = 0
count2 = 0
for i in st:
    if i == '(':
        count1+=1
    elif i == ')':
        count1-=1
print ("STRING has balanced parenthesis" if count1==0 else "STRING has not balanced parenthesis")
'''
with open("D:\\Log_Portal\\Exported JSONs\\DashBoard.json") as jfl:
    jl = json.loads(jfl.read()) # only acceptinf String
    #jl = json.load(jfl) # accepting file object
    print jl
    print type(jl)'''

#word occurance:
def word_count(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word]=1
    return count

print(word_count('the quick brown fox jumps over the lazy dog.'))

#if condition using type():
l = [1,2,3,4,[5,6],7]
for i in l:
    if type(i) == list:
    #if isinstance(i,list):
        for j in i: print j
    else: print i, type(i)


