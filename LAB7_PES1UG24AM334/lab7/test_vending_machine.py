
from hypothesis import given, strategies as st
from vending_machine import parse_coins, slot_position, change_due


# Test parse_coins with random strings and None
@given(st.one_of(st.text(), st.none()))
def test_parse_coins_no_crash(s):
    try:
        parse_coins(s)
    except (ValueError, TypeError):
        pass


# Test slot_position with random strings and None
@given(st.one_of(st.text(), st.none()))
def test_slot_position_no_crash(s):
    try:
        slot_position(s)
    except (ValueError, TypeError, IndexError):
        pass


# Test change_due with random strings and None
@given(st.one_of(st.text(), st.none()))
def test_change_due_no_crash(s):
    try:
        change_due(s)
    except (ValueError, TypeError, ZeroDivisionError):
        pass


# Test valid coin inputs
@given(st.lists(st.integers(min_value=1, max_value=1000), min_size=1))
def test_parse_coins_valid(coins):
    csv = ",".join(map(str, coins))
    assert parse_coins(csv) == coins


# Test valid slot positions
@given(
    st.sampled_from("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
    st.integers(min_value=1, max_value=99)
)
def test_slot_position_valid(row, column):
    code = row + str(column)
    assert slot_position(code) == (ord(row) - ord('A'), column - 1)


# Test valid payment and price
@given(
    st.integers(min_value=0, max_value=100000),
    st.integers(min_value=0, max_value=100000)
)
def test_change_due_valid(paid, price):
    if paid >= price:
        result = change_due(f"{paid}/{price}")
        expected = str((paid - price) // 5) + ' five-coins'
        assert result == expected
