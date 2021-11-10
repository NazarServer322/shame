import random
# cats = []
# while True:
#     print("Enter the cat name " + str(cats) )
#     name = input()
#     if name == "":
#         break
#     cats = cats + [name]
#     print("cats name are: ")
#     for name in cats:
#         print("" + name)

# dog = ["SIS", "Andrew", "ARS", "Bantik", "Kim"]
# lists = []
# for x in range(5):
#     name = str(input("Enter the name: "))
#     if  name  ==  dog:
#         print("don't name", name)
#         if name.startswith("S"):
#             lists.append
#         elif name.endswith("S"):
#             lists.append
#             print(lists)
#     else:
#         print("We have that name", name)
# x = 1
# while x < 5:
#     print(x)
#     x+=1

# x = ["something"]
# x = x + ["Test"]
# print(x)
# for x in range(10):
#     try:
#         dog  = ["SIS", "Andrew", "ARS", "Bantik", "Kim"]
#         name = str(input("enter tne name you want to delete: "))
#         dog.remove(name)
#     except Exception as exe:
#         print("AND STIIILLLL")
# # dog.index("SIS")
# # print(dog)
# # dog.append("Milka")
# # print(dog)
# # dog.insert(4, "buggatikukold")
# # print(dog)
#     print(dog)

# dog = ["SIS", "Andrew", "ARS", "Bantik", "Kim", "a"]
# dog.sort()
# print(dog)
# dog.sort(reverse=True)
# print(dog)
# dog.sort(key=str.lower)
# print(dog)

for x in range(1, 5):
    massage = ["Hello", "ASK ME SOMETHING", "JiM", "ERICK", "KAIL", "STAN", "ERICK"]

    print(massage[random.randint(0, len(massage)-1)])
