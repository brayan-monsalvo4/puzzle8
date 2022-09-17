import puzzle
import solver
import copy

puzz = puzzle.puzzle()
solv = solver.solver()


m = [[1, 2, 3], 
     [0, 4, 6], 
     [7, 5, 8]]

final = [[1,2,3], 
          [4, 5, 6], 
          [7, 8, 0]]

puzz.rellenar_puzzle(m)
puzz.rellenar_puzzle_final(final)

puzz.print_matriz()

lis = solv.resolver(puzz)

for resultado in lis:
     for fila in resultado:
          print(fila)
     print()
