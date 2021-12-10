import os

import hvac
import json

client = hvac.Client()
client = hvac.Client(
 #url=os.environ['VAULT_URL'],
 #token=os.environ['VAULT_TOKEN']
 url='http://172.19.0.1:8200',
 token="s.y2RgdhKWi544KO92X8hilbW9"
)

print()
print()
print("Bienvenido a la demostración de la herramienta de secretos dinámicos, Vault")
print("Antes de nada, al tratarse de una herramienta de información delicada, necesito que me hagas un favor...")
print("Acceda desde su navegador la url localhost:8200")
print("A continuación, introduzca las 3 claves guardadas anteriormente, deben tener un formato con el siguiente:")
print()
print()
print("N09JMtWnNOlszve8RWBbC4Rf4xopr2ug4HyjiQWa3LZQ")
print("gwajYB/JY2j5sA54hatnwYDitTLqLR7LXRyKAMym0CVd")
print("QUkZSu7OwZfenjF6D3+Y2Pz37SeW/3pEbNriH7E0YF5a")
print()
print()
print("Cuando acabes, pulse ENTER")
input()
print("¡¡Genial!!")
print()
print()
print("¿Qué secreto deseas guardar?")
secreto = input()

client.write('kv/cliente', Tu_secreto=secreto)

json_formatted_str = json.dumps(client.read('kv/cliente'), indent=2)

print(json_formatted_str)

print("Tu secreto ha sido guardado")
print()
print("Además, he creado un archvo txt llamado topSecret.txt en la carpeta permanentes (../permanentes/topSecret.txt) ")
print("con su información.")
f=open("../permanentes/topSecret.txt","w")
f.write(secreto)
f.close()

