class ConvRef:

    # initialize object
    def __init__(self):
        pass

    # method for converting units; checks unit value, to convert from and to and returns solution
    @classmethod
    def convert(cls, from_unit, to_unit, value):
        # convert from kelvin
        if from_unit == 'kelvin':
            if to_unit == 'celsius':
                return value - 273.15
            if to_unit == 'fahrenheit':
                return (value - 273.15) * (9/5) + 32
            if to_unit == 'kelvin':
                return value
        # convert from celsius
        if from_unit == 'celsius':
            if to_unit == 'kelvin':
                return value + 273.15
            if to_unit == 'fahrenheit':
                return value * (9/5) + 32
            if to_unit == 'celsius':
                return value
        # convert from fahrenheit
        if from_unit == 'fahrenheit':
            if to_unit == 'celsius':
                return (value - 32) * (5/9)
            if to_unit == 'kelvin':
                return (value - 32) * (5/9) + 273.15
            if to_unit == 'fahrenheit':
                return value
        # convert from miles
        if from_unit == 'miles':
            if to_unit == 'yards':
                return value * 1760
            if to_unit == 'meters':
                return value * 1609.344
            if to_unit == 'miles':
                return value
        # convert from yards
        if from_unit == 'yards':
            if to_unit == 'miles':
                return value / 1760
            if to_unit == 'meters':
                return value * 0.9144
            if to_unit == 'yards':
                return value
        # convert from meters
        if from_unit == 'meters':
            if to_unit == 'yards':
                return value * 1.0936132983
            if to_unit == 'miles':
                return (value * 1.0936132983) / 1760
            if to_unit == 'meters':
                return value
        # raise exceptions for improper unit conversions
        if from_unit == 'kelvin' or 'celsius' or 'fahrenheit' and to_unit == 'miles' or 'yards' or 'meters':
            raise ConversionNotPossible(from_unit, to_unit)
        if from_unit == 'miles' or 'yards' or 'meters' and to_unit == 'kelvin' or 'celsius' or 'fahrenheit':
            raise ConversionNotPossible(from_unit, to_unit)


class ConversionNotPossible(Exception):
    # Raised when a conversion is not possible between two units
    def __init__(self, from_unit, to_unit):
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.message = f"Conversion from {from_unit} to {to_unit} is not possible."
        super().__init__(self.message)

#
# a = ConvRef()
# b = a.convert('fahrenheit', 'miles', 100)
# print(b)
