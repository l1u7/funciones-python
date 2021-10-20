

var1 = bytes("Hola, ¿Comó estás?", encoding="utf8") 

basico = bytearray(b"saludos")

basico[0] = 82

basico = basico.decode()

print(basico)




print(var1.decode())