import random
import string

# 1 elaborar un programa que recorra una lista con los nombres de 10 futuros usuarios
futuros_usuarios = {"nombres": ["Juan", "Marta", "Luis", "Ana", "Diego", "Carla", "Pablo", "Lucía", "Fernando", "Valentina"]}
print(futuros_usuarios["nombres"])

# 2 mediante una función, a todos los usuarios se les creará una cuenta automaticamente

usuarios_creados = []

# 3 asignar una contraseña por cada cuenta. la contraseña debe ser creada por random y debe cumplir los sgtes criterios: mayusculas, minusculas y numeros

def generar_contraseña():
    longitud = 8
    caracteres = string.ascii_letters + string.digits
    while True:
        contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
        if any(char.isupper() for char in contraseña) and any(char.islower() for char in contraseña) and any(char.isdigit() for char in contraseña):
            return contraseña
        
# 4 cada cuenta debe guardarse en una nueva variable con su respectiva contraseña
# 5 por cada cuenta debe pedir un telefono (lo debe pedir por los 10 usuarios)
# 6 el telefono debe tener 8 numeros de lo contrario no se acepta
# 7 el numero de telefono se debe guardar como  un string


for nombre in futuros_usuarios["nombres"]:
    contraseña = generar_contraseña()
    while True:
        telefono = input(f"Ingrese el número de teléfono para {nombre}: ")
        if len(telefono) == 8:
            break
        else:
            print("El número de teléfono debe tener exactamente 8 dígitos. Intente nuevamente.")
    usuario = {"nombre": nombre, "contraseña": contraseña, "telefono": str(telefono)}
    usuarios_creados.append(usuario)

    

print(usuarios_creados)

