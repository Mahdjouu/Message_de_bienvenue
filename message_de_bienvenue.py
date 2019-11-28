def hello_nom(nom):
    if isinstance(nom, str):
        if len(nom)>0:
            nom = nom[0].upper() + nom[1:]
            hello = "Hello, " + nom
            return hello
        else:
            return "error"

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


