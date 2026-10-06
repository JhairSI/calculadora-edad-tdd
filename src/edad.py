def calcular_edad(nacimiento, hoy):
    edad = hoy.year - nacimiento.year
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1
    return edad