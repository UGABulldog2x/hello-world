from hello import greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_custom_name():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"
