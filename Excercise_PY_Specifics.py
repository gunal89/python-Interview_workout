# Generator
def example_generator(number):
    for n in range(number):
        yield n


ret_generatot = example_generator(10)

print(ret_generatot.next())
print(ret_generatot.__iter__())
print (dir(ret_generatot))

# Decorator
def star_fun(fn):
    def inner_star_fun(*args):
        print "*" * 24
        fn(*args)
        print "*" * 24
    return inner_star_fun


def hypen_fun(fn):
    def inner_hypen_fun(*args):
        print "-" * 24
        fn(*args)
        print "-" * 24
    return inner_hypen_fun


@hypen_fun
@star_fun
def printname():
    print ("Aadhira <--> Marimuthu")


printname()

# List Comprehension 1.if 2.if with else
list_comp_if = [num for num in range(1, 100) if num % 10 == 0]
print "List comprehension-IF :", list_comp_if
list_comp_else = [num if num % 10 == 0 else "odd" for num in range(1, 100)]
print "List comprehension-ELSE :", list_comp_else

# Dict Comprehension

dict_comp = {i: i**2 for i in range(10)}
print "dict_comp", dict_comp
print zip([1, 2], [3, 4], [5, 6], [7, 8])
# Nested Loop (transpose Example)
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)


for i in range(len(matrix[0])):
    trans = []
    for row in matrix:
        trans.append(row[i])
    print trans

# Lambda and Map
my_list = [1, 5, 4, 6, 8, 11, 3, 12, 14, 20]
lamb1 = map(lambda n: n**2, my_list)
print lamb1

name = "Aadhira-Marimuthu"
nums = "12345"
ex_map = map(printname(), name)
num_str = map(int, nums)
print ex_map
print num_str

