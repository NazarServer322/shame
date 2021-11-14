import os 
# print(os.getcwd()) # get current work directory
# os.chdir("C:\\Windows")
# print(os.getcwd())
#os.mkdir("C:\ newfolred")
#os.rmdir("C:\\ newfolred2")
# z = os.listdir("C:\\")
# if "ss" in z :

#     print("we found"+ str(z))
# elif "AMD" in z:
#     print(str(z))
# z = os.path.getsize("D:\\ubuntu-20.04.1-desktop-amd64.iso")
# print(str(z))

# totalzize = 0
# for x in os.listdir("D:\\"):
#     totalzize = totalzize 
#     os.path.getsize(os.path.join("D:\\ubuntu-20.04.1-desktop-amd64.iso"))
# print(totalzize)

# z = os.path.exists("C:\\Windows")
# print(str(z))
# z = open("C:\\text.txt", 'w')
# # x = z.read()
# # print(str(x))
# z =  z.write("bla bla bla")
# z.close()

# z.read()
# print(str(z))
#while True:
# file = open("C:\\text.txt", "a")
# file.write("bla bla bla bla bla")
# file.close()
# file = open("C:\\text.txt", "r")
# print(file.read())
# file.close()

with open("C:\\text.txt", 'r') as file:
    print(file.read())

with open("C:\\text.txt", "a") as file:
    print(file.write("new line"))

# with open("C:\\text.txt", "w") as file:
#     print("new line", file.write("some kind of shit"))