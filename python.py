
# print("ENTER NUMBER:")
# a = int(input())
# print("ENTER SECOND NUMBER")
# b = int(input())

# c = a + b
# print(c) 


# list = ["somekind of city", "strange city"]

# for x in list:
#     print(x)
######################MATH#######################################################
# a = 1
# b = 3 
# c = a + b
# c = b -a 
# c = a * b
# c = b / a
# c = a % b 
# print(c)

#########################FIND THE TYPE OF ELEMENT################################
# a = '10'

# print(type(int(a)))


# a = "Hello my \t frick \nfriend"

# print(a[1:25])

######################################FORMAT###############################################################
# b = 'Hello {name} are you {lastname} ? and your birth {birth}? '.format(name="Nazar", lastname="Mulko", birth="10.11.96") # first type of format and we have other choice

# a = " $$$ Hello my dear friend $$$"
# print(len(a))
# print(a.lower()) # all  words becom low
# print(a.upper()) # all words becom UPPER
# print(a.title()) # firs wodr  in any wodrs becom upper
# print(a.count("e")) # summa e in list
# print(a.find("e")) # with the number start e in list, in my  with 1 becouse 0 it"s H and 1 it's e
# print(a.replace("e", 'a'))# replace   word in  string in my bisnes replece all "E" in "A"  Hallo my daar friand result
# print(a.strip('$')) # delete $ from start and end string
# print(a.split(' ')) # split  all list  in space and print that
# print(b)

# name = "Privet"
# lastname = f"Nazar: {name}"
# print(lastname)
# for x in list:   #   find number less than 15  result = 1,2,3,4,12
#     if x < 15:   #
#       print(x)   #
##############################    SORT    ############################################################
# list = [1, 2, 24, 100, 3, 4 ,12, 15 ,16 ]
# list2 = [22, 12, 66, 44, 55]

# y = list + list2
# y.sort()
# print(y)

# for x in list:
#     if x < 44:
#         print(x)
# # list.extend(list2)
# # print(list)

# # y = sorted(list)
# # list.sort()
# # print(list)
# # print(list)
 #############################REMOVE ELEMENT###########################################################
# list = [1, 2, 2,  24, 100, 3, 4 ,12, 15 ,16 ]
# list2 = [22, 12, 66, 44, 55]
# #list.remove(2) # here we select list and delete number 2 from list  but we can delete only one argument
# #y = list.pop(-1) #Here I'm delete last elemet from list it's was 16, but firs of all i need create new par  it's y = list.pop

# print(list)

#######################FIND THE INDEX##############################################################
# list = [1, 2, 2,  24, 100, 3, 4 ,12, 15 ,16 ]
# list2 = [22, 12, 66, 44, 55]
# list.insert(2, "Hello my dear friend") here we change 2  in Hello my dear friend
# #y = list.index(24)  # here we find number of index in list
# print(list)


############################ DICT ##################################################################


# dict2 = {"Nazar":24, "Mulko":"one", "lastname":228, "City":"Zdolbunov"}

# #dict2.clear() ############# Here we clean our dict and after that  print clear dict
# dict2.update({"Edson":"Barboza"}) ###### here we update our dict add there plus one key + value
# del dict2["Mulko"] ### here we delete one key from dict
# print(dict2) ## here we output all dict
# print(dict2.values()) ## here we output all values from dict
# print(dict2.keys()) ## here we output all keys from dict
# print(dict2.items()) ## here we output all key and values  in out dict
# #print(sorted(dict2))# with this we sorted our dict and after that dict was sorted without any values
# copy2 = dict2.copy() # make copy of dict
# print(copy2)



###########################    SET #####################################################################

# a = [22, 45, 22, 23, 23, 55, 209, 144, 29, 40] ## here we make new list
# b = [44, 22, 22, 23, 53, 21, 66, 144, 44, 42 ] ## here we make other new list
# new = a + b ## wehe we create new object and make list  a plus b 
# new2 = set(new) ## here we make set to list and find only  original numbers withiout any dublicate
# print(new2) ## here we print two lists 
# print(a) ## here we print only one list witth dublicate