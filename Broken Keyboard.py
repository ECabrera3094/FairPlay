def brokenkeyboard(text, letters):

    # Validamos la Longitud del Texto y de las Letras.
    if (len(text) >= 1 and len(text) <= 1000) and (len(letters) >= 0 and len(letters) <= 25):
        # Convertimos a Minusculas el Texto dado que la Tecla Shift Funciona.
        text = text.lower()
        # Removemos los Espacios del Principio y Final en Caso de que Existan.
        text = text.strip()
        # Dividimos el Texto en Lista.
        list_Text = text.split()

        #print(list_Text)

        # Si la Longitus de Letters es Cero, Significa que el Resto de los Numeros y Caracteres Especiales SI Funcionan.
        if len(letters) == 0:
            return len(list_Text)
        else:
            intFinalCheck = 0

            # Evaluamos cada Palabra del Texto.
            for i in range(len(list_Text)):
                # Check in para cada Palabra.
                intCheck = 0
                # Obtenemos la Longitud de cada una de las Palabras.
                len_Word = len(list_Text[i])
                for j in range(len_Word):
                    # Evaluamos cada Letra de Letters.
                    for k in range(len(letters)):

                        if (list_Text[i][j] == letters[k]) or (
                        int(ord(list_Text[i][j]) >= 33 and int(ord(list_Text[i][j]) <= 47))):
                            # Si cada Letra de la Palabra CONCUERDA con cada Letra de Letters, el Check in Aumenta en 1.
                            intCheck += 1
                            # Si el TOTAL del Check in CONCUERDA con la Longitud de la Palabra, el Final Check Aumenta en 1.
                            if intCheck == len_Word:
                                intFinalCheck += 1
                            # Detenemos la Busqueda.
                            break
                        else:
                            intCheck += 0

            return intFinalCheck

    # De NO Cumplirse las Condiciones del Texto o Letras, regresa None.
    else:
        return None


if __name__ == '__main__':
    ans = brokenkeyboard("Hello, this is CodeSignal!", ['e','i','h','l','o','s'])
    print(ans)

    ans = brokenkeyboard("Hi, this is Chris!", ['r','s','t','c','h'])
    print(ans)

    ans = brokenkeyboard("2 + 3 = 5", [])
    print(ans)

    ans = brokenkeyboard("2 + 3 = 5", ['2','5'])
    print(ans)