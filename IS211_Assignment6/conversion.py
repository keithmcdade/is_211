def convert_celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    kelvin = format(kelvin, '.4f')
    return float(kelvin)


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    fahrenheit = format(fahrenheit, '.4f')
    return float(fahrenheit)


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    celsius = format(celsius, '.4f')
    return float(celsius)


def convert_fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * (5/9) + 273.15
    kelvin = format(kelvin, '.4f')
    return float(kelvin)


def convert_kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    celsius = format(celsius, '.4f')
    return float(celsius)


def convert_kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * (9/5) + 32
    fahrenheit = format(fahrenheit, '.4f')
    return float(fahrenheit)


def main():
    pass


if __name__ == '__main__':
    main()

