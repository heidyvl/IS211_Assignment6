def convertCelsiusToFahrenheit(celsius):
    farenheit = (celsius * 9/5) + 32
    return farenheit

def convertCelsiusToKelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def convertFahrenheittoCelsius(farenheit):
    celsius = (farenheit - 32)* 5/9
    return celsius

def convertKelvintoCelsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def convertFahrenheittoKelvin(farenheit):
    kelvin = (farenheit + 459.67)* 5/9
    return round(kelvin,2)

def convertKelvintoFahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return round(fahrenheit, 2)
