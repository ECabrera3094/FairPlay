def divideArray(a):

    lenght_Array = len(a)
    divide_Array = [[], []]

    # Si la Longitud del Arreglo es PAR.
    if lenght_Array % 2 == 0:
        for i in range(lenght_Array):
            intCount = 0
            for j in range(lenght_Array):
                if a[i] == a[j]:
                    intCount += 1
                    # Si un Entero se Presenta MAS DE 2 VECES, NO existe Solucion.
                    if intCount > 2:
                        # NO Existe Solución.
                        return []
    # Si la Longitud del Arreglo NO es PAR.
    else:
        # NO se puede Dividir.
        return []

    # Se Ingresan los Valores Correspondientes a la Lista de Listas.
    for i in range(len(divide_Array)):
        if i == 0:
            # Trabajamos con los Elementos [0][]
            for j in range((lenght_Array//2)): # 0,1,2.
                divide_Array[i].append(a[j])
        elif i == 1:
            # Trabajamos con los Elementos [][1]
            for j in range((lenght_Array//2), lenght_Array): # 3,4,5.
                divide_Array[i].append(a[j])

    # Se Comprueba la Lista de Listas para Validar sus Datos Repetidos.
    intFlag_1 = 0 # Bandera que se Activara si en el Lado [0][] EXISTE un Valor Repetido.
    intFlag_2 = 0 # Bandera que se Activara si en el Lado [][1] EXISTE un Valor Repetido.
    for i in range(len(divide_Array)): # 0,1.
        for j in range(len(divide_Array[i])): # 0,1,2.
            intCount = 0
            for k in range(len(divide_Array[i])): # 0,1,2.
                if divide_Array[i][j] == divide_Array[i][k]:
                    intCount += 1
                    if (intCount >= 2) and (i == 0):
                        # Posicion de Elemento Repetido en el Lado [0][].
                        intPosition_1 = k
                        # Almacenamos al Elemento Repetido.
                        strRepeatValue_1 = divide_Array[i][k]
                        # Cambiamos la Referencia de la Bandera.
                        intFlag_1 = 1
                    elif (intCount >= 2) and (i == 1):
                        # Posicion de Elemento Repetido en el Lado [][1].
                        intPosition_2 = k
                        # Almacenamos al Elemento Repetido.
                        strRepeatValue_2 = divide_Array[i][k]
                        # Cambiamos la Referencia de la Bandera.
                        intFlag_2 = 1

    # Se Intercambian los Elementos Repetidos.
    # Si Dos Numeros que se Repiten estan en los Lados [0][1] de la Lista de Listas.
    if (intFlag_1 == 1) and (intFlag_2 == 1):
        # Emiliamnos de la Lista de Listas los Elementos Repetidos.
        for i in range(len(divide_Array)):  # 0,1.
            if i == 0:
                divide_Array[i].pop(intPosition_1)
            elif i == 1:
                divide_Array[i].pop(intPosition_2)

        # Insertamos los Valores Repetidos en la Lista de Listas OPUESTA.
        for i in range(len(divide_Array)):  # 0,1.
            if i == 0:
                divide_Array[i].append(strRepeatValue_2)
            elif i == 1:
                divide_Array[i].append(strRepeatValue_1)

    # Si Dos Numeros que se Repiten estan en el Lado [0][] de la Lista de Listas.
    elif (intFlag_1 == 1) and (intFlag_2 == 0):
        for i in range(3):
            # Se Busca un Candidato a Intercambiar Diferente.
            if divide_Array[0][intPosition_1] != divide_Array[1][i]:
                intReplacePosition = i
                strReplaceValue = divide_Array[1][i]

        strRepeatValue_1 = divide_Array[0][intPosition_1]

        # Emiliamnos de la Lista de Listas los Elementos Repetidos.
        for i in range(len(divide_Array)):
            if i == 0:
                divide_Array[i].pop(strRepeatValue_1)
            elif i == 1:
                divide_Array[i].pop(intReplacePosition)

        # Insertamos los Valores Repetidos en la Lista de Listas OPUESTA.
        for i in range(len(divide_Array)):
            if i == 0:
                divide_Array[i].append(strReplaceValue)
            elif i == 1:
                divide_Array[i].append(strRepeatValue_1)

    # Si Dos Numeros que se Repiten estan en el Lado [][0] de la Lista de Listas.
    elif (intFlag_1 == 0) and (intFlag_2 == 1):
        for i in range(3):
            # Se Busca un Candidato a Intercambiar Diferente.
            if divide_Array[1][intPosition_2] != divide_Array[0][i]:
                intReplacePosition = i
                strReplaceValue = divide_Array[0][i]

        strRepeatValue_2 = divide_Array[1][intPosition_2]

        # Emiliamnos de la Lista de Listas los Elementos Repetidos.
        for i in range(len(divide_Array)):
            if i == 0:
                divide_Array[i].pop(intReplacePosition)
            if i == 1:
                divide_Array[i].pop(strRepeatValue_2)

        for i in range(len(divide_Array)):
            if i == 0:
                divide_Array[i].append(strRepeatValue_2)
            elif i == 1:
                divide_Array[i].append(strReplaceValue)

    # Lista de Listas FINAL
    return (divide_Array)


if __name__ == '__main__':
    ans = divideArray([2,3,2,1,3,4,8])
    print(ans)
    ans = divideArray([2,3,2,1,3,4,8,2])
    print(ans)
    ans = divideArray([2,3,2,1,3,4])
    print(ans)
    ans = divideArray([2,1,2,3,3,4])
    print(ans)
    ans = divideArray([1,3,4,2,3,2])
    print(ans)
    ans = divideArray([1,2,3,4,5,6])
    print(ans)