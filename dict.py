#dictionaries: dictionary is an ordered elements of data whihc uses key-value pairs and contains unique keys

student={"Id":1,"name":"avinash","kattappa":"sudeep"}
print("student dict:",student)
print("student id:",student["Id"])
print("student name:",student["name"])
print("student name using get method:",student.get("name"))
print("returns none if there is no attribute using get method:",student.get("salary"))


#add key
print()
student["f_subject"]="maths"
print("updated student dict after adding favourite subject:",student)
student["f_subject"]="biology practicals"
print("updated student dict after updating favourite subject:",student)
print()
#returing only keys
print("returning only keys from student dict:",student.keys())
print()
#returning only valuess
print("returning only values from student dict:",student.values())
print()
#returning only items
print("returning only items from student dict:",student.items())
print()

#returning dictionary using for loop
for i,j in student.items():
    print(i,end="")
    print(":",end=" ")
    print(j)

print()
#updating more than 1 value
student.update({
    "Id":24,
    "name":"avi"
})
print("student dictionary after updatig more than 2 values:",student)
print()

#removing item in student dictionary
student.pop("Id")
print("student dict after removing id using pop method:",student)
print()

# methods in dictionary
print("lenght of student dictionary:", len(student))
print("max of student dictionary:", max(student))
print("min of student dictionary:", min(student))
print("sorted of student dictionary:", sorted(student))
print()

student.clear()
print("student dict after using clear method:",student)
print()