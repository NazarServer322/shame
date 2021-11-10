import copy
# figure = int(input("enter the number of firura"))
#
# if figure == 1:
#     print("this super figura with one ")
# elif figure == 2:
#     print("this super figura with two ")
# elif figure == 3:
#     print("this super figura with three ")
# elif figure == 4:
#     print("this super figura with four ")
# elif figure == 5:
#     print("this super figura with five ")
# elif figure == 6:
#     print("this super figura with six ")
# elif figure == 7:
#     print("this super figura with seven ")
# elif figure == 8:
#     print("this super figura with eigth ")
# elif figure >= 9:
#     # exit
#     print("more than nine end the list")

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

# for x in range(1, 5):
#     massage = ["Hello", "ASK ME SOMETHING", "JiM", "ERICK", "KAIL", "STAN", "ERICK"]
#
#     print(massage[random.randint(0, len(massage)-1)])

# spam = ["one", "two", "three", "four", "five"]
# cheese = spam
# cheese[1] = "five"
# print(cheese)
# print(spam)




#hello(samp)
#print(samp)


#linux = ["Ubuntu", "RedHat", "Amazon", "Kali", "Centos"]
# linuxcopy = copy.copy(linux)
# linuxcopy[2] = "Hello there"
# print(linuxcopy)
# print(linux)
# print(linux[2][0:3])
# print(linux[1])
# print(len(linux))
# del linux[2][2]
# print(linux)
# for i in range(0, 5):
#     print("Chose the OS")
#     name = input("Enter the OS: ")
#     if name in linux:
#         print("we have that name")
#         break
#     else:
#         print("we don't have that name")
# print(linux.index("Amazon"))
# mark = "Hello"
# print(tuple(linux))
# print(list(linux))
# print(list(mark))
def hello(someparameter):
    someparameter.append("hello my friend")
samp = [1, 2, 3, 4]
def task(Jim):
    Jim = []

    #enter = str(input("Enter the  some things"))
    for x in range(1, 5000):
        name = str(input("enter the name"))
        Jim.append(name)
        if name.startswith("0"):
            break
    Jim[-2] = "and"
    print(" ".join(Jim))
#task("name")

# dict = {"Nazar":"October 11", "Misha":"November 20", "Guobis":"April 25", "Dima":"April11"}
# print(dict)

# while True:
#     name = input("Enter the name")
#     if name in dict:
#         print("Nice " + name + " in the dict")
#     elif name.startswith("0"):
#         print("ops we leave")
#         break
#
#     else:
#         print("we don't have that name enter tha date and we will update our database ")
#         bday = input()
#         dict[name] = bday
#         print("data base update")
#     print(dict)
#dict = {"Nazar":"October 11", "Misha":"November 20", "Guobis":"April 25", "Dima":"April11"}
#print(dict)
# print(dict.items())
# print(dict.values())
# print(dict.keys())
# print(dict.get("Nazar"))
# name = str(input("Enter the key: "))
# if name not in dict:
#     lastname = str(input("value: "))
#     dict[name] = lastname
# else:
#     print("Name in the dict")
# print(dict)

# dict.setdefault("Number", "two")
# print(dict)
