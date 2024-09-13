def convert_price(input):
    import re

    # The string containing the currency value
    currency_string = input

    # Regular expression to find the numeric value
    pattern = r"\d+\.\d+"

    # Search for the pattern in the string
    match = re.search(pattern, currency_string)

    if match:
        # Extract the matched value
        value = match.group()
        return  value
    else:
        0
