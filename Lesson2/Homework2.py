# Part 1
a = [7, 10, 23, -19, 80]
# 1
a1 = sorted(a)
print(a1)
# 2
b = [20, 21]
a1.extend(b)
print(a1)
# 3
a2 = sorted(a1)
print(a2)
# 4
print(a2[::2])
# 5
print(a2.count(20))
# 6
print(a2.index(20))
# 7
a2.insert(3, 19)
print(a2)

# Part 2
t = (1, 2, 3)
print(len(t))
print(t[0])
print(t*2)

# Part 3
# 1
family = ["sister", "brother", "mother"]
person = {
   "Name": "Alex",
   "Age": 23,
   "Members_of_family": family,
   "Profession": "teacher"}
# 2
print(person["Name"])
# 3
person["Profession"] = "programmer"
# 4
person["Members_of_family"].append(["father"])
# 5
print(person.keys())
# 6
person["Gender"] = "male"
# 7
person.pop("Gender")
print(person)

