students = {
    "anu" : 85 ,
    "manu" : 90,
    "asha" : 87,
    "rahul" : 85

}
print("orginal dictionary:")
print(students)
sorted_students = sorted(students.items(),key = lambda x:(x[1],x[0]))
print("sorted dictionary:")
print(dict(sorted_students))
