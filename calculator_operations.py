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

    def history_log(self, operation, first_number, second_number, result):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.history_file, "a") as history_file:
            history_file.write(f"[{timestamp}] {operation}: {first_number} and {second_number} = {result}\n")