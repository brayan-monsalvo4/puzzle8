import copy

class puzzle:
    def __init__(self):
        self.matriz = list()
        self.f_score = 0
        self.matriz_final = list()
        pass

    def rellenar_puzzle (self, lista):
        self.matriz = list(lista)

    def rellenar_puzzle_final(self, lista_final):
        self.matriz_final = lista_final

    def get_element_at(self, numeroFila, numeroColumna) -> int:
        return self.matriz[numeroFila-1][numeroColumna-1]

    def get_f_score (self):
        return self.f_score

    def get_matriz (self) -> list:
        return copy.deepcopy(self.matriz)

    def get_matriz_final (self) -> list:
        return copy.deepcopy(self.matriz_final)

    def print_matriz (self):
        for fila in self.matriz:
            print(fila)
        print()

    def find_zero (self) -> dict:
        ubicacion = dict()

        for fila in range(3):
            for columna in range(3):
                if self.matriz[fila][columna] == 0:
                    ubicacion.update({"x":fila+1})
                    ubicacion.update({"y":columna+1})
                    break
        
        return copy.deepcopy(ubicacion)

    def move_up(self, diccCoor={}) -> list:
        if diccCoor["x"] == 0 or diccCoor["y"] == 0 or len(self.get_matriz()) == 0:
            print("error, funcion move up valores incorrectos")
            return 

        if diccCoor["x"] == 1:
            raise ValueError("no pueden mover hacia arriba en la fila 1")

        x = diccCoor["x"]-1
        y = diccCoor["y"]-1    

        lis = self.get_matriz()
        
        temporal = lis[x-1][y]
        cero = lis[x][y]

        lis[x-1][y] = cero 
        lis[x][y] = temporal

        return copy.deepcopy(lis)
    
    def move_down (self,diccCoor) -> list:
        if diccCoor["x"] == 0 or diccCoor["y"] == 0 or len(self.get_matriz()) == 0:
            print("error, funcion move down valores incorrectos")
            return
        
        if diccCoor["x"] == 3:
            raise ValueError("no pueden moverse hacia abajo en la fila 3")

        x = diccCoor["x"]-1
        y = diccCoor["y"]-1    

        lista = self.get_matriz()
        
        temporal = lista[x+1][y]
        cero = lista[x][y]

        lista[x+1][y] = cero 
        lista[x][y] = temporal

        return copy.deepcopy(lista)

    def move_right (self, diccCoor) -> list:
        if diccCoor["x"] == 0 or diccCoor["y"] == 0 or len(self.get_matriz()) == 0:
            print("error, funcion move right valores incorrectos")
            return 

        if diccCoor["y"] == 3:
            raise ValueError("no pueden moverse a la derecha en la columna 3")

        x = diccCoor["x"]-1
        y = diccCoor["y"]-1    

        lis = self.get_matriz()
        
        temporal = lis[x][y+1]
        cero = lis[x][y]

        lis[x][y+1] = cero 
        lis[x][y] = temporal

        return copy.deepcopy(lis)

    def move_left (self, diccCoor) -> list:
        if diccCoor["x"] == 0 or diccCoor["y"] == 0 or len(self.get_matriz()) == 0:
            print("error, funcion move right valores incorrectos")
            return 

        if diccCoor["y"] == 1:
            raise ValueError("no pueden moverse a la izquierda en la columna 1")

        x = diccCoor["x"]-1
        y = diccCoor["y"]-1    
        
        lis = self.get_matriz()

        temporal = lis[x][y-1]
        cero = lis[x][y]

        lis[x][y-1] = cero 
        lis[x][y] = temporal

        return copy.deepcopy(lis)