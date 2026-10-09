''' difference between function  nad generator: 

function: it uses return keyword to return the value. function execution ends with return. fucntion can return collections.
a normal function executes and gives returned value.

generator: it uses yield keyword to return the value. it produces values one at a time. execution can pause at yield. 
it can generate sequence of elements. generator gives a generator object which can perform values when we ask for them.

'''



''' difference between list comprehension and generator expression:

list comprehension: uses square brackets for implementation. it stores values in list directly. immediate execution. 
list consumes larger memeory to store data. we can access values by indexing. 

generator expression: opening and closing parameters. it does not store all values at once. pause and next execution (lazy execution). 
it consumes less memory. we cannot access values directly by indexing.

'''
#list comprehenson: it is a one line representation of for loop
#syntax: [expression for variable in iterable]
#below is an example for list comprehension

n=int(input("Enter num: "))
nums=[i for i in range(1,n)]
print("nums:",nums)
print("squares of nums:",[i*i for i in nums])
names=["sam and jim are friends","ram","jim","jam"]
print("names:",names)
print("uppercase of names:",[i.upper() for i in names])
print("uppercase of first letter in names:",[i.capitalize() for i in names])
print("uppercase of each letter in names:",[i.title() for i in names])
print("printing even numbers:",[i for i in nums if i%2==0])

#filtering values
print("printing numbers greater than 2:",[i for i in nums if i>2])

#nested list comprehension: it refers to having more than 1 for loop in list comprehension
print("nested loop comprehension returning indexes of i and j:",[(i,j) for i in range(n) for j in range(i+1)])

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print("matrix:",matrix)
print("printing matrix using nested loop:",[matrix[i][j] for i in range(3) for j in range(3)])






#generators: generator generates value one at a time when required
#yield: yield passes the function and remembers its current state
#generator is used when we want to generate values at a time
def num():
    for i in range(1,n+1):
        yield i
res=num()
for i in range(1,n+1):
    print(next(res))  # we have to use next() keyword while using yield to generate next numbers like in first print 1, 2nd print 2 and so on

# ***imp*** yield vs return 
def demo():
    return 10
    return 20
print(demo())  #here it returns only 10 not 20
print(demo())
print()
def demo():
    yield 1
    yield 2
    yield 3
#using generator with for loop
r=demo()
for i in range(3):
    print(next(r))   # here yield returns more than ione number based on the given next keyword
print()
nn=(x*x for x in range(1,n+1))
print(next(nn))
print(next(nn))
print(next(nn))
print(next(nn))
print(next(nn))
print()
def even():
    for i in range(1,21):
        if i%2==0:
            yield i
print("generating even numbers till 20 using generators:")
for i in even():
    print(i)