def reverseDigitsInPairs(n):

    list_Reverse = []

    # Si el Arreglo es Par.
    if len(n) % 2 == 0:
        for i in range(0, len(n), 2):
            # En la Posicion 0 Insertamos lo que esta en la Posicion 0+1.
            list_Reverse.insert(i, n[i + 1])
            # En la Posicion 0+1 Insertamos lo que esta en la Posicion 0.
            list_Reverse.insert(i+1, n[i])

    # Si el Arreglo es Impar.
    else:
        # Al ser un Arreglo Impar, Insertaremos el Ultimo Valor de n[] y lo Eliminaremos, para Transformarlo en Par APROX.
        # Obtenemos la Longitud de N - 1.
        length_n = len(n) - 1
        # Insertamos en la Ultima Posicion de la Lista Reversa, el Ultimo Valor de n[]
        list_Reverse.insert(length_n, n[length_n])
        # Eliminamos del Arreglo n[] el Ultimo Valor y con Base a Este, sera con el que Trabajemos.
        n.pop(length_n)
        for i in range(0, len(n), 2):
            # En la Posicion 0 Insertamos lo que esta en la Posicion 0+1.
            list_Reverse.insert(i, n[i + 1])
            # En la Posicion 0+1 Insertamos lo que esta en la Posicion 0.
            list_Reverse.insert(i+1, n[i])

    return (list_Reverse)

if __name__ == '__main__':
    ans = reverseDigitsInPairs([1,2,3,4,5,6])
    print(ans)
    ans = reverseDigitsInPairs([7,2,3,2,8])
    print(ans)