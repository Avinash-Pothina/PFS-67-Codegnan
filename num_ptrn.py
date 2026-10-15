a=int(input("enter num: "))
print("Pattern-1:")
for i in range(a):
    for j in range(1,i+2):
        print(j,end=" ")
    print()
print()

print("Pattern-2: ")
for i in range(a):
    for j in range(i+1,a+1):
        print(j,end=" ")
    print()
print()

print("Pattern-3: ")
for i in range(a):
    for j in range(1,i+2):
        print(i+1,end=" ")
    print()
print()

print("Pattern-4: ")
for i in range(a):
    for j in range(i+1):
        print(a-j,end=" ")
    print()
print()

print("Pattern-5: ")
for i in range(a):
    for j in range(1,i+2):
        print(i+j,end=" ")
    print()
print()

print("Pattern-6: ")
k=0
for i in range(a):
    for j in range(i+1):
        k+=1
        print(k,end=" ")
    print()
print()

print("Pattern-7:")
for i in range(a):
    for j in range(a):
        print(a-j,end=" ")
    print()
print()

print("Pattern-8:")
for i in range(a):
    for j in range(a-i):
        print(a-j,end=" ")
    print()
print()

print("Pattern-9:")
for i in range(a):
    for j in range(i+1,0,-1):
        print(j,end=" ")
    print()
print()

print("Pattern-10:")
for i in range(1,a+1):
    print(" "*(a-i),end="")
    for k in range(i*2-1):
        print(k+1,end="")
    print()
print()

print("Pattern-11:")
for i in range(1,a+1):
    print(" "*(a-i),end="")
    for k in range(i*2-1):
        print(i,end="")
    print()
print()

print("Pattern-12:")
for i in range(a):
    print(" "*i,end=" ")
    for j in range(a-i):
        print("*",end=" ")
    print()
print()

print("Pattern-13:")
for i in range(1,a):
    print(" "*(a-i)+"*"*(i*2-1),end=" ")
    print()
for i in range(a,0,-1):
    print(" "*(a-i)+"*"*(i*2-1),end=" ")
    print()
print()

print("Pattern-14:")
sd=input("Enter String: ")
for i in range(len(sd)):
    for j in range(i+1):
        print(sd[j],end="")
    print()
print()

print("Pattern-15:")
for i in range(len(sd)):
    for j in range(i+1):
        print(sd[i],end="")
    print()
print()

print("Pattern-16:")
print(" "*a+"*")
for i in range(1,a-1):
    print(" "*(a-i)+"*"+" "*(i*2-1)+"*")
print(" "+"*"+"*"*(i*2+1)+"*")