confele=[("1S",2),("2S",2),"2P6","3S2","3P6","4S2","3D10","4P6","5S2","4D10","5P6","6S2","4F14","5D10","6P6","7S2","5F14","6D10","7P6"]

#Pedir datos
n=int(input("Ingrese valor de n: "))
l=int(input("Ingrese valor de l: "))
m=int(input("Ingrese valor de m: "))
s=input("Ingrese si es positivo (+) o negativo(-): ")
e=0

#Rango de n
if n>7 and n<1:
    print("El valor de n debe estar entre 1 y 7")
    n=int(input("Ingrese valor de n: "))

#Rango de l y m, definir letras de l
if l<0 and l>3:
    print("El valor de l debe estar entre 0 y 3")
    l=int(input("Ingrese valor de l: "))
if l==0:
    l="S"
    if m!=0:
        print("El valor de m no puede ser diferente de 0")
        m=int(input("Ingrese valor de m: "))
elif l==1:
    l="P"
    if m<-1 and m>1:
        print("El valor de m debe estar entre -1 y 1")
        m=int(input("Ingrese valor de m: "))
elif l==2:
    l="D"
    if m<-2 and m>2:
        print("El valor de m debe estar entre -2 y 2")
        m=int(input("Ingrese valor de m: "))
else:
    l="F"
    if m<-3 and m>3:
        print("El valor de m debe estar entre -3 y 3")
        m=int(input("Ingrese valor de m: "))

#Rango de s
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
        e=10
if l=="F" and m==-2:
    if s=="+":
        e=2
    else:
        e=11
if l=="F" and m==-1:
    if s=="+":
        e=3
    else:
        e=12
if l=="F" and m==0:
    if s=="+":
        e=4
    else:
        e=13
if l=="F" and m==1:
    if s=="+":
        e=5
    else:
        e=14
if l=="F" and m==2:
    if s=="+":
        e=6
    else:
        e=15
if l=="F" and m==3:
    if s=="+":
        e=7
    else:
        e=16   

sum=0
for i in confele:
    sum=int(i[2])+sum
    if i[0]==str(n) and i[1]==l:
        pass
print(sum)