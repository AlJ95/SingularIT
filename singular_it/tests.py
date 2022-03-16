from singular_it.main import solve


def test_1():
    assert solve(["WESTEN", "OSTEN", "NORDEN", "NORDEN", "SÜDEN"]) == ["NORDEN"], "Test 1 nicht bestanden."


def test_2():
    directions = ["NORDEN", "NORDEN", "OSTEN", "OSTEN", "WESTEN", "WESTEN", "SÜDEN", "WESTEN"]
    assert solve(directions=directions) == ["NORDEN", "WESTEN"], "Test 2 nicht bestanden."


def test_3():
    assert solve(["NORDEN"]) == ["NORDEN"], "Test 3 nicht bestanden."


def test_4():
    assert solve(["NORDEN", "SÜDEN"]) == [], "Test 4 nicht bestanden."
