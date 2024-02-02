class CurrencyConverter:
    def __init__(self, exchange_rates):
        self.exchange_rates = exchange_rates

    def convert(self, amount, from_currency, to_currency):
        exchange_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        converted_amount = amount * exchange_rate
        return converted_amount

    def is_valid_currency(self, currency):
        return currency in self.exchange_rates and not currency.isdigit()

def main():
    exchange_rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.78,
        'INR': 82.84,
        'PHP': 55.92,
    }

    converter = CurrencyConverter(exchange_rates)

    print("Welcome to the Currency Converter!")

    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            print("\nCurrency Code:"
                  "\n[ USD , EUR , GBP , INR , PHP ]")

            # Loop until valid 'from currency' is entered
            while True:
                from_currency = input("\nType the currency code to convert from (e.g., USD): ").upper()
                if converter.is_valid_currency(from_currency):
                    break
                print("\nInvalid Currency Code. Please Enter a Valid 3-Letter Currency Code.")

            # Loop until valid 'to currency' is entered
            while True:
                to_currency = input("Type the currency code to convert to (e.g., EUR): ").upper()
                if converter.is_valid_currency(to_currency):
                    break
                print("Invalid Currency Code. Please Enter a Valid 3-Letter Currency Code.")

            if from_currency == to_currency:
                print("Invalid Currency Code. Please  Enter Two Different Currency Code")
                continue

            try:
                amount = float(input("Enter the amount to convert: "))
            except ValueError:
                print("Please Enter a Valid Amount.")
                continue

            converted_amount = converter.convert(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

        elif choice == '2':
            print("Exiting the Currency Converter. Goodbye! Have a great day ahead!")
            break
        else:
            print("Invalid choice. Please Enter a Valid Option (1-2).")

if __name__ == "__main__":
    main()
