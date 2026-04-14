def add_two_numbers(a, b):
    return a + b

def test_small_numbers():
    assert add_two_numbers(1, 2) == 3, "Suma 1 + 2 powinna wynosić 3"

def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "Suma 100 + 300 powinna wynosić 400"