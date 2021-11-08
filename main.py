# towns = ["Zdolbunid", "RIvne", "Lviv", "Kiev", "New-Yourk", "London", "Barcelona"]

# for x in towns:
#     print(x)

# string = "AAAAAAA"
# print (string.lower())

# for x in towns:
#     if x.startswith ("Z"):
#         print(x)

# for x in towns:
#     if x.endswith ("v"):
#         print(x)
# for x in towns:
#     if x.endswith ("a"):
#         print(x)
# for x in towns:
#     if x.startswith ("L"):
#         continue
#     print(x)

# for x in towns: 
#     if x.startswith ("R"):
#         break
#     print(x)
# numbers = (12, 25, 66, 322,333)
# # print(sorted(numbers))
# print(numbers)

# number = input ("enter nubmer")
# number =  number.split (" ")
# print(number)


# from typing import SupportsIndex

# #here we enter the values and then split it 
# string = input("enter values:")
# string = string.split(" ")
# print(string)

# # here we make cicle  and convert it from string in int 
# # numbers.append  make string to int x list number take values from string and become int
# nubmers = [] 
# for x in string:
#     print(type(x))
#     nubmers.append(int(x))
# print(nubmers)

# for x in nubmers:
#     print(type(x))

# towns = ["Zdolbunid", "RIvne", "Lviv", "Kiev", "New-Yourk", "London", "Barcelona"]

# start_with_Z =[]

# for x in towns:
#     if x.startswith("Z"):
#         start_with_Z.append(x)
        
# print(start_with_Z)

# towns = ["Zdolbunid", "RIvne", "Lviv", "Kiev", "New-Yourk", "London", "Barcelona"]


# for x in towns:
#     if x.startswith("L"):
#         towns.remove(x)
        
# print(towns)
# for x in range(0, 12):
#     try:
#         print(towns[x])
#     except:
#         print("end")

# for x in range(0, 12):
#     try:
#         print(towns[x])
#     except Exception as exs:
#         print("the error {exs}")
#     else:
#         print("OK")

# towns = ["Zdolbunid", "RIvne", "Lviv", "Kiev", "New-Yourk", "London", "Barcelona"]
# towns2 = ["Zdolbunid", "RIvne", "Lviv", "Kiev", "New-Yourk", "London", "Barcelona"]

# def appending(initial_list, finding_char):
#     new_list = []
#     for x in initial_list:
#         if x.startswith(finding_char):
#             new_list.append(x)
#     return new_list
# def appending(finding_char, *args ):
#     new_list = []
#     if not args:
#         return
#     for x in args:
#         for var in x:
#             try:
#                 if  var.startswith(finding_char):
#                     new_list.append(var)
#             except Exception as exc:
#                 print(exc)
#         return new_list
# print(appending("L", towns2))
# print(appending("K", towns))
# def printing():
#     for x in towns_start_K:
#         if x.startswith("K"):
#             print("TOWN START WITH {x}")
# appending()
# printing()



# persons = {"name" : "Nazar", "Last_name" : "Mulko"}
# persons2 = dict(name2 = "Andrew")
# persons.update(persons2)

# name = persons.get("name2")

# print(name)


surname = input("Enter name:  ")
tel = {}

if surname.isupper():
    print("Upper")
