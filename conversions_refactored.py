class ConversionErrors (Exception): pass
class ConversionNotPossible(ConversionErrors): pass

def convert (fromUnit, toUnit, value):
    units = {'f': (((value * 9/5) + 32), ((value*9/5)-459.67)), 'c': (((value - 32)* 5/9), (value - 273.15)),
             'k':(value + 273.15 , (value + 459.67)* 5/9), 'mi' : ((value * 0.00062137), (value / 1760.00)),
             'm': (value / 0.00062137, value * 0.9144), 'yd': ((value * 1760.00), (value/0.9144))}
    temp = ['c', 'f', 'k']
    for key in units:
        if fromUnit == 'c' and toUnit == 'f':
            result = units['f'][0]
        if fromUnit == 'k' and toUnit == 'f':
            result = units['f'][1]
        if fromUnit == 'f' and toUnit == 'c':
            result = units['c'][0]
        if fromUnit == 'k' and toUnit == 'c':
            result = units['c'][1]
        if fromUnit == 'c' and toUnit == 'k':
            result = units['k'][0]
        if fromUnit == 'f' and toUnit == 'k':
            result = units['k'][1]
        if fromUnit == 'm' and toUnit == 'mi':
            result = units['mi'][0]
        if fromUnit == 'yd' and toUnit == 'mi':
            result = units['mi'][1]
        if fromUnit == 'mi' and toUnit == 'm':
            result = units['m'][0]
        if fromUnit == 'yd' and toUnit == 'm':
            result = round(units['m'][1], 2)
        if fromUnit == 'mi' and toUnit == 'yd':
            result = units['yd'][0]
        if fromUnit == 'm' and toUnit == 'yd':
            result = round(units['yd'][1],2)
        if fromUnit == toUnit:
            result = value
    for value in temp:
        if fromUnit not in temp and toUnit in temp:
            raise ConversionErrors("Conversion Not Possible")
        if fromUnit in temp and toUnit not in temp:
            raise ConversionErrors("Conversion Not Possible")
        
    return result



