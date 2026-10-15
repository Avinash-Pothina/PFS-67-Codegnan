#lambda function: lambda funcion is anonymus(without name), single line and small anonymous function
#syntax for lambda function: lambda: expression
# we have to use ambda when there is a requirement of small temporary functions
#methods for lambda function: map(), filter(), sorted(), reduce()
#map(): it applies function ot every element
#filter(): it is used to filter the elements based on a condition.
#filter() --> syntax: filter(function,iteration)
#reduce(): it repeatedly applies function to elements and reduces entire sequence to one final value. it is mandatory to import functools to use reduce method

#below is lambda with 1 parameter
x=int(input("enter num: "))
s=lambda x: x*x
print(s(x))

#lambda wiht multiple parameter
y=int(input("Enter num: "))
t=lambda x,y: x+y
print(t(x,y))

#lambda wiht if else: we can add conditional statemnt of if 
u=lambda x: "even" if x%2==0 else "odd"
print(x,"is",u(x))

nums=[1,2,3,4,5]
v=list(map(lambda x:x*x,nums))
print("with lambda function:",v)

#map without lambda
def w(x):
    return x*x
res=map(w,nums)
print("without lambda functions:",list(res))

#filter()
res=filter(lambda x:x%2==0,nums)
print("using filter:",list(res))

#reduce()
from functools import reduce
add=reduce(lambda x,y:x+y,nums)
print("using reduce:",add)


#sorted
print(sorted(nums))
stri=["arun","arjun","aakash","ajay"]
print(stri)
print("sorts based on the length:",sorted(stri,key=len))

#sorting list by last character
print("sorting list by last character:",sorted(stri,key=lambda x:x[-1]))