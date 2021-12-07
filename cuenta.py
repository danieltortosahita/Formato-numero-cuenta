if __name__ != "__main__":

    def get_cuenta(cuenta):

        diccionario_caracteres={

            ' ':'',
            '-':'',
            '\t':'',
            '/':'',

        }


        for caracter, valor_nuevo in diccionario_caracteres.items():
            cuenta = cuenta.replace(caracter, valor_nuevo)

        if cuenta.upper().find("ES") == 0:
            cuenta = cuenta[4:len(cuenta)]

        if cuenta.isnumeric() is False:
            resultado = "El número de cuenta contiene caracteres no numéricos."

        else:

            if len(cuenta) != 20:

                resultado = "El número de cuenta no tiene 20 dígitos."

            else:

                entidad = cuenta[0:4]

                oficina = cuenta[4:8]

                dc = cuenta[8:10]

                n_cuenta = cuenta[10:21]

                resultado = f"{entidad}/{oficina}/{dc}/{n_cuenta}"

        return resultado
