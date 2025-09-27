
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


try:
    temperature_to_convert = float(input("Enter the temperature to convert: "))
    temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    if temperature_type == "c":
        result = convert_to_fahrenheit(temperature_to_convert)
        print(f"{temperature_to_convert}°C is {result}°F")

    elif temperature_type == "f":
        result = convert_to_celsius(temperature_to_convert)
        print(f"{temperature_to_convert}°F is {result}°C")

    else:
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

except ValueError as e:
    print(f"Invalid temperature. Please enter a numeric value. ({e})")
