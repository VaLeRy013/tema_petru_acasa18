a=int(input("primul numar"))
b=int(input("al doilea numar"))
c=int(input("al treilea numar"))
if (a<b+c) and (b<a+c) and (c<b+a):
    print("Da")
else:
     print("Nu")