Característica: Inicio de sesión
Como usuario del sistema
necesito iniciar sesiión
para realizar mis actividades dentro del sistema.


        Escenario: Credenciales correctas
            Dado que  ingreso mi usuario "alex" y contraseña "admin123"
             Cuando presiono el botón  Identificarse
             Entonces puedo ver el mensaje de "BIENVENIDO, ALEX"

        Escenario: Credenciales incorrectas
            Dado que  ingreso mi usuario "alexxx" y contraseña "admin123"
             Cuando presiono el botón  Identificarse
             Entonces puedo ver el mensaje de error "Por favor introduza nombre de usuario y contraseña correctos de una cuenta de staff. Note que puede que ambos campos sean estrictos en relación a diferencias entre mayúsculas y minúsculas."