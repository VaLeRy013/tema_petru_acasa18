n1 = int(input(" prima nota : "))
n2 = int(input(" a doua nota : "))
n3 = int(input(" a treia nota: "))
if (n3>=8):
    print(n1, n2, n3)
elif (n3<8):
    if (n1>n2):
        print(n1)
    if (n2>n1):
        print(n2)
    else:
        print(n1, n2)