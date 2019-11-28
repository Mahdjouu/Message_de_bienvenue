import message_de_bienvenue as b


def test_hello_nom():
    assert b.hello_nom("bob") == "Hello, Bob"
    assert b.hello_nom("Barbie") == "Hello, Barbie"
    assert b.hello_nom("")=="error"
    assert b.hello_nom(123)=="error"


