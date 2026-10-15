print("Hello, World!")
>>> print("Això és una \"polzada\" dins d'una cadena amb cometes dobles")
Això és una "polzada" dins d'una cadena amb cometes dobles
>>> print("Roger", "Faro")
Roger Faro
>>> print("Python", "és", "divertit", sep '-')
  File "<python-input-2>", line 1
    print("Python", "és", "divertit", sep '-')
                                          ^^^
SyntaxError: invalid syntax
>>> print("Python", "és", "divertit", sep -)
  File "<python-input-3>", line 1
    print("Python", "és", "divertit", sep -)
                                           ^
SyntaxError: invalid syntax
>>> print("Python", "és", "divertit", sep = "-")
Python-és-divertit
>>> print("15+17")
15+17
>>> print(15+17)
32
>>> print("float:")
float:
>>> print(type(3.14))
<class 'float'>
>>> print(float(3.14))
3.14
>>> print(int(3.14))
3
>>> print(str("Hola"))
Hola
>>> print(str("""
...   Multilínia
... """))

  Multilínia

>>> print(bool(True))
True
>>> print(bool(5 > 3))
True
>>> print(5<3)
False
>>> miisatge=hola
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    miisatge=hola
             ^^^^
NameError: name 'hola' is not defined
>>> missatge = "Hola"
>>> print(missatge)
Hola
>>> print(str(missatge))
Hola
>>> print(type(10))
<class 'int'>
>>> print(type(25))
<class 'int'>
>>> print(type("hola món"))
<class 'str'>
>>> print(type(10>5))
<class 'bool'>
>>> nom_encaminador = aula
Traceback (most recent call last):
  File "<python-input-24>", line 1, in <module>
    nom_encaminador = aula
                      ^^^^
NameError: name 'aula' is not defined
>>> nom_encaminador = "aula"
>>> nombre_ports = "8"
>>> estat 0 "ences"
  File "<python-input-27>", line 1
    estat 0 "ences"
          ^
SyntaxError: invalid syntax
>>> estat = "ences"
>>> print(f"A l'{nom_encaminador} hi ha {nombre_ports} ports i està {estat}")
A l'aula hi ha 8 ports i està ences
longitud_km = float(input("Introdueix la longitud de l'enllaç de fibra (km): "))
velocitat_gbps = float(input("Introdueix la velocitat de transmissió (Gbps): "))
mida_dades_gb = 8.0
temps_transmissio_s = mida_dades_gb / velocitat_gbps
print(f"Per transmetre 1 GB de dades a través de l'enllaç caldran {temps_transmissio_s:.4f} segons.")
#Exercicis bàsics tema 1
print("""
Roger Faro
Terrassa
""")
>>> print(type(15))
<class 'int'>
>>> print(type("Hola mon"))
<class 'str'>
>>> print(type(None))
<class 'NoneType'>
>>> print(type(True))
<class 'bool'>
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

nom = "Marc"
edat = 40
alcada = 1.75
print(f"Hola! Em dic {nom}, tinc {edat} anys i faig {alcada} metres")

print("--------------")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

pi = 3.141592653589793
pi_arrodonit = round(pi)
resultat = pi_arrodonit // 2
print(resultat)

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

celsius = float(input("Introdueix la temperatura en graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} °C equivalen a {fahrenheit:.2f} °F.")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

total_compte = float(input("Introdueix el total del compte (€): "))
percentatge_propina = float(input("Introdueix el percentatge de propina (%): "))

propina = total_compte * (percentatge_propina / 100)
total_final = total_compte + propina

print(f"Propina: {propina:.2f} €")
print(f"Total a pagar: {total_final:.2f} €")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

contrasenya = input("Introdueix la teva contrasenya: ")

if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")