def budget(enter):
    print("WELCOM TO OUR SHOP")
    enter = int(input("Enter tne your budget"))
    print("make you choice: 1 one \n 2 two \n 3 three")
    choice = int(input("make your choice"))
    while enter != 0 or enter == "":
        if choice == 1:
            return enter - 25
            print(enter)
        elif choice == 0:
            break
            print("good luck")
        

budget(100)