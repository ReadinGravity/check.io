def translate(vstup:str)->str:
    i=0
    sam="aeouy"
    spol="qwrtpsdfghjklzxcvbnm"
    fin=""
    while i<len(vstup) or vstup[i] in sam.upper():
        #print(vstup[1])
        if vstup[i] in sam:
            fin+=vstup[i]
            i+=3
        elif vstup[i] in spol:
            fin+=vstup[i]
            i+=2
        else:
            fin+=vstup[i]
            i+=1
    return fin

print(translate("hieeelalaooo"))

print(translate("hieeelalaooo") == "hello")

