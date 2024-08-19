import conversion
import unittest
import conversions_refactored as cr


class TempConversionValues(unittest.TestCase):

    test_values_c_to_k = [(100, 373.15),
                          (500, 773.15),
                          (115.75, 388.9),
                          (321.5, 594.65),
                          (0.05, 273.2)]

    test_values_c_to_f = [(100, 212),
                          (500, 932),
                          (115.75, 240.35),
                          (321.5, 610.7),
                          (0.05, 32.09)]

    test_values_f_to_c = [(100, 37.7778),
                          (500, 260),
                          (115.75, 46.5278),
                          (321.5, 160.8333),
                          (0.05, -17.75)]

    test_values_f_to_k = [(100, 310.9278),
                          (500, 533.15),
                          (115.75, 319.6778),
                          (321.5, 433.9833),
                          (0.05, 255.4)]

    test_values_k_to_c = [(100, -173.15),
                          (500, 226.85),
                          (115.75, -157.4),
                          (321.5, 48.35),
                          (0.05, -273.1)]

    test_values_k_to_f = [(100, -279.67),
                          (500, 440.33),
                          (115.75, -251.32),
                          (321.5, 119.03),
                          (0.05, -459.58)]

    refactored_units = ['kelvin', 'celsius', 'fahrenheit', 'miles', 'yards', 'meters']
    test_values_dict = {'celsius': {'kelvin': test_values_c_to_k,
                                    'fahrenheit': test_values_c_to_f,
                                    'celsius': [(1, 1)],
                                    'miles': [(1, None)],
                                    'yards': [(1, None)],
                                    'meters': [(1, None)]
                                    },
                        'kelvin': {'fahrenheit': test_values_k_to_f,
                                   'celsius': test_values_k_to_c,
                                   'kelvin': [(1, 1)],
                                   'miles': [(1, None)],
                                   'yards': [(1, None)],
                                   'meters': [(1, None)]
                                   },
                        'fahrenheit': {'kelvin': test_values_f_to_k,
                                       'celsius': test_values_f_to_c,
                                       'fahrenheit': [(1, 1)],
                                       'miles': [(1, None)],
                                       'yards': [(1, None)],
                                       'meters': [(1, None)]
                                       },
                        'miles': {'yards': [(1, 1760)],
                                  'meters': [(1, 1609.344)],
                                  'miles': [(1, 1)],
                                  'kelvin': [(1, None)],
                                  'celsius': [(1, None)],
                                  'fahrenheit': [(1, None)]
                                  },
                        'yards': {'meters': [(1, 0.9144)],
                                  'miles': [(1760, 1)],
                                  'yards': [(1, 1)],
                                  'kelvin': [(1, None)],
                                  'celsius': [(1, None)],
                                  'fahrenheit': [(1, None)]
                                  },
                        'meters': {'yards': [(1, 1.0936)],
                                   'miles': [(1609.344, 1)],
                                   'meters': [(1, 1)],
                                   'kelvin': [(1, None)],
                                   'celsius': [(1, None)],
                                   'fahrenheit': [(1, None)]
                                   }
                        }

    def test_celsius_to_kelvin_conversion(self):
        for val, res in self.test_values_c_to_k:
            conv_c_to_k_res = conversion.convert_celsius_to_kelvin(val)
            self.assertEqual(res, conv_c_to_k_res)
            print(f"Test for converting {val} celsius to {res:.2f} kelvin passed")

    def test_celsius_to_fahrenheit_conversion(self):
        for val, res, in self.test_values_c_to_f:
            conv_c_to_f_res = conversion.convert_celsius_to_fahrenheit(val)
            self.assertEqual(res, conv_c_to_f_res)
            print(f"Test for converting {val} celsius to {res:.2f} fahrenheit passed")

    def test_fahrenheit_to_celsius_conversion(self):
        for val, res, in self.test_values_f_to_c:
            conv_f_to_c_res = conversion.convert_fahrenheit_to_celsius(val)
            self.assertEqual(res, conv_f_to_c_res)
            print(f"Test for converting {val} fahrenheit to {res:.2f} celsius passed")

    def test_fahrenheit_to_kelvin_conversion(self):
        for val, res, in self.test_values_f_to_k:
            conv_f_to_k_res = conversion.convert_fahrenheit_to_kelvin(val)
            self.assertEqual(res, conv_f_to_k_res)
            print(f"Test for converting {val} fahrenheit to {res:.2f} kelvin passed")

    def test_kelvin_to_celsius_conversion(self):
        for val, res, in self.test_values_k_to_c:
            conv_k_to_c_res = conversion.convert_kelvin_to_celsius(val)
            self.assertEqual(res, conv_k_to_c_res)
            print(f"Test for converting {val} kelvin to {res:.2f} celsius passed")

    def test_kelvin_to_fahrenheit_conversion(self):
        for val, res, in self.test_values_k_to_f:
            conv_k_to_f_res = conversion.convert_kelvin_to_fahrenheit(val)
            self.assertEqual(res, conv_k_to_f_res)
            print(f"Test for converting {val} kelvin to {res:.2f} fahrenheit passed")

    def test_conversions_refactored(self):
        for from_unit in self.refactored_units:
            to_unit_dict = self.test_values_dict[from_unit]
            for to_unit in to_unit_dict:
                val_res_list = to_unit_dict[to_unit]
                for val, res in val_res_list:
                    try:
                        conv = cr.ConvRef().convert(from_unit, to_unit, val)
                        self.assertEqual(res, round(conv, 4))
                        print(f"conversions_refactored.py test for converting {val} "
                              f"{from_unit} to {res:.2f} {to_unit} passed")
                    except cr.ConversionNotPossible:
                        print(f"exception test between {from_unit} and {to_unit} passed")


if __name__ == '__main__':
    unittest.main()
