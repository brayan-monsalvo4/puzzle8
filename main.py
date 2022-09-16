import puzzle
import solver
import copy

puzz = puzzle.puzzle()
solv = solver.solver()


m = [[1,2,3], 
     [4,0,6], 
     [7,5,8]]

final = [[1,2,3], 
          [4,5,6], 
          [7,8,0]]

puzz.rellenar_puzzle(m)

puzz.print_matriz()

print( puzz.move_up( puzz.find_zero() ) )

puzz.print_matriz()

puzz.rellenar_puzzle( puzz.move_up( puzz.find_zero() ) )

puzz.print_matriz()
