class Promedios:
    def promedio(self, *calificaciones):
        if len(calificaciones) == 0:
            return "No se proporcionaron calificaciones"
        if any(isinstance(cal, list) for cal in calificaciones):
            return "No se pueden promediar listas"
        if any(isinstance(cal, bool) for cal in calificaciones):
            return "No se aceptan valores booleanos"
        if any(isinstance(cal, str) for cal in calificaciones):
            return "La calificación debe ser un numero"
        if any(cal > 10 for cal in calificaciones):
            return "Calificación maxima es 10"
        if any(cal < 0 for cal in calificaciones):
            return "La calificación no puede ser menor que cero"
        if any(not isinstance(cal, int) for cal in calificaciones):
            return "La calificación debe ser un número entero"
        if all(cal == 0 for cal in calificaciones):
            return 0
        else:
            suma = sum(calificaciones)
            return round(suma / len(calificaciones), 2)