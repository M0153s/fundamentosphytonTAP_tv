#esto es un comentario.

def nuevoTema(tema):
    print ("\n=======",tema,"=======\n")


if __name__ == "__main__":
    nuevoTema("Operadores aritmeticos")
    print("Operador de division entera (10//3):",10//3)
    print("Operador de potencias (5**5):",5**5)
    print("Operador de cambio de signo (-5):",-5)

    nuevoTema("Operadores logicos")
    print("Operador and (True and False):",True and False)
    print("Operador and (False and True):",False and True)
    print("Operador and (False and False):",False and False)
    print("Operador and (True and True):",True and True)

    print("Operador or (False or True):",False or True)
    print("Operador or  (True or False):",True or False)
    print("Operador or (False or False):",False or False)
    print("Operador or (True or True):",True or True)

    print("Operador not ( not True):", not True)
    print("Operador not ( not False):", not False)


    nuevoTema("Operadores de comparacion")

    print("2==3",2==3)
    print("2!=3",2!=3)
    print("2<3",2<3)
    print("2<=3",2<=3)
    print("2>3",2>3)
    print("2>=3",2>=3)

    nuevoTema("Variables")

    variable1 = 10
    _variable2 = 34.2
    variable3= "pepe"
    dos_palabras = "hola"
    dosPalabras = "Hello"

    print(variable1,_variable2,variable3,dos_palabras,dosPalabras)

    A,B,C = 98, 3.13416, "bIENVENIDO"
    print(A,B,C)

    nuevoTema("Enteros ")
    w=105
    x=2074074873847821
    y= -345
    z=0b0110011 #entero en binario.
    h=0xffa #entero enhexadecimal.

    print(w,type(w))
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
    print(h,type(h))

    nuevoTema("flotantes ")

    x=1297.5
    print(x,type(x))
    y=0.052829
    print(y,type(y))

    nuevoTema("Numeros Complejos")

    x = -46j
    y = 12+45j
    z = 2j

    print(x, type(x))
    print(y,type(y))    
    print(z,type(z))


    nuevoTema("Listas")

    a = [10,20.5,"phyton list"]
    print(a)

    a= ["listas2",45,16.3]
    print(a)
    print(a[2])
    a[1] = 34.6 
    print(a)

    nuevoTema("Tuplas")

    t = (25,"tupla",5.6)
    print(t)
    print(t[1])
    #t[0] = "Modificado" # Operacion no permitida
    #print(t)

    nuevoTema("Conjuntos")
    c = {50,20,10,4,8,50}
    print(c)

    nuevoTema("Diccionarios")
    d = {1: "valor2", "2":45}
    print(d, type(d))
    print(d["2"])
    print(d[1])

    nuevoTema("Cadenas")
    cadena1 = "cadena entre comillas dobles"
    print(cadena1)
    cadena2 = 'cadena entre comillas sencillas'
    print(cadena2)
    cadena3 = ''' Cadena de
    varias
    lineas'''
    print (cadena3)








    






