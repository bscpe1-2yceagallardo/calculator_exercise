import datetime

class CalculatorOperation:

    def addition(self, first_number, second_number):
        return first_number + second_number

    def subtraction(self, first_number, second_number):
        return first_number - second_number

    def multiplication(self, first_number, second_number):
        return first_number * second_number

    def division(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError ("Cannot divide by zero!!!")
        return first_number / second_number

    def modulus(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero!!!")
        return first_number % second_number

    def floor_division(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero!!!")
        return first_number // second_number

    def power(self, first_number, second_number):
        return first_number ** second_number

class CalculatorRuntime:

    def __init__(self):
        self.history_file = "calculator_history.txt"
        self.currency_rates = {
            "United States Dollar": 1.0,
            "Euro": 0.92,
            "British Pound Sterling": 0.79,
            "Japanese Yen": 150.25,
            "Australian Dollar": 1.52
        }

    def convert_currency(self, amount):
        print("\n--- Convert Your Answer Into Currency ---")
        print("\nAvailable Currencies:")

        for name in self.currency_rates.keys():
            print(f" - {name}")

        target = input("\nEnter the full name of the currency (or press Enter to skip: ").strip()

        target_formatted = target.title() if target else ""

        if target_formatted in self.currency_rates:
            converted = amount * self.currency_rates[target_formatted]
            print(f"\n Converted Value: {converted:,.2f} {target_formatted}")
            return target_formatted, converted

        if target:
            print("\n Currency not recognized. Skipping conversion")
        return None, None

    def history_log(self, operation, first_number, second_number, result, conversion_info=None):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {operation}: {first_number} and {second_number} = {result}\n"

        if conversion_info and conversion_info[0] is not None:
            name, conversion_value = conversion_info
            log_entry += f" | Converted to {name}: {conversion_value:,.2f}"

        with open(self.history_file, "a") as history_file:
            history_file.write(log_entry + "\n")