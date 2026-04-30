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