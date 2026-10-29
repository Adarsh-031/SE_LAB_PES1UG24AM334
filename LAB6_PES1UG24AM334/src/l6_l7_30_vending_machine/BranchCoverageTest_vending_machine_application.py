
import pytest
from vending_machine import make_change, purchase, select_item


@pytest.mark.parametrize(
    "item, stock, credit, expected",
    [
        ("water", {}, 100, "invalid"),
        ("cola", {}, 150, "sold_out"),
        ("cola", {"cola": 0}, 150, "sold_out"),
        ("chips", {"chips": 1}, 99, "insufficient"),
        ("candy", {"candy": 1}, 75, "ok"),
    ],
)
def test_select_item_all_decisions(item, stock, credit, expected):
    assert select_item(item, stock, credit) == expected


def test_make_change_negative():
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-5)


@pytest.mark.parametrize(
    "amount, expected",
    [
        (0, []),
        (5, [5]),
        (185, [100, 50, 25, 10]),
        (255, [100, 100, 50, 5]),
        (1, None),
    ],
)
def test_make_change_all_branches(amount, expected):
    assert make_change(amount) == expected


@pytest.mark.parametrize(
    "item, stock, credit, expected",
    [
        ("water", {}, 100, "invalid"),
        ("cola", {"cola": 0}, 150, "sold_out"),
        ("chips", {"chips": 1}, 99, "insufficient"),
    ],
)
def test_purchase_rejected_without_stock_change(
    item, stock, credit, expected
):
    before = stock.copy()

    assert purchase(item, stock, credit) == (expected, [])
    assert stock == before


def test_purchase_no_exact_change():
    stock = {"chips": 2}

    assert purchase("chips", stock, 101) == (
        "no_exact_change", []
    )
    assert stock["chips"] == 2


def test_purchase_success_with_change():
    stock = {"candy": 2}

    assert purchase("candy", stock, 100) == (
        "dispensed", [25]
    )
    assert stock["candy"] == 1


def test_purchase_success_without_change():
    stock = {"candy": 1}

    assert purchase("candy", stock, 75) == (
        "dispensed", []
    )
    assert stock["candy"] == 0
