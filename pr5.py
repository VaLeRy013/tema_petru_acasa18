ac=int(input(" anul curent: ")) 
lc=int(input(" luna curenta: ")) 
zc=int(input(" ziua curenta: ")) 
an=int(input(" anul nasterii: ")) 
ln=int(input(" luna nasterii: ")) 
zn=int(input(" ziua nasterii: ")) 
if (ln==lc): 
    if ((zc>zn)or(zc==zn)): 
        print(ac-an,"ani") 
    else: 
        print((ac-an)-1,"ani") 
elif (lc>ln): 
    print(ac-an,"ani") 
else: 
    print((ac-an)-1,"ani")