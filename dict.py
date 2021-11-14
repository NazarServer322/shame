Linux = {"Ubuntu":"Unix", "RedHat":"Unix", "Windows":"Microsoft", "Mac":"Unix"}
Linuxw = {"Ubuntu":{"Unix":"0"}, "Unix": {"Windows":"Microsoft"}, "Jim":{"Mac":"Unix"}}
# for x in Linux:
#     print(Linux.items())
#     print(Linux.keys())
#     print(Linux.values())

# for x, v in Linux.items():
#     print("Key: " +  x  + "  values: " + str(v))


# print(Linux.get("Ubuntu"))
# Linux.setdefault("Baykal", "Russia")
# print(Linux)

# def task(Os, desterbuter):
#     numDestr = 0
#     for x, v in Os.items():
#         numDestr = numDestr + v.get(desterbuter, 0)
#         return numDestr

# print("IDK" + str(task(Linuxw, "Jim")))

get  = input("Enter value ")
print(Linux.get(get))