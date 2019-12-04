def hello_nom(nom):
    if isinstance(nom, str):
        if len(nom) > 0:
            nom = nom[0].upper() + nom[1:]
            hello = "Hello, " + nom
            return hello
        else:
            return "error"

    else:
        return "error"


def hello_cri(nom):
    if nom.isupper():
        return "HELLO, " + nom + " !"
    else:
        return "error"


def hello_blank(string):
    if is_blank(string):
        return "Hello, my friend"
    else:
        return "error"


def is_blank(string):
    boolean_is_blank = True
    if len(string) != 0:
        i = 0
        while i < len(string) and boolean_is_blank == True:
            if string[i] != " ":
                boolean_is_blank = False
            i += 1
    return boolean_is_blank


def hello_deux_noms(noms):
    i = 0
    while noms[i] != ',' and i < len(noms):
        i += 1
    nom1 = noms[0:i+1]
    nom2 = noms[i+1:]
    nom2 = nom2[0].upper() + nom2[1:]
    return hello_nom(nom1) +' ' + nom2


def hello_plusieurs_noms(noms):
    nom = ""
    noms_traites = ""
    j = 0
    for i in range(0, len(noms)):
        if noms[i] == ",":
            nom = noms[j:i + 1]
            nom = nom[0].upper() + nom[1:]
            noms_traites += nom + " "
            j = i + 1
    nom = noms[j:]
    nom = nom[0].upper() + nom[1:]
    noms_traites += nom
    return hello_nom(noms_traites)


def hello_plusieurs_noms_cris(noms):
    nom = ""
    noms_a_crier = traitement_plusieurs_noms_cris(noms)
    noms_traites = traitement_plusieurs_noms(noms)
    if len(noms_a_crier) == 0:
        return hello_nom(noms_traites)
    elif len(noms_traites) == 0:
        return hello_cri(noms_a_crier)
    return hello_nom(noms_traites) + ". AND " + hello_cri(noms_a_crier)


def traitement_plusieurs_noms(noms):
    nom = ""
    noms_traites = ""
    j = 0
    for i in range(0, len(noms)):
        if noms[i] == ",":
            nom = noms[j:i]
            if nom != nom.upper():
                nom = nom[0].upper() + nom[1:]
                noms_traites += nom + ", "
            j = i + 1
    nom = noms[j:]
    if nom != nom.upper():
        nom = nom[0].upper() + nom[1:]
        noms_traites += nom
    if len(noms_traites) > 0 and noms_traites[-2] == ',':
        noms_traites = noms_traites[0:-2]
    return noms_traites

def traitement_plusieurs_noms_cris(noms):
    nom = ""
    noms_a_crier = ""
    j = 0
    for i in range(0, len(noms)):
        if noms[i] == ",":
            nom = noms[j:i]
            if nom.isupper():
                noms_a_crier += nom + ", "
            j = i + 1
    nom = noms[j:]
    if nom.isupper():
        noms_a_crier += nom
    if len(noms_a_crier) > 0 and noms_a_crier[-2] == ',':
        noms_a_crier = noms_a_crier[0:-2]
    return noms_a_crier