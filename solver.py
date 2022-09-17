import copy
import puzzle

class solver:
    def __init__(self):
        self.pasos = list()
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

    def resolver (self, puzzle=puzzle.puzzle) -> list:
        pasos_temporal = list()
        fallas_temporal = list()
        paso_final_temporal = list()

        while ( puzzle.get_matriz_final() not in paso_final_temporal ):
            matriz = list()
            matriz_final = list()

            try:
                matriz = puzzle.move_up( puzzle.find_zero() )
                matriz_final = puzzle.get_matriz_final()

                numero_fallos = self.contar_numero_fallas(matriz, matriz_final)

                pasos_temporal.append(matriz)
                fallas_temporal.append(numero_fallos)
            except Exception:
                pass

            try:
                matriz = puzzle.move_down( puzzle.find_zero() )
                matriz_final = puzzle.get_matriz_final()

                numero_fallos = self.contar_numero_fallas(matriz, matriz_final)

                pasos_temporal.append(matriz)
                fallas_temporal.append(numero_fallos)
            except Exception as e:
                pass

            try:
                matriz = puzzle.move_left( puzzle.find_zero() )
                matriz_final = puzzle.get_matriz_final()

                numero_fallos = self.contar_numero_fallas(matriz, matriz_final)

                pasos_temporal.append(matriz)
                fallas_temporal.append(numero_fallos)
            except Exception as e:
                pass

            try:
                matriz = puzzle.move_right( puzzle.find_zero() )
                matriz_final = puzzle.get_matriz_final()

                numero_fallos = self.contar_numero_fallas(matriz, matriz_final)

                pasos_temporal.append(matriz)
                fallas_temporal.append(numero_fallos) 
            except Exception as e:
                pass

            for i in range( len(fallas_temporal) ):
                fallas_temporal[i] = fallas_temporal[i] + len( paso_final_temporal )

            ordenada = list(copy.deepcopy(fallas_temporal))
            ordenada.sort()
            
            paso_final_temporal.append( pasos_temporal[ fallas_temporal.index( ordenada[0] ) ] )

            puzzle.rellenar_puzzle( paso_final_temporal[-1] )
                
            
        return paso_final_temporal


