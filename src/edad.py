from datetime import date

def calcular_edad(nacimiento: date, hoy: date) -> int:
    if nacimiento > hoy:
        raise ValueError("La fecha de nacimiento no puede ser en el futuro")
        
    edad = hoy.year - nacimiento.year
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
        edad -= 1
    return edad