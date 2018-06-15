celsius = float(input())
fahrenheit = float(input())

celsiusFahrenheit = (9 * celsius + 160) / 5
fahrenheitCelsius = (fahrenheit - 32) * 5/9

print('Temperatura %f C = '
      '%f F\n'
      'Temperatura %f F = '
      '%f C' % (celsius, celsiusFahrenheit, fahrenheit, fahrenheitCelsius))
