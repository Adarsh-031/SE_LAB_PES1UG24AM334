
def parse_coins(coins_csv):
    # Check if input is a string
    if not isinstance(coins_csv, str):
        raise TypeError("Coin input must be a string")

    # Check for empty input
    if not coins_csv.strip():
        raise ValueError("Coin input cannot be empty")

    coins = []

    # Split the input using commas
    for c in coins_csv.split(','):
        c = c.strip()

        # Check if the coin value is empty
        if not c:
            raise ValueError("Empty coin value found")

        # Convert coin value into integer
        value = int(c)

        if value <= 0:
            raise ValueError("Coin value must be positive")

        coins.append(value)

    return coins


def slot_position(code):
    # Check if input is a string
    if not isinstance(code, str):
        raise TypeError("Slot code must be a string")

    code = code.strip().upper()

    # Check if slot code is valid
    if len(code) < 2:
        raise ValueError("Invalid slot code")

    # First character should be an alphabet
    if not ('A' <= code[0] <= 'Z'):
        raise ValueError("Invalid row")

    # Remaining characters should be numbers
    if not code[1:].isdigit():
        raise ValueError("Invalid column")

    row = ord(code[0]) - ord('A')
    column = int(code[1:]) - 1

    if column < 0:
        raise ValueError("Column must be positive")

    return row, column


def change_due(payment):
    # Check if input is a string
    if not isinstance(payment, str):
        raise TypeError("Payment must be a string")

    # Split payment into paid amount and price
    parts = payment.split('/')

    if len(parts) != 2:
        raise ValueError("Payment must be in paid/price format")

    paid, price = parts

    paid = paid.strip()
    price = price.strip()

    if not paid or not price:
        raise ValueError("Paid amount and price cannot be empty")

    paid = int(paid)
    price = int(price)

    if paid < 0 or price < 0:
        raise ValueError("Amounts cannot be negative")

    if paid < price:
        raise ValueError("Insufficient payment")

    change = paid - price

    return str(change // 5) + ' five-coins'


def main():
    print("==== Running parse_coins ====")

    user_input = input("Enter coin values as CSV (e.g. 5,10,25): ")
    try:
        result = parse_coins(user_input)
        print("Coins:", result)
    except (ValueError, TypeError) as e:
        print("Error:", e)

    print("\n==== Running slot_position ====")

    user_input = input("Enter a slot code (e.g. B7): ")
    try:
        result = slot_position(user_input)
        print("Row and Column:", result)
    except (ValueError, TypeError) as e:
        print("Error:", e)

    print("\n==== Running change_due ====")

    user_input = input("Enter paid/price (e.g. 200/150): ")
    try:
        result = change_due(user_input)
        print("Change Due:", result)
    except (ValueError, TypeError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
