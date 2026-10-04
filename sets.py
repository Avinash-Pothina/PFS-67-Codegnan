# a set is an unordered collection of data which doesnt allow duplicates
# we cannot use indexing or slicing for sets

name={10,20,20,30,40,50,60,50,50,40}
dict={} # python declares an empty set as a dictionary
print("set:",name)
print(type(name))
print(type(dict))
name.add(90)
print("set after adding 90:",name)
s1={10,20,30}
s2={50,40,30}

print("s1:",s1)
print("s2:",s1)


#union: combines 2 sets
print("adding 2 sets:",s1|s2)
print("adding 2 sets using union:",s1.union(s2))


#intersection: returns common elements from 2 sets
print("returning common elements from 2 sets:",s1&s2)
print("returning common elements from 2 sets using intersection:",s1.intersection(s2))


#diufference: elements exist in first set but not in second set
print("subtractig s1-s2:",s1-s2)
print("subtractig s2-s1:",s2-s1)
print("subtractig s1-s2 using difference",s1.difference(s2))
print("subtractig s2-s1 using difference",s2.difference(s1))


#symmetric difference: elements that are in either set but not in both
print("returning elements which does not exist in both sets:",s1^s2)
print("returning elements which does not exist in both sets using symmetric difference:",s1.symmetric_difference(s2))


#builtin methods
print("Length of s1:",len(s1))
print("sum of s1:",sum(s1))
print("max of s1:",max(s1))
print("min of s1:",min(s1))
print("sorting name returns list instead of set:",sorted(name)) 
s2.update([60,80,70])
print("updating s2 wiht 3 different numbers",s2)
ts2=s2
s2.remove(40)
print("s2 after removing 40:", s2)
s2.pop()
print("after popping s2:",s2)
s2.discard(60)  #safest way to delete an element
print("s2 after deletign 60 using discard:",s2)
s2.discard(100)
print("used discard on s2 for removing 100 since there was 100 not existed no error raised by the compiler:",s2)
s2.clear()
print("s2 after usng clear method:",s2)