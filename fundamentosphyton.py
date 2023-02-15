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


    






