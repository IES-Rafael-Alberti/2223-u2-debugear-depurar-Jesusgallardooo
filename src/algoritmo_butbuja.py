# Práctica 2.4: Bucle burbuja / ordenar listas.


if __name__ == "__main__":
    
    SecuenciaDesordenada = [1, 10, 7, 19, 13, 3, 15]
    
    
    ordenado = False #Está desordenado (T/F)
    while ordenado == False: #Recorre todo hasta que no esté desordenado y por tanto no entre al if
        ordenado = True #Si no entra en el if, en el último recorrido tendra valor True y no repetirá el bucle while
        for i in range(len(SecuenciaDesordenada)-1): 
            if SecuenciaDesordenada[i] > SecuenciaDesordenada[i+1]: #compara cada elemento con su elemento de su derecha
                guardarNumero = SecuenciaDesordenada[i] #guarda el número de la derecha para sustituir y hacer el cambio por el de su derecha
                SecuenciaDesordenada[i] = SecuenciaDesordenada[i+1] # al menor le da el valor del mayor 
                SecuenciaDesordenada[i+1] = guardarNumero # y al mayor le da el valor del menor 
                ordenado = False
    
    print(SecuenciaDesordenada) #ordenada