
# # --- Basic Python list example ---
# my_list = [10, 20, 30]
# print("Original list:", my_list)

# name = "khaled"
# age = 40
# student = True

# print ("my name is", name)
# print ("My age is", age, "years old")
# print ("student status: ", student)

# favorites = ["coding", "swimming", "coffee", "music", "python"]
# print(favorites[0])
# print(favorites[-1])
# favorites.append("reading")
# print(favorites)

# profile = {
#   "name": "khaled gawesh",
#   "age": 40,
#   "skills": ("reading", "coding", "gaming"),
#   "is_employed": True
# }

# print(profile["name"])
# print(profile["skills"][1])
# profile["country"] = "egypt"
# print(profile)

# my_list.append(40)
# print("After append:", my_list)
# my_list.remove(20)
# print("After remove 20:", my_list)
# del my_list[0]
# print("After deleting index 0:", my_list)

# # --- List of numbers from 1 to 100 ---
# numbers_1_to_100 = list(range(1, 101))
# print("Numbers from 1 to 100:", numbers_1_to_100)

# # --- Sum of all even numbers from 1 to 100 ---
# even_sum = sum(x for x in numbers_1_to_100 if x % 2 == 0)
# print("Sum of all even numbers from 1 to 100:", even_sum)

# e= []
# o= []
# for i in range(1, 101):
#     if i % 2 == 0:
#         e.append(i)
#     else:
#         o.append(i)
# print("Even numbers1:", e)

# print("Odd numbers1:", o)



# # other method
# even2= []
# odd2= []
# for i in range(1, 101):
#     if i % 2 == 0:
#         even2.append(i)
#         continue
#     else:
#         odd2.append(i)
# print("Even numbers2:", even2)
# print("Odd numbers2:", odd2)

#Function Expression
#Function Declaration

# age = 25

# if age >= 60:
#   print("you are a senior")
# elif age >= 18:
#   print("you are an adult")
# else:
#   print("you are underage")

skills = ["reading", "coding", "gaming", "python", "swimming"]

for skill in skills:
  print(skill)