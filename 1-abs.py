# -------=---------=|^|---------=------------

distancia = 40

if distancia < 0:
    print(f"Te faltan {abs(distancia)} kilometros para llegar")
elif distancia == 0:
    print("Has llegado")
else:
    print(f"Te has pasado por {abs(distancia)} metros")
