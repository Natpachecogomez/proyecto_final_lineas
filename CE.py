#Importar diccionario tabla periódica
import Dc_proyecto 
diccionario=Dc_proyecto.Tablaperiodica

#Lista configuración electrónica
confele=[("1S",2),("2S",2),("2P",6),("3S",2),("3P",6),("4S",2),("3D",10),("4P",6),("5S",2),("4D",10),("5P",6),("6S",2),("4F",14),("5D",10),("6P",6),("7S",2),("5F",14),("6D",10),("7P",6),("6F",14),("7D",10),("7F",14)]

#Preguntar si ingresa elemento o número cuánticos
e=0
inicio=input("Para ingresar un elemento escriba e, para números cuánticos nc: ")
if inicio!="e" and inicio!="nc":
    inicio=input("Escriba e o nc: ")

#PROGRAMA PARA CUANDO INGRESA UN ELEMENTO
if inicio=="e":
    ele=input("Ingrese nombre o símbolo del elemento: ")
    for i in diccionario:
        if ele==diccionario[i]["Nombre"] or ele==diccionario[i]["Símbolo"]:
            print("Símbolo:", diccionario[i]["Símbolo"])
            print("Nombre:",diccionario[i]["Nombre"])
            print("Número atómico:",diccionario[i]["Número atómico"])
            print("Peso atómico:",diccionario[i]["Peso atómico"])
            print("Grupo:",diccionario[i]["Grupo"])
            print("Periodo:",diccionario[i]["Periodo"])
            print("Configuración electrónica:",diccionario[i]["Configuración electrónica"])

#PROGRAMA PARA CUANDO INGRESA NÚMEROS CUÁNTICOS
if inicio=="nc":
    #Rango de n
    n=int(input("Ingrese valor de n: "))
    if n>7 or n<1:
        print("El valor de n debe estar entre 1 y 7")
        n=int(input("Ingrese valor de n: "))

    #Rango de l y m, definir letras de l
    l=int(input("Ingrese valor de l: "))
    if l<0 or l>3:
        print("El valor de l debe estar entre 0 y 3")
        l=int(input("Ingrese valor de l: "))
    m=int(input("Ingrese valor de m: "))
    if l==0:
        l="S"
        if m!=0:
            print("El valor de m no puede ser diferente de 0")
            m=int(input("Ingrese valor de m: "))
    elif l==1:
        l="P"
        if m<-1 or m>1:
            print("El valor de m debe estar entre -1 y 1")
            m=int(input("Ingrese valor de m: "))
    elif l==2:
        l="D"
        if m<-2 or m>2:
            print("El valor de m debe estar entre -2 y 2")
            m=int(input("Ingrese valor de m: "))
    else:
        l="F"
        if m<-3 or m>3:
            print("El valor de m debe estar entre -3 y 3")
            m=int(input("Ingrese valor de m: "))

    #Rango de s
    s=input("Ingrese si es positivo (+) o negativo(-): ")
    if s!="+" and s!="-":
        print("El valor de s debe ser + o -")
        s=input("Ingrese si es positivo (+) o negativo(-): ")

    #Definir exponente que se suma para hallar z
    #S
    if l=="S" and m==0:
        if s=="+":
            e=1
        else:
            e=2

    #P
    if l=="P" and m==-1:
        if s=="+":
            e=1
        else:
            e=4
    if l=="P" and m==0:
        if s=="+":
            e=2
        else:
            e=5
    if l=="P" and m==1:
        if s=="+":
            e=3
        else:
            e=6

    #D
    if l=="D" and m==-2:
        if s=="+":
            e=1
        else:
            e=6
    if l=="D" and m==-1:
        if s=="+":
            e=2
        else:
            e=7
    if l=="D" and m==0:
        if s=="+":
            e=3
        else:
            e=8
    if l=="D" and m==1:
        if s=="+":
            e=4
        else:
            e=9
    if l=="D" and m==2:
        if s=="+":
            e=5
        else:
            e=10

    #F
    if l=="F" and m==-3:
        if s=="+":
            e=1
        else:
            e=8
    if l=="F" and m==-2:
        if s=="+":
            e=2
        else:
            e=9
    if l=="F" and m==-1:
        if s=="+":
            e=3
        else:
            e=10
    if l=="F" and m==0:
        if s=="+":
            e=4
        else:
            e=11
    if l=="F" and m==1:
        if s=="+":
            e=5
        else:
            e=12
    if l=="F" and m==2:
        if s=="+":
            e=6
        else:
            e=13
    if l=="F" and m==3:
        if s=="+":
            e=7
        else:
            e=14   

    #Suma exponentes anteriores al que cambia
    sum=0
    for i in confele:
        sum=i[1]+sum
        if i[0][0]==str(n) and i[0][1]==l:
            sum=sum-i[1]
            break

    #Encotrar z
    z=sum+e
    
    #Encontrar elemento con z de número atómico e imprimir toda su info
    for i in diccionario:
        if int(i)==z:
            print("Símbolo:", diccionario[i]["Símbolo"])
            print("Nombre:",diccionario[i]["Nombre"])
            print("Número atómico:",diccionario[i]["Número atómico"])
            print("Peso atómico:",diccionario[i]["Peso atómico"])
            print("Grupo:",diccionario[i]["Grupo"])
            print("Periodo:",diccionario[i]["Periodo"])
            print("Configuración electrónica:",diccionario[i]["Configuración electrónica"])