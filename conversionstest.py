import conversions
import unittest

class KnownConversions(unittest.TestCase):
    """Gives known conversions for testing"""
    knownConversionsCtoF = ( (0.00, 32.00),
                             (10.00, 50.00),
                             (20.00, 68.00),
                             (30.00, 86.00),
                             (40.00, 104.00))
    knownConversionsCtoK = ( (0.00, 273.15),
                             (10.00, 283.15),
                             (20.00, 293.15),
                             (30.00, 303.15),
                             (40.00, 313.15))
    knownConversionsFtoK = ( (32.00, 273.15),
                             (50.00, 283.15),
                             (68.00, 293.15),
                             (86.00, 303.15),
                             (104.00, 313.15))
    def testCtoFValues(self):
        """Tests if convertCelsiusToFahrenheit returns the correct value"""
        for c,f in self.knownConversionsCtoF:
            result = conversions.convertCelsiusToFahrenheit(c)
            self.assertEqual(f,result)
            
    def testCtoKValues(self):
        """Tests if convertCelsiusToKelvin returns the correct value"""
        for c,k in self.knownConversionsCtoK:
            result = conversions.convertCelsiusToKelvin(c)
            self.assertEqual(k,result)
            
    def testFtoCValues(self):
        """Tests if convertFahrenheittoCelsius returns the correct value"""
        for c,f in self.knownConversionsCtoF:
            result = conversions.convertFahrenheittoCelsius(f)
            self.assertEqual(c,result)
            
    def testKtoCValues(self):
        """Tests if convertKelvintoCelsius returns the correct value"""
        for c,k in self.knownConversionsCtoK:
            result = conversions.convertKelvintoCelsius(k)
            self.assertEqual(c,result)

    def testFtoKValues(self):
        """Tests if convertFahrenheittoKelvin returns the correct value"""
        for f,k in self.knownConversionsFtoK:
            result = conversions.convertFahrenheittoKelvin(f)
            self.assertEqual(k,result)

    def testKtoFValues(self):
        """Tests if convertKelvintoFahrenheit returns the correct value"""
        for f,k in self.knownConversionsFtoK:
            result = conversions.convertKelvintoFahrenheit(k)
            self.assertEqual(f,result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
