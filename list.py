#l.sort() sorts list in the same list where as sorted(l) should be stored in separate list
l=[50,20,10,40,30]
print("list: ",l)
print("length: ",len(l))
print("maximum element: ",max(l))
print("minimum element: ",min(l))
print("sum of elemnts: ",sum(l))
print("sorted list: ",sorted(l))
print("appedning 90")
l.append(90)
print("list after qappending 90:",l)
l.extend([60,70]) # adds the given list to the l
print("list after using extend method:",l)
l.insert(1,80)  # used to insert the element at a specific place with index
print("list after using insert method to plave 80 at index 1:",l)
l.reverse() # reverse elemnsts in the list in place
print("reversed list",l)
l.reverse()