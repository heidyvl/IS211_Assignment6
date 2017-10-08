import conversions_refactored
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
    knownConversionsMtoMi = ((1, 0.00062137),
                             (10, 0.0062137),
                             (20, 0.0124274),
                             (30, 0.0186411),
                             (40, 0.0248548))
    knownConversionsMtoYd = ((1, 1.09),
                             (10, 10.94),
                             (20, 21.87),
                             (30, 32.81),
                             (40, 43.74))
    knownConversionsMitoYd = ((1, 1760),
                             (10, 17600),
                             (20, 35200),
                             (30, 52800),
                             (40, 70400))
    sameValues = (('c', 'c', 5), ('f', 'f', 5), ('k', 'k', 5), ('m', 'm', 10), ('mi', 'mi', 10))
 
    
    def testCtoFValues(self):
        """Tests if Celsius to Fahrenheit conversion returns the correct value"""
        for c,f in self.knownConversionsCtoF:
            result = conversions_refactored.convert('c','f',c)
            self.assertEqual(f,result)
            
    def testCtoKValues(self):
        """Tests if Celsius to Kelvin conversion returns the correct value"""
        for c,k in self.knownConversionsCtoK:
            result = conversions_refactored.convert('c','k',c)
            self.assertEqual(k,result)

    def testFtoCValues(self):
        """Tests if Fahrenheit to Celsius conversion returns the correct value"""
        for c,f in self.knownConversionsCtoF:
            result = conversions_refactored.convert('f','c',f)
            self.assertEqual(c,result)
            
    def testKtoCValues(self):
        """Tests if Kelvin to Celsius returns the correct value"""
        for c,k in self.knownConversionsCtoK:
            result = conversions_refactored.convert('k','c',k)
            self.assertEqual(c,result)

    def testFtoKValues(self):
        """Tests if Fahrenheit to Kelvin conversion returns the correct value"""
        for f,k in self.knownConversionsFtoK:
            result = conversions_refactored.convert('f','k',f)
            self.assertEqual(k,round((result),2))
            
    def testKtoFValues(self):
        """Tests if Kelvin to Fahrenheit conversion returns the correct value"""
        for f,k in self.knownConversionsFtoK:
            result = conversions_refactored.convert('k','f',k)
            self.assertEqual(f,round((result), 2))

    def testMtoMiValues(self):
        """Tests if Meter to Mile conversion returns the correct value"""
        for m,mi in self.knownConversionsMtoMi:
            result = conversions_refactored.convert('m','mi',m)
            self.assertEqual(mi,result)
            
    def testMitoMValues(self):
        """Tests if Mile to Meter conversion returns the correct value"""
        for m,mi in self.knownConversionsMtoMi:
            result = conversions_refactored.convert('mi','m',mi)
            self.assertEqual(m,result)

    def testMtoYdValues(self):
        """Tests if Meter to Yard conversion returns the correct value"""
        for m,yd in self.knownConversionsMtoYd:
            result = conversions_refactored.convert('m','yd',m)
            self.assertEqual(yd,result)

    def testYdtoMValues(self):
        """Tests if Yard to Meter conversion returns the correct value"""
        for m,yd in self.knownConversionsMtoYd:
            result = conversions_refactored.convert('yd','m',yd)
            self.assertEqual(m,result)

    def testMitoYdValues(self):
        """Tests if Mile to Yard conversion returns the correct value"""
        for mi,yd in self.knownConversionsMitoYd:
            result = conversions_refactored.convert('mi','yd',mi)
            self.assertEqual(yd,result)

    def testYdtoMiValues(self):
        """Tests if Mile to Yard conversion returns the correct value"""
        for mi,yd in self.knownConversionsMitoYd:
            result = conversions_refactored.convert('yd','mi',yd)
            self.assertEqual(mi,result)

    def testSameUnitValue(self):
        """Tests that converting from one unit to itself returns the same value for all units"""
        for value in self.sameValues:
            result = conversions_refactored.convert(value[0], value[1], value[2])
            self.assertEqual(value[2], result)
            
    def testConversionNotPossible(self):
        """Tests that converting from incompatible units will raise a ConversionNotPossible exception"""
        self.assertRaises(conversions_refactored.ConversionErrors)
            

if __name__ == "__main__":
    unittest.main(verbosity=2)
