def validacion_dominio (dominio):
    letraPatenteCorta = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P")
    if len(dominio) == 6:
        primerasTres = dominio [:3]
        ultimasTres = dominio[-3:]
        if ultimasTres.isdigit():
            if primerasTres.isalpha():
                if dominio[0] in letraPatenteCorta:
                    return True
                else:
                    return False 
            else:
                return False 
        else:
            return False 
    elif len(dominio) == 7:
        return True

patente = "abc123"
patente = patente.upper()
print(validacion_dominio(patente))