
values = [1, 2, "rahul", 4, 5]
# list of the data types that allows multiple values and can be different types

print(values[0])   # 1
print(values[3])   # 4
print(values[-1])   # 5
print(values[1:3])   # 2 and "rahul"
values.insert(3, "shetty") # to add new index after rahul
values.append("End") # [1, 2, "rahul", "shetty", 4, 5, "End"]
print(values)

values[2] = "RAHUL"  # update "rahul" to "RAHUL"

del values[0]  # delete value

print(values)




