import re 
import pyperclip

# mytext = "nazar@gmail.com, +3666555000, nazar@ukr.net,+3666555022 nazar@mail.ru, Bukmeker@gmail.com, nazar 1996"
# # \d any number 0-9
# # \D any non number
# # \w any symbol
# #\W any non symbol
# #\s space
# #\S non space
# | Chenall 

# textlookfor  = r"@\w+\.\w+" # [A-Z a-z], [0-9]{10}, 
# result = re.findall(textlookfor, mytext)
# print(result)

# filename = "./emailtable.txt"
# results = "./results.txt"

# inputfile = open(filename, mode='r', encoding='latin-1')
# results =   open(results, mode='w', encoding='latin-1')
# mytext = inputfile.read()
# lookfor = r"[\w.-]+@[A-Z a-z-]+\.[\w.]+"
# globalresults = re.findall(lookfor, mytext)

# for item in globalresults:
#     print(item)
#     results.write(item + "\n")

# print("RE")
# phonenumberNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
# mo = phonenumberNumRegex.search("my number: 415-555-5555.")
# print("wft" + mo.group())

# z = re.compile(r"\d\d\d")
# x  = z.search("333")
# print("result: " +  x.group())


# z = re.compile(r"(\d\d\d)-(\d\d\d)")
# x = z.search("111-131")
# print("try:" + x.group())

# b  = re.compile(r"\w\s\w")
# n = b.search("n w")
# print("hello this your search? " + n.group())


# z = re.compile(r"Nazar I'm | will find you")
# x = z.search("Nazar I'm  ")
# print("This is what you  exacly you  looking yor? "  + x.group())
# c = z.search(r' will find you')
# print("The second things: " + c.group())


# z = re.compile(r'Bat(wo)?man')
# x = z.search("i*M the Batman of the nigth city a'm the king of the nigth or im the batwoman")
# print("who i'm ? " + " I'm The " + x.group())

# c = z.search("Batwoman in the cyti of the nigth")
# print("grou p " + c.group())

# z = re.compile(r"\d\d\d-?\d\d\d")
# x = z.search("333-444")
# print("print the number with - " + x.group())

# z = re.compile(r" ki(n)*(i)*g ")
# x = z.search("king kinnnnnnnnnnnnnnnnnnnnng king kinnnnnng i'm the king kingkingowih king  nazarking of whole world king king king")
# print("find all of the king: " + x.group())


# z = re.compile(r"(HA){3}")
# x = z.search("HAHAHA ")
# print("how many bu bu we gonna find? " + x.group())

# z = re.compile(r"(HA){3,6}")
# x = z.search("HAHAHAHAHAHAHA ")
# print("how many bu bu we gonna find? " + x.group())

# z = re.compile(r" \w\w\w\w\w\d*")
# x = z.findall("king king king king king broo nazar3 ")
# print("i hope we find some thing"+ str(x))

# z = re.compile(r"[^13]")
# x = z.findall("ASDSASAFGASF asdf aasd asasd as as das f 1 2 3 6  3  3 z 5 ")
# print(str(x))

# z = re.compile(r"\w+\s\d+")
# x = z.findall("wdsadsad 0404040, wdasdasdsa 9494949")
# print("i hope this gonna work"+ str(x))


# z = re.compile(r'[^asd]')
# x = z.findall("a s d  b c j ")
# print("i hope this gonna work"+ str(x))


# z = re.compile(r"\w+$")
# x = z.findall("dd2d")
# print(str(x))

# z = re.compile(r".atman")
# x = z.findall("batman batman ratman fatman")
# print("atman:=======" + str(x))


# z = re.compile(r"tesla$")
# x = z.findall("mazda, minicuper, tesla")
# print("find the auto: " + str(x))


# z = re.compile(r"^mazda")
# x = z.findall("mazda, minicuper, tesla")
# print("find the auto: " + str(x))

# email = re.compile(r"[A-Z-a-z-0-9._+-]+@+[A-Z-a-z-0-9._+-]+\.*[A-Z-a-z]")

# z  = email.findall("nazarbukmeker@gmail.com mulko@gmail.com")
# print("find the email=== " + str(z))
