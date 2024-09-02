class Fechas:
    def conv_fecha(self,fecha):
        dias = {
            1: "Uno", 2: "Dos", 3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez",
            11: "Once", 12: "Doce", 13: "Trece", 14: "Catorce", 15: "Quince", 16: "Dieciséis", 17: "Diecisiete", 18: "Dieciocho", 
            19: "Diecinueve", 20: "Veinte", 21: "Veintiuno", 22: "Veintidós", 23: "Veintitrés", 24: "Veinticuatro", 25: "Veinticinco", 
            26: "Veintiséis", 27: "Veintisiete", 28: "Veintiocho", 29: "Veintinueve", 30: "Treinta", 31: "Treinta y uno"
        }

        meses = {
            1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 
            10: "Octubre", 11: "Noviembre", 12: "Diciembre"
        }

        unidades = {
            0: "", 1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco", 6: "seis", 7: "siete", 8: "ocho", 9: "nueve"
        }

        decenas_dict = {
            10: "diez", 20: "veinte", 30: "treinta", 40: "cuarenta", 50: "cincuenta", 60: "sesenta",
            70: "setenta", 80: "ochenta", 90: "noventa"
        }

        dia_str, mes_str, año_str = fecha.split('/')
        dia = int(dia_str)
        mes = int(mes_str)
        año = int(año_str)
    
        dia_palabras = dias[dia]
        mes_palabras = meses[mes]

        miles = año // 1000
        centenas = (año % 1000) // 100
        decenas_y_unidades = año % 100
    
        miles_palabras = "mil" if miles == 1 else f"{unidades[miles]} mil"
        centenas_palabras = "" if centenas == 0 else f"{unidades[centenas]}cientos"
    
        if decenas_y_unidades < 10:
            decenas_y_unidades_palabras = unidades[decenas_y_unidades]
        elif decenas_y_unidades < 20:
            decenas_y_unidades_palabras = decenas_dict[decenas_y_unidades]
        else:
            decena = decenas_y_unidades // 10 * 10
            unidades_restantes = decenas_y_unidades % 10
            if unidades_restantes != 0:
                decenas_y_unidades_palabras = f"{decenas_dict[decena]} y {unidades[unidades_restantes]}"
            else:
                decenas_y_unidades_palabras = decenas_dict[decena]

        if centenas == 0 and decenas_y_unidades == 0:
            año_palabras = miles_palabras.strip()
        else:
            año_palabras = f"{miles_palabras} {centenas_palabras} {decenas_y_unidades_palabras}".strip()

        formato_fecha = f"{dia_palabras} de {mes_palabras} del {año_palabras}" 
        return formato_fecha