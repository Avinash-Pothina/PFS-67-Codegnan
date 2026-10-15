#exceptional handling
#exception is an error which occurs in the program
#value error: int("Abc")
#type error: "10"+5 <-- raises error coz we are trying to concatenate string and integer
#index error: l=[1,2]==> print(l[4])  <-- raises an index error because index is out of range
#zerodivision error: 10/0  <-- raises error coz a number cannot be divided by zero
#indentation error: occurs when we havent given enough or more then the space required.
#key error: s["age"] where age doesnt exist in s dictionary so it raises key error
#file not found error: raises error when we try to open a file that doesnt exist
#name error: raises error when we print a varbale which is not declared


#valueerror
try:
    a=int(input("Enter int: "))
    print("entered number is:",a)
except ValueError:
    print("enter integer")

#Zerodivisionerror, valueerror,nameerror
try:
    a=int(input("Enter num: "))
    b=int(input("Enter num: "))
    print(a/b)
    print(c)
except ValueError:
    print("It is a value error")
except ZeroDivisionError:
    print("number cannot be divided by zero")
except NameError:
    print("It is a name error")
else:
    print("No error occured") # prints only if there was no error
finally:
    print("this is a finally block") # runs even if there was no error and if there was a error