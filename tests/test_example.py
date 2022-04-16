from src.jtmds.example import add_one


def test_example_add():
    assert add_one(1) == 2
    assert add_one(4) == 5
