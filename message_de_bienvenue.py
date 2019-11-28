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