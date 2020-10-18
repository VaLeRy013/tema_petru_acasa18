ngaini = int(input("numarul de gaini: "))
nboabe = int(input("numarul de boabe: "))
if (nboabe % ngaini == 0):
    print("Fiecare gaina primeste ",nboabe // ngaini," boabe, iar curcanul nu primeste nimic.")
elif (nboabe % ngaini !=0):
    if ((nboabe % ngaini) > (nboabe // ngaini)):
        print("Curcanul primeste cu ",nboabe % ngaini," boabe mai mult")
    if ((nboabe % ngaini) < (nboabe // ngaini)):
        print("Fiecare gaina primeste ",nboabe // ngaini," boabe mai mult")
    else:
        print("Fiecare primeste un numar egal de boabe")
