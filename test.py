
# age  = int(input("Enter your age: "))

# if age > 1 and age < 7:
#     print("you are the child")
# elif age >= 8 or age >= 17:
#     print("you are tenager")
# elif age >= 18 and age < 29:
#     print("you are older")
# elif age >= 30 and age < 49:
#     print("you are old")
# elif age == 50:
#      print("you are fifty cent")
# elif age >= 51:
#     print("you are  sinior")
# else:
#     print("nothing")

# x = 2 
# if isinstance(x, int):
#     print("yes  x this is number")


# x = "STRING"
# if isinstance(x, str):
#     print("yes : " + x + " this is STRING")

# superlist = [10, 12 ,13]  ##  Check list if there we have 10 print super list
# if  10 in superlist: ## here we cheking
#     print("ten in super list") ### print

# if "Nazar" in "Nazar_Mulko":
#     print("Nazar in the list")
# else:
#     print("nofing")
#dict_one = {1:"one", 2:"two", 3:"three"}

# if 1 in dict_one: #### here we check  key on dict
#     print("we have one there")


# if "one" in dict_one.keys(): ## here we check the values in dict
#     print("we have one there")


# if len(dict_one) < 40:    #### here we check how long the dict with hepl *len*
#     print("dict less than 10") 
# elif len(dict_one) > 10:
#     print("dict more than 10")


##################################### LOPS ###########################################################################
# variable = 10
# while  variable != 15:
#     print("hello i will be working forever if you dont make variable += 1")
#     variable +=1

# enter_number =  input("enteter number")
# enter_fale = False

# while  not enter_fale: 
#     if len(enter_number) != 10:
#         enter_number = input("enter more some numbers")
#         print("less than 10")
#     elif len(enter_number) == 10:
#         enter_fale = True
#         print("we off from loop")

############################################# FOR #######################################################################

# for  text in range(10 , 100 +1):
#     print(text)

# for text in range(len("surprise mothafucker")):
#     print(text)

# dict_one = {1:"Bil", 2:"Jon", 3:"Tony"}

# name = dict_one.get(1)
# print(name)
# for  x in dict_one:
#     print(dict_one)


############################################# BREAK #########################################################################

# for text in range(10):  Here all thinks we can get if text == 4 we breake the cicle
#     if text == 4:
#         break
#     print(text) 




######################################### continue  and else #########################################################################

# for text in range (10):
#     print(text)
#     if text == 4:
#         break
#     else:
#         print("ok")



################################################## Try Ecept ###########################################################################
# Try except we use when we gonna try something with error and  want to avoid them without any brake code
# a = " i don't wonna work without try except"
# b = 2
# try:
#     a * b
# except(TypeError):
#     print("type")
# except Exception as e:
#     print(e)
# else:
#     print("else")
# finally:
#    print("finally") # finally use when we want to end the list even if we hava there some mistakes or don't have any mistake but we anyway want to end the loop 