import message_de_bienvenue as b


def test_hello_nom():
    assert b.hello_nom("bob") == "Hello, Bob"
    assert b.hello_nom("Barbie") == "Hello, Barbie"
    assert b.hello_nom("")=="error"
    assert b.hello_nom(123)=="error"


def test_hello_cri():
    assert b.hello_cri("JERRY") == "HELLO, JERRY !"
    assert b.hello_cri("bobby") == "error"
    assert b.hello_cri("Johnny Hallyday") == "error"

    
def test_hello_blank():
    assert b.hello_blank("     ") == "Hello, my friend"
    assert b.hello_blank("") == "Hello, my friend"
    assert b.hello_blank("bob") == "error"


def test_is_blank():
    assert b.is_blank("") == True
    assert b.is_blank("      ") == True
    assert b.is_blank("       a") == False


def test_hello_deux_noms():
    assert b.hello_deux_noms("Amy,Bob")=="Hello, Amy, Bob"
    assert b.hello_deux_noms("Amy,bob") == "Hello, Amy, Bob"
    assert b.hello_deux_noms("amy,bob") == "Hello, Amy, Bob"


def test_hello_plusieurs_noms():
    assert b.hello_plusieurs_noms("Amy,Bob,Jerry") == "Hello, Amy, Bob, Jerry"
    assert b.hello_plusieurs_noms("mahdjou,aymeric,mike,damien,dang,matthieu") == "Hello, Mahdjou, Aymeric, Mike, Damien, Dang, Matthieu"


def test_hello_plusieurs_noms_cris():
    assert b.hello_plusieurs_noms_cris("Amy,BOB,Jerry") == "Hello Amy, Jerry. AND HELLO, BOB !"