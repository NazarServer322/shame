import os
import datetime
import random
import sys
# figure = int(input("enter the number of firura"))
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
#
#     print("more than nine end the list")
# else:
#     print("end")

# enter_mount = str(input("enter the mounth"))
#
# if enter_mount == "Januvery":
#     print("31")
# elif enter_mount == "Fabuary":
#     print("28")
# elif enter_mount == "Mart":
#     print("31")
# elif enter_mount == "April":
#     print("30")
# elif enter_mount == "May":
#     print("31")
# else:
#     print("wrong")

# noize = int(input("Enter the number of noize"))
#
# if noize == 130:
#     print("humer")
# elif noize == 106:
#     print("gaze")
# elif  noize == 70:
#     print("alarm")
# elif  noize == 40:
#     print("qviet room")
# elif noize < 129 or  noize > 107:
#     print("betwen humer and gaze")
# elif noize  < 69 or noize < 39:
#     print("bettwen rom and alarm")

# inputmoney = int(input("Enter money: "))
# if inputmoney == 1:
#     print("Джордж Вашингтон")
# elif inputmoney == 2:
#     print("Томас Джефферсон")
# elif inputmoney == 5:
#     print("Авраам Линкольн")
# elif inputmoney == 10:
#     print("Александр Гамильтон н")
# elif inputmoney == 20:
#     print("Эндрю Джексонн")
# elif inputmoney == 50:s
#     print("Улисс Грантн")
# elif inputmoney == 10:
#     print("Бенджамин Франклинн")
# else:
#     print("wrong number")

# enterholyday = str(input("Enter holyday"))
# enterdata    = str(input("Enter date"))
# if enterholyday == "New Year" and enterdata == "1 january":
#     print("exelent")
# elif  enterholyday == "Birth" and enterdata == "11 october":
#     print("happy birhday Nazar")
# else:
#     print("wrong")

# name = ""
#
# while name != "Nazar":
#     print("Enter Nazar if you wonna leave from loop")
#     name = input()
# print("Enter nazar thank you")

# while True:
#     print("Enter name if you want to leave from loop: ")
#     name = input("Enter name Nazar if want to leave from loop: ")
#     if name == "Nazar":
#         break
# print("you are good dam right")

# while True:
#     name = input("Enter Nazar if you want to continue")
#     if name != "Nazar":
#         continue
#         print("Enter your password if you want to leave from loop")
#     password = input("enter your pass if  want to live")
#     if password == "123":
#         break
#     print("access acept")


# print("check several times")
# for i in range(2, 10):
#     print("prints")

# for i in range(5):
#     print(random.randint(1, 100))

def randomname(name):
    if name == 1:
        return "Nazar"
    elif name == 2:
        return "Stas"
    elif name == 3:
        return "Ivan"
    elif name == 4:
        return "Andrew"
    elif name == 5:
        return "Misha"
    elif name == 6:
        return "Dasha"
    elif name == 7:
        return "Anastasia"
    elif name == 8:
        return "Alex"
    elif name == 9:
        return "Oleg"
# r = random.randint(1, 9)
# fortuna = randomname(r)
# print("Hwo nex die :", fortuna)

def casino(lucky):
    if lucky == 1:
        return "black"
    elif lucky == 2:
        return "RED"
# r =random.randint(1, 2)
# fortuna = casino(r)
# print("if RED you are rich: ", fortuna)


# while True:
#     print("always return")
#     name = input("enter exit if you want to leave")
#     if name == "exit":
#         sys.exit()
#     print("chao")
#x = 100
# while True:
#     for x in range(1, 100):
#         r = random.randint(1, 100)
#         # t = x(r)
#         print(x)
#         if x == 55:
#             break
#     if x == 55:
#         break
# print("you are genius")

# superrandom = random.randint(1, 20)
# print("Try to answer the right number ")
# for x in range(1, 7):
#     # print(x)
#     # print(superrandom)
#     answer = int(input("try to guess"))
#     if answer < superrandom:
#         print("less than answer")
#     elif answer > superrandom:
#         print("more than answer")
#     else:
#         print("norm")
# if answer == superrandom:
#     print("you are the genius!" + str(x))
# else:
#     print("wrong you are the loser!" + str(superrandom))
# r = random.randint(1, 7)
# print(r)


def hello(name):
    print("Hello you are?", name)

#
# hello("Jon")
# hello("Jeck")

# def math(a , b):
#   c =   a + b
#   print(c)
#
#
# def tryblobal():
#     global wrong
#     wrong = 10
#
#
# tryblobal()
# print(wrong)

# def divide(divideby):
#     try:
#         return 11 / divideby
#     except ZeroDivisionError:
#         print("don't even try divide by zero this wrong")
#
# print(divide(2))

# def colapz(number):
#     for x in range(1,11):
#         try:
#             number = int(input("Enter the number"))
#         except ValueError:
#             print("wrong")
#         if number %2 == 1:
#             print("can't ")
#         elif number %2 == 0:
#             print("can")
#         else:
#              print("some things wrong")
#
# colapz(5)
