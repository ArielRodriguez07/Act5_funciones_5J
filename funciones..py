print("Ejemplo de funciones")
# declarar funciones
def hola():
    print("alguien uso la funcion hola")

def chat (mensa):
    print(f"chat{mensa}")

def ellacontesta (mensa):
    print(f"chat ella :{mensa}")

def escribenombre(ap,n):
    print(f"tu nomnbre completo es :{n} {ap}")
def suma(a,b):
    s=a+b
    return s
def resta(a,b):
    s=a-b
    return s
def multi(a,b):
    s=a*b
    return s
def div(a,b):
    s=a/b
    return s
# llamada a funciones
hola()
chat(" que bonita es")
ellacontesta("gracias")
escribenombre("Rodriguez","Ariel")
print ("operaciones suma ")
c1 = int(input("ingresa un numero"))
c2 = int(input("ingresa un numero"))
damesuma=suma(c1,c2)
print(f"la suma de {c1} + {c2} = {damesuma}")
c1 = int(input("ingresa un numero"))
c2 = int(input("ingresa un numero"))
damesuma=resta(c1,c2)
print(f"la resta de {c1} - {c2} = {damesuma}")
c1 = int(input("ingresa un numero"))
c2 = int(input("ingresa un numero"))
damesuma=multi(c1,c2)
print(f"la multiplicacion de {c1} * {c2} = {damesuma}")
c1 = int(input("ingresa un numero"))
c2 = int(input("ingresa un numero"))
damesuma=div(c1,c2)
print(f"la divicion de {c1} / {c2} = {damesuma}")