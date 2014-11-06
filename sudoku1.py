
MAX = 9
TEST_MATRIX = [
        [4,8,1,5,0,9,6,7,0],
        [3,0,0,8,1,6,0,0,2],
        [5,0,0,7,0,3,0,0,8],
        [2,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,1],
        [8,0,0,0,0,0,0,0,4],
        [0,3,9,2,7,5,4,8,0],
        [6,0,0,0,0,0,9,2,7],
        [7,0,0,0,0,0,3,1,0]
]
class cell(object):
    matrix = None
    def __init__(self, val, r, c, matrix):
        if val != 0:
            self.value = {val,}
        else:
            self.value = {1, 2, 3, 4, 5, 6, 7, 8, 9,}
        self.row = r
        self.col = c
        self.block = self.blockNumber(r, c)
        cell.matrix = matrix

def createMatrix():
    M = [
        [4,8,1,5,0,9,6,7,0],
        [3,0,0,8,1,6,0,0,2],
        [5,0,0,7,0,3,0,0,8],
        [2,0,0,0,0,0,0,0,9],
        [9,0,0,0,0,0,0,0,1],
        [8,0,0,0,0,0,0,0,4],
        [0,3,9,2,7,5,4,8,0],
        [6,0,0,0,0,0,9,2,7],
        [7,0,0,0,0,0,3,1,0]
    ]
    matrix = []
    for r in range(MAX):
        row = []
        for c in range(MAX):
            row.append(Cell(M[r][c],r,c,matrix))
        matrix.append(row)
    return matrix
def restoreValues(matrix, oldMatrix):
    for r in range(MAX):
        for c in range(MAX):
            matrix[r][c].value = oldMatrix[r][c].value
    return matrix
def recursivelySolveTheSudoku(matrix):
    matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
    if badMatrix(matrix) or solutionIsCorrect(matrix):
        return matrix
    oldMatrix = deepcopy(matrix)
    r, c = coordinatesofCellWithSmallestValueSet(matrix)
    for guess in matrix[r][c].value:
        matrix[r][c].value = {guess,}
        matrix = recursivelySolveTheSudoku(matrix)
        if solutionIsCorrect(matrix):
            return matrix
        matrix = restoreValues(matrix, oldMatrix)
    return matrix
def main():
    matrix = createTheSudokuBoard()
    matrix = recursivelySolveTheSudoku(matrix)
    displayTheSudokuBoard(matrix)
    printVerification(matrix)
