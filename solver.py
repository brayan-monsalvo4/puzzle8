import copy

class solver:
    def solver(self):
        self.pasos = dict()
        pass
    
    def contar_numero_fallas (self, listInit, listFin) -> int:
        count = 0

        for fila in range(3):
            for columna in range(3):
                elementoInicial = listInit[fila][columna]
                elementoFinal = listFin[fila][columna]

                if elementoInicial != elementoFinal and elementoInicial != 0:
                    count += 1

        return count
