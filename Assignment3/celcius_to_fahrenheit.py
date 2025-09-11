"""Convert Celsius ↔ Fahrenheit temperature."""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


temp_c = float(input("Enter tempeature in celsius ="))
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.2f}°F")

temp_f = float(input("Enter temperature in fahrenheit ="))
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.2f}°C")
