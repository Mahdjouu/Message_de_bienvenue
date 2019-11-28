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
