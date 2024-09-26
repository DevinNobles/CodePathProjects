#Write a function convertTemp() that takes in celsius as a parameter, which denotes the temperature in celsius. The variable is a non-negative floating point number rounded to two decimal places. In the function, convert celsius into Kelvin and Fahrenheit and return the list ans, in which ans = [kelvin, fahrenheit].


def convert(celsius):
    fahrenheit = round(((celsius * 1.8) + 32), 2)
    Kelvin = round((celsius + 273.15), 2)

    ans = [Kelvin, fahrenheit]
    print(ans)



convert(23.00)