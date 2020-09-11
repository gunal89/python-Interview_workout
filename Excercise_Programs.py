# Sorting:
num_list = [4, -2, 7, 1, 10, 16, 12, 9, 14]
def_sort = sorted(num_list)
print "Sorted List-1 :", (def_sort)
sortlist = list()
while num_list:
    f_val = num_list[0]
    for num in num_list:
        if f_val > num:
            f_val = num
    num_list.remove(f_val)
    sortlist.append(f_val)
print "Sorted List-2 :", (sortlist)

# Largest Number:
num_list = [4, -2, 7, 1, 10, 16, 12, 9, 14, 20]
print "Largest Number-1 :", (max(num_list), min(num_list))

def_sort = sorted(num_list)
print "Largest Number-2 :", (def_sort[-1])

lar1_num = num_list[0]
lar2_num = 0
for l_num in num_list:
    if lar2_num < l_num:
        if l_num > lar1_num:
            lar1_num, lar2_num = l_num, lar1_num
        else:
            lar2_num = l_num
print "Largest Number-3 :", (lar1_num, lar2_num)

# Smallest Number:
num_list = [4, -2, 7, 1, 10, 16, 12, 9, 14, 20]
print "Smallest Number-1 :", (min(num_list))

def_sort = sorted(num_list)
print "Smallest Number-2 :", (def_sort[0])

s1_num = num_list[0]
s2_num = int()
for s_num in num_list:
    if s2_num > s_num:
        if s1_num > s_num:
            s1_num, s2_num = s_num, s1_num
        else:
            s2_num = s_num
print("Smallest Number-3 :", s1_num, s2_num)

# Reverse Number:
n = 123456
rev_num = int()
while n > 0 :
    remainder = n % 10
    rev_num = (rev_num*10)+remainder
    n = n // 10
print "Reverse_Number-1", rev_num

# Reverse String:
s = "Aadhira Gunal"
print "Reverse String-1 :", s[::-1]
slist = list(s)[::-1]
print "Reverse String-1(a):", (''.join(slist))

rev = ""
for char in s:
    rev = char + rev
print "Reverse String-2 :", (rev)

# Factorial
fac_num = 7
fac = 1
for f in range(fac_num, 1, -1):
    fac = fac*f
print "Factorial :", (fac)

# Fibonacci
count = 0
n1 = 0
n2 = 1
nr = 0
while count < 10:
    print (n1)
    nr = n1+n2
    n1=n2
    n2=nr
    count += 1

# Armstrong number
number_to_check = 407
arms_num = 0
len_num = len(str(number_to_check))
for anum in str(number_to_check):
    arm_num = pow(int(anum), int(len_num))
    arms_num += arm_num
if number_to_check == arms_num:
    print "{} --> is an Armstrong Number".format(number_to_check)
else:
    print "{} --> is not an Armstrong Number".format(number_to_check)

# Modify Tuples:
tuples = (1, 2, 3, 4, 5, 9)
tup_list = list(tuples)
tup_list.insert(2,100)
list_to_tuple = tuple(tup_list)
print list_to_tuple


# Character occurances and max-frequency:
proverb = "Make have while the sunshines"
vdict = {}
dict1 = vdict.fromkeys(proverb.strip(), 0)
for v in proverb:
    if v in dict1.keys():
        dict1[v] += 1
print dict1


max_val = 0
key_max = str()
for d_key, val in dict1.items():
    if val > max_val:
        max_val = val
        key_max = d_key
print "key_max, max_val", key_max, max_val

# Vowels count:
vowel = 'aeiou'
prov = "Face the failure until failure fails to face you"
dict_vow = dict()
vowel_dict = dict_vow.fromkeys(vowel, 0)
for p in prov:
    if p in vowel_dict.keys():
        vowel_dict[p] += 1
print "Vowels count-1 :", vowel_dict

v_dict = dict()
for ch in prov:
    if ch in vowel:
        if ch in v_dict.keys():
            v_dict[ch] += 1
        else:
            v_dict[ch] = 1
print "Vowels count-2 :", v_dict

# Prime Number:
prime_check = 11
for i in range(2, prime_check-1):
    if prime_check % i == 0:
        print "{} --> is not a Prime number".format(prime_check)
        break
else:                                                      
    print "{} --> is a Prime Number".format(prime_check)

# Frequency of elements (max and min)

list_freq = [0, 0, 1, 5, 3, 5, 1, 8, 9, 7, 5, 5, 0]
freq_max = 0
freq_ele = int()
set_li = set(list_freq)
for uni_num in set_li:
    count_freq = list_freq.count(uni_num)
    if freq_max < count_freq:
        freq_max = count_freq
        freq_ele = uni_num
print "Frequency of elements (max)-1 :", freq_max, freq_ele

print "Frequency of elements (max)-2 :"
print max(set(list_freq), key=list_freq.count)
print min(set(list_freq), key=list_freq.count)

''' Total head is 34 and total Leg is 96 how many rabbits and chickens ?'''
total_heads = 34
total_legs = 96
for rab_head in range(total_heads+1):
    chick_head= total_heads - rab_head
    if chick_head * 2 + rab_head * 4 == 96:
        print "Rabbit Head - {} <--> Chicken Head - {}".format(rab_head, chick_head)

# Swapping Two Numbers
a, b = 2, 3
a, b = b, a
print a, b

# Clone or Copy Lists

li1 = [1, 2, 3]
li2 = li1[:]     # 1. copying or cloning. li1 and li2 id is different
li3 = list(li1)  # 2. copying or cloning. li1 and li2 id is different.
li4 = li1        # Assigning one list to another list. ID will be same.
print li1, id(li1), type(li1)
print li2, id(li2), type(li2)
print li3, id(li3), type(li3)
print li4, id(li4), type(li4)
