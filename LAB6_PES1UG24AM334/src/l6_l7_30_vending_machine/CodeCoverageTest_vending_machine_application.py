
from vending_machine import make_change, purchase, select_item


def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"


def test_sold_out():
    assert select_item("cola", {"cola": 0}, 150) == "sold_out"


def test_insufficient_credit():
    assert select_item("chips", {"chips": 1}, 99) == "insufficient"


def test_zero_change():
    assert make_change(0) == []


def test_multiple_coins():
    assert make_change(185) == [100, 50, 25, 10]


def test_no_exact_change():
    assert make_change(3) is None


def test_purchase_invalid_item():
    assert purchase("water", {}, 100) == ("invalid", [])


def test_purchase_success_updates_stock():
    stock = {"candy": 2}
    assert purchase("candy", stock, 100) == ("dispensed", [25])
    assert stock["candy"] == 1
