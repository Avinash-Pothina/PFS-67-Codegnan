#function: a function is nothing but running smae part of code by calling the function name
''' advantage:
to avoid repeatation of code
to keep the code clean
to make documentation simple and understandable.
'''
#user-defined functions: function created by programmer is nothing but user defined function.
# def is a keyword to specify the function name
# parameters: the values which are passed with the function

# below function is a no parameter and no return value function
'''name=input("Enter name: ")
def func1(): #func()==> function name. the code inside this function is known as function body
    print("this is func")
func1() #callgn fucntion by function name==> func()

# below function is a paramter with no return value
def func2(name): #name==> is parameter in this function
    print("hello "+name)
func2(name)

# below function is a no paramter with return value
def func3(): 
    return "hello world"
print(func3())  # we have to use print statement to print the return value from the function

#below fucntion is parameter wiht return value
def func4(name):
    return "hi "+name
print(func4(name))

#function to return multiple values
a=int(input("enter num:"))
b=int(input("enter num:"))
def calc(a,b):
    add=a+b
    sub=a-b
    return "addition and subtraction of given 2 numbers are "+str(add)+" and "+str(sub)
print(calc(a,b))

#positional arguments: arguents whihc matched based on thier position
c=int(input("enter age: "))
def func5(name,c):
    print("Name:",name)
    print("age:",c)
func5(name,c)

#keyword arguments: sending data to the function itself using equalto "=" in irrespective of order
print("printing data usning keyword argument:")
def func6(name,age):
    print(name)
    print(age)
func6(age=c,name=name)  #age=c,name=name  <== this is a keyword argument 

#default arguments: setting data in the function name itself
def func7(name="Student"):
    return "hello "+name
print(func7())

#variable length arguments: an argument which takes number of arguments without declaring a variable in the parameter
#*args= it collects multiple positional argyuments using tuple 
def func8(*num):  #*num <== is the variable length argument whihc accepts elemnets dynamically
    s=0
    for i in num:
        s+=i
    return s
print(func8(1,2,3,4,5,6,7,8,9))
#name="avi"
#c=21
#keyword variable length arguments(**kwargs)= results output as a dictionary format. accpets dynamic arguments wiht argument name and argument variable  
def st_det(**details): #**details <== keyword arguments
    return details
print(st_det(name=name,age=c,city="Hyd"))  #(name=name,age=c,city="Hyd")  <== keyword arguments

#printing with both arguments and keyowrd arguments.
def func9(*args,**kargs):
    print(args)
    print(kargs)
func9(1,2,3,name=name,age=c)'''


#scope: scope is the region of a program where a variable can be accessed.
'''
types of scopes:
--> local scope
--> global scope
'''
#local scope: a vraiable created inside a function
print("Local scope: ")
def func10():
    name="avi"
    age=21
    print("Name:",name)
    print("age:",age)
func10()
#print(name) #returns error because name is a local variable in func10
#values changes when we have same local variable name in different functions   code:
def fir():
    x=10
    print(x)
def firs():
    x=100
    print(x)
fir()
firs()


#global scope: varaibles declared outside the function which we can access in any function
name="arun"
age=21
def func11():
    print(name)
    print(age)
func11()
#local scope has more preference than global scope
def func12():
    name="arjun"
    print(name)
    print(age)
func12()

#code to change global variable ina function
x=1233
print("Value of x before changing by the fucntion:",x)
print("Value of x after changing by the fucntion:",end=" ")
def func13():
    global x
    x=123
func13()
print(x)

#pass by value and pass by reference
#pass by reference: the original value will be changed if the value is changed inside the function
#pass by value: a copy of value passed inside the function but original value will not be changed if the value is changed inside the function
def func14(x):
    xi=20    #here x is just a copy of a where a value will not be changed if the x value is changed 
    print("Inside func:",xi)
a=10
func14(a)
print("Outside func:",a)
#print("Outside func:",xi)    #raises an error

'''
a--> 10
calling func func14(a)
xi recieves a reference to the same integer object
xi = 20
before:
a --> 10 and xi--> 10
after:
a-->10 and xi --> 20
'''

#pass by reference: the original value will be changed from inside the function
def func15(data):
    data.append(40)
val=[10,20,30]
print("pass by reference example, before changing values:",val)
func15(val)
print("pass by reference example, after changing values:",val)


