#house password
def checkio(vstup:str)->bool:
    status= False
    if len(vstup)>=10:
        for i in vstup:
            if i.isdigit():
                status=True
                break;
        for i in range vstup:
            if i.isupper()
                status1=True
                break;
        for i in range vstup:
            if i.islower():
                status2=True
                break;
        if status and status1 and status2:
            return True
        else:
            return False
    else:
        return False

#ULOHA refactor this one









