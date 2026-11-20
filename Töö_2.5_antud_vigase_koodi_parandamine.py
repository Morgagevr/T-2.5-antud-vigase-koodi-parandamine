


    #Lisaülessanne:

    
#     Muuda programmi nii, et alguses kuvatakse men�� ja kasutaja valib, millist osa k�ivitada:

 

# Vali programm:
# 1 - Ruutvõrrand
# 2 - Palga arvutamine
# 3 - Parkimise hind
# Sisesta valik (1-3) =>

# Käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.

#     Lisa ruutv�rrandi osasse kontroll: kui a = 0, kuvatakse teade Tegemist ei ole ruutvõrrandiga.
#     Palga osa ei tohi lubada sisestada nulli või negatiivset tunnitasu.

print("vali programm")
print("1- Ruutvõrrand")
print("2- Palga arvutamine")
print("3- Parkimise hind")

Programm=int(input("vali programm (1,2,3):"))
if Programm==1 :
        print("Ruutvõrrandi lahendamine") #Tuli lõpetada sulg
        a=float(input("Sisesta a => "))
        b=float(input("Sisesta b => "))  #Tuli lõpetada sulg
        c=float(input("Sisesta c => ")) #float tuli lisada
        D = b*b - 4*a*c
        if D>0:   #Koolon oli puudu
            x1=(-b+D**0.5)/(2*a)  #Sulud olid puudu 
            x2=(-b-D**0.5)/(2*a)
            print("Kaks lahendit:", x1, x2)
        elif D==0:  #Else if vahetada elif-i vastu ja ekstra "=" oli vaja
            x=-b/(2*a)
            print("üks lahend:", x)
        else:
            print("Reaalarvulised lahendid puuduvad") #Identatsioon oli puudu
            print()
elif Programm==2 :
        print("Palga arvutamine")
        tunnid=float(input("Sisesta töötunnid nädalas => "))
        tunnitasu=float(input("Sisesta tunnitasu (€) => "))
        if tunnid<0 and tunnid>168:
            print("Vigane tundide arv")
        elif tunnid<=40:
            palk=tunnid*tunnitasu
            print("Nädalapalk:", palk, "€")
        else:
            palk=40*tunnitasu+(tunnid-40)*tunnitasu*1,5
            print("Nädalapalk koos ületundidega:", palk, "€")
            print()
elif Programm==3 :
        print("Parkimise hind")
        tunnid=int(input("Sisesta parkimise aeg tundides => "))
        if tunnid<=0:  # = ja < olid vastupidised
            print("Vigane aeg")
        elif tunnid>=3:
            print("Hind: 5 €")
        elif tunnid>=8:
            print("Hind: 10 € (p�evapilet)")
        else:     #koolon oli puudu
            print("Hind: 2 €") #sulg oli vaja lõpetada

else:
    print("See pole valikus")