class tenisMatch:
    def __init__(self):
        self.score_jugador1 = 0
        self.score_jugador2 = 0
        self.puntos = [0, 15, 30, 40, 50, 'AVG']
        self.juego_finalizado = False

    def anotar_punto(self, jugador):
        if self.juego_finalizado:
            return "El juego ya ha terminado"

        if jugador == 1:
            if isinstance(self.score_jugador1, int) and self.score_jugador1 == 50 and isinstance(self.score_jugador2, int) and self.score_jugador2 < 50:
                print("Jugador 1 gana")
                self.juego_finalizado = True
                return "Jugador 1 gana"
            elif isinstance(self.score_jugador1, int) and self.score_jugador1 < 50:
                self.score_jugador1 = self.puntos[self.puntos.index(self.score_jugador1) + 1]
                if self.score_jugador1 == 50 and isinstance(self.score_jugador2, int) and self.score_jugador2 < 40:
                    print("Jugador 1 gana")
                    self.juego_finalizado = True
                    return "Jugador 1 gana"
            elif self.score_jugador1 == 50 and self.score_jugador2 == 50:
                self.score_jugador1 = 'AVG'
            elif self.score_jugador1 == 'AVG':
                if self.score_jugador2 == 'AVG':
                    self.score_jugador2 = 50
                else:
                    print("Jugador 1 gana")
                    self.juego_finalizado = True
                    return "Jugador 1 gana"

        elif jugador == 2:
            if isinstance(self.score_jugador2, int) and self.score_jugador2 == 50 and isinstance(self.score_jugador1, int) and self.score_jugador1 < 50:
                print("Jugador 2 gana")
                self.juego_finalizado = True
                return "Jugador 2 gana"
            elif isinstance(self.score_jugador2, int) and self.score_jugador2 < 50:
                self.score_jugador2 = self.puntos[self.puntos.index(self.score_jugador2) + 1]
                if self.score_jugador2 == 50 and isinstance(self.score_jugador1, int) and self.score_jugador1 < 40:
                    print("Jugador 2 gana")
                    self.juego_finalizado = True
                    return "Jugador 2 gana"
            elif self.score_jugador2 == 50 and self.score_jugador1 == 50:
                self.score_jugador2 = 'AVG'
            elif self.score_jugador2 == 'AVG':
                if self.score_jugador1 == 'AVG':
                    self.score_jugador1 = 50
                else:
                    print("Jugador 2 gana")
                    self.juego_finalizado = True
                    return "Jugador 2 gana"

    def obtener_score(self):
        if self.juego_finalizado:
            return "El juego ha terminado."
        if self.score_jugador1 == 50 and self.score_jugador2 == 50:
            return "Deuce"
        elif self.score_jugador1 == 'AVG' and self.score_jugador2 == 'AVG':
            return "Deuce"
        elif self.score_jugador1 == 'AVG':
            return "Ventaja Jugador 1"
        elif self.score_jugador2 == 'AVG':
            return "Ventaja Jugador 2"
        else:
            formato_score = f"Jugador 1: {self.score_jugador1} - Jugador 2: {self.score_jugador2}"
            return formato_score


juego = tenisMatch()