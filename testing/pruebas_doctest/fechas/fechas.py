def fecha(num):
    stored_values_thousandths = {
    1: 0, # lugar de las unidades
    2: 0, # lugar de las decenas
    3: 0, # lugar de las centenas
    4: 0 # lugar de las unidades de millar
    }
    for enum, value in enumerate(str(num)[::-1], 1):
        stored_values_thousandths[enum] = int(value)
        print(stored_values_thousandths)