import re 

# mytext = "nazar@gmail.com, +3666555000, nazar@ukr.net,+3666555022 nazar@mail.ru, Bukmeker@gmail.com, nazar 1996"
# # \d any number 0-9
# # \D any non number
# # \w any symbol
# #\W any non symbol
# #\s space
# #\S non space
# textlookfor  = r"@\w+\.\w+" # [A-Z a-z], [0-9]{10}, 
# result = re.findall(textlookfor, mytext)
# print(result)

filename = "./emailtable.txt"
results = "./results.txt"

inputfile = open(filename, mode='r', encoding='latin-1')
results =   open(results, mode='w', encoding='latin-1')
mytext = inputfile.read()
lookfor = r"[\w.-]+@[A-Z a-z-]+\.[\w.]+"
globalresults = re.findall(lookfor, mytext)

for item in globalresults:
    print(item)
    results.write(item + "\n")
