n1 = int(input("primul numar: "))
n2 = int(input("al doilea numar: "))
n3 = int(input("al treilea numarul: "))
if ((n1>0)and(n2>0)and(n3>0)):
    if (n2>n3):
        print(n2)
    if (n3>n2):
        print(n3)
    else:
        print(n2, n3)
else:
    print(n1 + n2)