import requests

# Function to convert currency using ExchangeRate-API
def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()

        # Get the conversion rate
        conversion_rate = data['rates'][to_currency]

        # Calculate the converted amount
        converted_amount = amount * conversion_rate

        return converted_amount
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the API: {e}")
        return None

# User input for amount and currency codes
amount = float(input("Please enter the amount you want to convert: "))
from_currency = input("Please enter the currency code to convert from (e.g., USD): ").upper()
to_currency = input("Please enter the currency code to convert to (e.g., EUR): ").upper()

# Perform the currency conversion
converted_amount = convert_currency(amount, from_currency, to_currency)

# Display the result
if converted_amount is not None:
    print(f"The converted amount is: {converted_amount} {to_currency}")
else:
    print("Conversion failed. Please try again later.")
100