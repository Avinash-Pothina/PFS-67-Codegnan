# nested loops: a loop within the loop is nothing but nested loop  # ex: loop for o(n)^2 time complexity
a=int(input("enter num: "))
print("pattern using nested loop:")
for i in range(1,a+1):
    for j in range(i,a):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
    
print("without using nested loop:")
for i in range(1,a+1):
    print(" "*(a-i)+"*"*i)

print("Pyramid:")
for i in range(1,a+1):
    print(" "*(a-i)+"*"*i+"*"*(i-1))

print("Pyramid using nested loop:")
for i in range(1,a+1):
    for j in range(a-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    for l in range(i-1):
        print("*",end="")
    print()