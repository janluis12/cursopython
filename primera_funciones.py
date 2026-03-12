#def mensaje(): #declaracion de mi funcion

	#print("don eduardo es gay") #cuerpo de la funcion
	#print("el ñema")
	#print("ayudame nicola")

#mensaje() #llamada de la funcion

#mensaje ()
#print("michi tu ta toa rica xd")






#def suma(num1,num2): #funcion que recibe parametros
	
	#print(num1*num2)

#suma(10,20)#llamando la funcion suma


#def maquinita(num1,num2):
	#resultado = num1+num2
	#return resultado #opcional
#almacena_resultado = maquinita(10,20)
	
#print(almacena_resultado)

#milista=["jan","mariana","martita","jose"]
#milista.append("mamaguevo") #agrega elementos a nuestra lista
#milista.insert(2,"sandra")#inserta un elemento apartir de la seccion que se le asigne
#milista.extend(["pepe","mariana"])#inserta nuevos elementos a nuestra lista
#milista.remove("jose")#elimina un elemento de nuestra lista, en particular, el que indiquemos.
#milista.pop()#elimina el ultimo valor de nuestra lista
#print(milista[:]) #accediendo a la lista
#print(milista.index("pepe"))#index es para buscar un dato especifico de nuestro arrays, y si existen datos que se repitan, siempre imprimira el primero que encuentre.
#print(milista[0:3])#accediendo a una porcion de la lista
#print("jan" in milista) #nos sirve para saber si un elemento de nuestra lista, esta o no, en este caso true or false

#tuplas sintaxis basica

#mitupla = ("jan","mariana","pepito")
#mitupla=list(mitupla) #convertimos nuestra tupla a una lista
#mitupla=tuple(mitupla)#convertimos una lista a tupla
#print(mitupla)
#print("jan" in mitupla) #podemos saber si un elemento, se encuentra en nuestra tupla.
#print(mitupla.count("mariana")) #con count, podremos saber cuantas veces se encuentra en nuestra tupla.
#print(len(mitupla))# con el metodo len, podremos saber la longitud de nuestra tupla.

#los diccionarios

#midiccionario = {"santiago":"chile","francia":"paris","santo domingo":"republica dominicana"}
#print(midiccionario["santo domingo"])#de esta forma podremos acceder a una clave en especifico
#midiccionario["españita"]="lisboaxd" #con esto podremos agregar nuevos valores a nuestros diccionario
#del midiccionario["santiago"] #con esto podremos eliminar un elemento de nuestro diccionario
#print(midiccionario.keys())#con este metodo podremos saber las llaves que contienen nuestro diccionario
#print(midiccionario.values())# con este metodo podremos saber lo que contienen dentro las llaves.
#print(midiccionario)

#mi_lista = ["santo domingo","chile","francia"] #aqui declaramos una tupla que seran utilizadas como elementos para nuestras claves de nuestro diccionario
#mi_diccionario = {mi_lista[0]:"republica dominicana",mi_lista[1]:"region metropolitana"} #aqui declaramos nuestro diccionario junto con nuestra tupla, iniciando en nuestro elemento 0, para asi entonces a nuestra llave agregar su elemento
#print(mi_diccionario)

#condicionales if
#print("ingresa tu nombre mamañema")
#nombre = input("nombre")
#edad = int(input("edad"))
#def usuario(nombre,edad):
	
	#if (nombre =="jan" and edad>=18):
		
		#print("cumple es mayor")
		#print("programa finalizado papito")
		#return
	#else:
		#print("maldito gey eres mayor")
		#return
#print(usuario(nombre,edad))


#-------------------contatenacion de operadores-------------#

#salario_presidente = int(input("ingresa el salario el presidente"))
#print("salario presidente " + str(salario_presidente))
#salario_director = int(input("ingresa el salario el director"))
#print("salario director " + str(salario_director))
#salario_jefe_area = int(input("ingresa el salario del jefe de area"))
#print("salario jefea area " + str(salario_jefe_area))
#salario_administrativo = int(input("ingresa el salario miserable del administrativo"))
#print("salario administrativo " + str(salario_administrativo))
#
#if (salario_presidente>salario_director>salario_jefe_area>salario_administrativo):
#	print("todo esta bien en la empresa")
#else:
#	print("algo no esta funcionando en esta empresa")

#bucles for determinados
#for i in [1,2,3,4,5,6,7,8,9]:
	#print("buenas", i)

#email = False
#
#for i in "janluis@gmail.com":
#	
#	if( i=="@" or i=="."):
#
#		email=True
#if email:
#	print("cumples")
#else:
#	print("no cumples")

#for i in range(5,45,5):
	#print(f"valor de la variable {i}") #tipo de concatenacion


#bucle while
#i=1

#while i<=10:
	#print("ejecucion programa" + str(i))
	#i=i+1
#print("termino la ejecucion")

#edad = int(input("ingresa tu  edad por favor"))
#
#while edad<5 or edad>100:
#
#	print("has introducido una edad negativa, vuelve a intentarlo")
#	edad = int(input("ingresa tu  edad por favor"))
#
#print("edad del aspirante " + str(edad) + " años")

""" def cajero():
    print("Cajero de chile")
    saldo = 1000
    respuesta = input("deseas ingresar al cajero: ")

    while respuesta == "si":
        rut_usuario = input("Por favor ingresa tu rut: ")
        contraseña_usuario = input("Por favor ingresa tu pin: ")

        if rut_usuario == "25014207-2" and contraseña_usuario == "2902":
            print("Session iniciada correctamente")

            opcion = "0"

            while opcion != "4":
                print("escoja una de las siguientes operaciones")
                print("1-Consultar saldo")
                print("2-depositar saldo")
                print("3-retirar saldo")
                print("4-salir")

                opcion = input("por favor selecciona una opcion: ")

                if opcion == "1":
                    print("tu saldo es igual a:", saldo)

                elif opcion == "2":
                    nuevomonto = int(input("ingresa tu deposito: "))
                    saldo += nuevomonto
                    print("tu nuevo saldo es:", saldo)
               
                elif opcion =="3":
                    nuevomonto = int(input("ingresa el saldo a retirar"))
                    if nuevomonto>saldo or nuevomonto<=0:
                        print("no se puede retirar")
                    else:
                        saldo -=nuevomonto
                        print("retiro realizado con exito, saldo disponible ", saldo)
                       
                       
                   

        else:
            print("Datos incorrectos vuelva a intentarlo")

        respuesta = input("deseas ingresar nuevamente al cajero: ")
    print("programa terminado con exito")

cajero()

 """









""" print("bienvenidos a la calculadora")

respuesta_usuario=input("deseas ingresar a la calculadora")

numero1=int(input("ingresa un numero"))
numero2=int(input("ingresa un numero"))

if respuesta_usuario=="si":
    opciones_usuario=input("por favor escoge una de las siguientes operaciones a realizar suma,resta,multiplicacion,division").lower()
   
   
    if opciones_usuario=="suma":
       
        resultado= numero1+numero2
        print("resultado es ", resultado)
       
    elif opciones_usuario =="resta":
       
        resultado= numero1-numero2
        print("resultado es ", resultado)
       
    elif opciones_usuario =="multiplicacion":
       
        resultado= numero1*numero2
        print("resultado es ", resultado)
       
    elif opciones_usuario =="division":
       
        resultado= numero1/numero2
        print("resultado es ", resultado)
    else:
        print("opcion no valida, vuelva a intentarlo nuevamente.")
   
else:
    print("programa terminado") """