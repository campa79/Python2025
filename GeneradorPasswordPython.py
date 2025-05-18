################################
### Generador de Contraseñas ###
### AC 17/5/25 v1.0 Beta     ###
################################
import random

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "1234567890"
simbolos = "_-!"

todos = f"{letras}{numeros}{simbolos}"
longitud = 10
extension = random.sample(todos, longitud)

password = "".join(extension)

print("La contraseña creada es: ",password)



