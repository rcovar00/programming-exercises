def convert_to_dollars(pesos):
    dollar = 18.20
    return pesos // dollar


pesos = float(raw_input('How many pesos do you have? '))
print convert_to_dollars(pesos)
