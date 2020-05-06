meter = int(input('Input value in meter '))
long_values = {1: 'mm', 2: 'cm', 3: 'km'}
var = str(input(f"Input value {long_values[1]} or {long_values[2]} or {long_values[3]} "))


if long_values[1] == var:
    print(meter * 1000)
elif long_values[2] == var:
    print(meter*100)
else:
    print(meter/1000)
