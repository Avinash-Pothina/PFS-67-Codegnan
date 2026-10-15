# tuple is an ordered and immutable collection of data which allows duplicates and different data types
# tuple data cannot be changed once it is declared

t=("apple",25,5.8,"c")
a=(50,20,40,10,30)
print("original tuple t",t)
print("original tuple a",a)
print("slicing t",t[:2])
print("maximum element in a",max(a))
print("minimum elemnt in a",min(a))
print("sum of tuple in a",sum(a))
print("sorted tuple of a",sorted(a))
print("first element in the tuple a:",a[0])
print("addiung 2 tuples:",a+t)
print("length of tuple t",len(t))
print("index of the givne elemmt for tuple a:",a.index(10))
print(type(60))
print(type((60,)))
print(t*2)