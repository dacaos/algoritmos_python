from math import log10 as l

#Algoritmos implementados para la clase de analisis de algoritmos en python


#Algoritmo del factorial recursivo

def factorial(n):
    if(n==1):
        return 1;
    else:
        return n * factorial(n-1)
#######
# Metodo para  saber si un array esta contenido en otro o no


def contiene(arr,arr2):
     if(len(arr)>= len(arr2)):
         j=0
         for i in range(0,len(arr)):
             if(arr[i]==arr2[j]):
                  j=j+1
                  if(j>=len(arr2)):
                      return True
             else:
                 j=0
     return False

#ALgoritmo del primer previo

def getMayor(n):
    digitos = int(l(n))+1
    arr_digitos=[]
    aux = n
    for i in range(digitos):
        arr_digitos.append(int(aux%10))
        aux = aux/10

    metodo_burbuja(arr_digitos)

    numero = 0
    var = 1
    aux=0
    i=0
    while(i<digitos):
          aux = arr_digitos[i]*var
          numero = numero + aux
          var = var*10
          i= i+1
    return numero

## metodo auxiliar para poder llevar a cabo mi aLgoritmo
def metodo_burbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


x = int(input("Digite el numero: "))
y = getMayor(x)

print("EL numero mayor formado es: "+str(y))

## metodo para saber si un numero es primo
def es_primo(numero):
    for i in range(2,numero):
        if (numero%i)==0:
            # es divisible
            return False
    return True
 
while True:
    try:
        numero = int(raw_input("inserta un numero (0) salir >> "))
        if numero==0:
            break
        if es_primo(numero):
            print "\nEl numero %s es primo" % numero
        else:
            print "\nEl numero %s NO es primo" % numero
    except:
        print "\nEl numero tiene que ser entero"
