import requests

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=cff0b34d0f7f6319ca3a15cb20450ea7'
response = requests.get(url)
currency_data = response.json()

print(currency_data['rates'])

def currencyConverter(from_currency, to_currency, amount):
    if from_currency != 'EUR':
        amount = amount / currency_data['rates'][from_currency]
    amount = round(amount * currency_data['rates'][to_currency], 2)
    return amount

from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()
amount = float(input("Amount: "))
converted_amount = currencyConverter(from_currency, to_currency, amount)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")