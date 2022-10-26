import random

def alter(dlzka = 5)->str:
    sam="aeouy"
    spol="qwrtpsdfghjklzxcvbnm"
    fin=""
    for i in range(dlzka):
        fin+=random.choice(spol)
        fin+=random.choice(sam)
        # index=random.randrange(0,len(spol))
        # fin+=spol[index]
    return fin.capitalize
print (alter())
