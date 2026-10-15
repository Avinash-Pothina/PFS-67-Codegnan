#recursion: a function calling itself until base condition is met
n=int(input("enter num: "))
def count_num(n):
    if n==0: return n
    return n+count_num(n-1)
print(count_num(n))

def fact(n):
    if n==1: return n
    return n*fact(n-1)
print(fact(n))

def fib_num(a,b,c,n):
    if n==0: return b
    a=a+b
    b=c
    c=a
    return fib_num(a,b,c,n-1)
print(fib_num(0,1,0,n))