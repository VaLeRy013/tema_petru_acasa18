ama = int(input(" numarul bilelor albe mari: "))
rma = int(input(" numarul bilelor rosii mari: "))
vma = int(input(" numarul bilelor verzi mari: "))
ami = int(input(" numarul bilelor albe mici: "))
rmi = int(input(" numarul bilelor rosii mici: "))
vmi = int(input(" numarul bilelor verzi mici: "))
bile_mari = ama + rma + vma
bile_mici = ami + rmi + vmi
print("Pe masa de biliard sunt",bile_mari + bile_mici,"bile in total")
if (bile_mari > bile_mici):
    print("Bile mari: ", bile_mari)
elif (bile_mici > bile_mari):
    print("Bile mici: ", bile_mici)
else:
    print("Numarul de bile mari si mici este egal", bile_mici)
if ((ama + ami) > (rma + rmi)) and ((ama + ami) > (vma + vmi)):
    print("Bilele albe sunt cele mai multe: ",ama + ami)
elif ((rma + rmi) > (ama + ami)) and ((rma + rmi) > (vma + vmi)):
    print("Bilele rosii sunt cele mai multe: ",rma + rmi)
elif ((vma + vmi) > (rma + rmi)) and ((vma + vmi) > (ama + ami)):
    print("Bilele verzi sunt cele mai multe: ",vma + vmi)
elif ((ama + ami) == (rma + rmi)) and ((ama + ami) > (vma + vmi)):
    print("Bilele albe si rosii sunt cele mai multe: ",ama + ami)
elif ((ama + ami) > (rma + rmi)) and ((ama + ami) == (vma + vmi)):
    print("Bilele albe si verzi sunt cele mai multe: ",ama + ami)
elif ((vma + vmi) == (rma + rmi)) and ((ama + ami) < (vma + vmi)):
    print("Bilele rosii si verzi sunt cele mai multe: ",rma + rmi)
elif ((ama + ami) == (rma + rmi)) and ((ama + ami) == (vma + vmi)):
    print("Numar egal de bile",ama + ami)
 