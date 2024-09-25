Característica: Mensaje de acuerdo a tu edad
    Como usuario del sistema edades
    quiero ingresar mi edad
    para obetener un mensaje con respecto a esa edad.

    Escenario: Edad menor a 0
        Dado que ingreso al sistema la edad de "-1"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "No existes"

        Escenario: Edad es 3
        Dado que ingreso al sistema la edad de "3"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Eres un niño"

        Escenario: Ingreso de caracter 
        Dado que ingreso al sistema el caracter "X"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Edad solo numerica"

        Escenario: Edad es 16 
        Dado que ingreso al sistema la edad de "16"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Eres un adolecente"

        Escenario: Edad es 25
        Dado que ingreso al sistema la edad de "25"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Eres un adulto"

        Escenario: Edad es 61
        Dado que ingreso al sistema la edad de "61"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Eres un adulto mayor"

        Escenario: Edad es mayor o igual a 110
        Dado que ingreso al sistema la edad de "110"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Eres un mumm-ra"

        Escenario: Edad con decimal 
        Dado que ingreso al sistema el caracter "19.5"
        Cuando presiono el botón Mensaje
        Entonces puedo ver el mensaje "Edad solo numerica"