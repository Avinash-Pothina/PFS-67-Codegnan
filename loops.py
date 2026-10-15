#loop: a loop refers to running a line of statements for n times
nums=[10,20,30,40,50]
print("printing nums through index:",end=" ")
for i in range(0,5):
    print(nums[i],end=" ")
print()
print("printing nums through value:",end=" ")
for i in nums:
    print(i,end=" ")
print()


#while loop: refers to a loop whihc runs until the condition is false
print("printing 1 to 5 using while loop:",end=" ")
i=1
while i<=5:
    print(i,end=" ")
    i+=1
print()


a=int(input("enter num: "))
i=1
print("while loop:",end=" ")
while i<=a:
    if i%2==0:
        print(i,end=" ")
    i+=1
print()
print("For loop:",end=" ")
for i in range(1,a+1):
    if i%2==0:
        print(i,end=" ")
print()
print("For loop:",end=" ")
for i in range(a,0,-1):
    print(i,end=" ")
print()
print("For loop sum of n numbers:",end=" ")
k=0
for i in range(a,0,-1):
    k+=i
print(k)
for i in range(1,a+1):
    print(i*a,end=" ")
print()

#max element wihtout using max
m=nums[0]
for i in range(1,len(nums)):
    if nums[i]>m: m=nums[i]
print("max element in nums:",m)

#min element wihtout using max
m=nums[0]
for i in range(1,len(nums)):
    if nums[i]<m: m=nums[i]
print("min element in nums:",m)