li = int(input("locul lui Ionel: "))
if (li <= 100):
    if (li % 4 == 0):
        print("Ionel va primi un tricou negru")
    elif (li % 4 == 1):
        print("Ionel va primi un tricou alb")
    elif (li % 4 == 2):
        print("Ionel va primi un tricou rosu")
    elif (li % 4 == 3):
        print("Ionel va primi un tricou albastru")
else:
    print("Ionel nu se afla intre primii 100 si nu va primi un premiu")