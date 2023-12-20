from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

def is_valid_currency(currency_code):
    """ Check if the provided currency code is valid. """
    currency_codes = CurrencyCodes()
    try:
        # Try getting the symbol for the currency code
        symbol = currency_codes.get_symbol(currency_code)
        return symbol is not None
    except RatesNotAvailableError:
        return False

def convert_currency(from_currency, to_currency, amount):
    """ Convert amount from one currency to another. """
    currency_rates = CurrencyRates()
    try:
        converted_amount = currency_rates.convert(from_currency, to_currency, amount)
        return converted_amount
    except RatesNotAvailableError:
        raise ValueError("Invalid currency code.")

def format_currency(amount, currency_code):
    """ Format the amount with the currency symbol. """
    currency_codes = CurrencyCodes()
    symbol = currency_codes.get_symbol(currency_code)
    return f"{symbol} {amount:.2f}"
