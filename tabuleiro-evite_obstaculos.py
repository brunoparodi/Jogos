# Criado por Bruno Parodi em 24/10/2018
# última revisão em 29/10/2018
# report bugs to bruno@parodi.com.br

# crie um tabuleiro, começe no canto superior esquerdo e chegue no canto inferior direito
# você só consegue se mover para baixo ou para a direita

from random import uniform as randomuniform
from numpy import where as numpywhere
from numpy import array as numpyarray
from os import system as clear

class Grid(object):

    def size_row(self):
        max_rows = input('Informe o número de linhas, umas 15 linhas é bom: ')
        c = 0
        while c < 1:
            try:
                int(max_rows)
                max_rows = int(max_rows)
                c += 1
                if max_rows <= 4:
                    c = 0
                    max_rows = 'a'
            except ValueError:
                print('Informe um número inteiro positivo maior que 04')
                max_rows = input('Informe o número de linhas, umas 15 linhas é bom: ')
        return max_rows

    def size_col(self):
        max_cols = input('Informe o número de colunas, umas 15 colulas é bom: ')
        d = 0
        while d < 1:
            try:
                int(max_cols)
                max_cols = int(max_cols)
                d += 1
                if max_cols <= 4:
                    d = 0
                    max_cols = 'a'
            except ValueError:
                print('Informe um número inteiro positivo maior que 04')
                max_cols = input('Informe o número de colunas, umas 15 linhas é bom: ')
        return max_cols
    # gera uma matriz conforme indicacao do usuario
    def generate_matrix(self):
        max_rows = self.size_row()
        max_cols = self.size_col()
        matrix = []
        for rows in range(max_rows):
            new_row = []
            for cols in range(max_cols):
                new_row.append('o')
            matrix.append(new_row)
        clear('cls')
        return matrix
    # gera barreiras na matriz
    def final_matrix(self):
        matrix = self.generate_matrix()
        matrix_rows = int(len(matrix)-1)
        matrix_cols = int(len(matrix[0])-1)
        total_cells = len(matrix) * len(matrix[0])
        max_invalid_cells = total_cells // 4
        invalid_cells = []
        while len(invalid_cells) <= max_invalid_cells -1:
            invalid = [int(randomuniform(0,matrix_rows)),int(randomuniform(0,matrix_cols))]
            #remove repeated cells
            for cel in invalid_cells:
                if cel == invalid:
                    invalid_cells.remove(cel)
            if invalid == [0,0] or invalid == [matrix_cols,matrix_rows]:
                pass
            else:
                invalid_cells.append(invalid)
        for item in invalid_cells:
            matrix[item[0]][item[1]] = 'x'
        if matrix[0][1] == 'x' and matrix[1][0] == 'x':
            input('Oooops!!! Temos que refazer nosso tabuleiro!!\nAperte uma tecla para continuar')
            main()
        else:
            return matrix

    # imprime a matriz com as barreiras
    def print_matrix(self, matrix):
        matrix_rows = int(len(matrix))
        matrix_cols = int(len(matrix[0]))
        print('  ',end='')
        for cols in range(matrix_cols):
            print(cols,end=' ')
        print('', end='\n')
        for rows in range(matrix_rows):
            print(rows, end=' ')
            for c in range(matrix_cols):
                print(matrix[rows][c],end=' ')
            print('')

    #recebe x e y de onde esta o robo | get robot coord
    def move_right(self,matrix):
        m = numpyarray(matrix)
        indices = numpywhere(m == '#')
        indice_row = int(indices[0])
        indice_col = int(indices[-1])
        move_right = indice_col + 1

        if int(move_right) >= int(len(matrix[0])):
            move_right = len(matrix[0]) - 1
            print('Você não pode andar para a direita\n')
        if matrix[indice_row][move_right] != 'x':
            matrix[indice_row][indice_col] = 'o'
            matrix[indice_row][move_right] = '#'
            return matrix
        else:
            print('Você não pode andar para a direita\n')
            return False

    def move_down(self,matrix):
        #matrix = self.play()
        #recebe x e y de onde esta o robo | get robot coord
        m = numpyarray(matrix)
        indices = numpywhere(m == '#')
        indice_row = int(indices[0])
        indice_col = int(indices[-1])

        move_down = indice_row + 1

        if int(move_down) >= int(len(matrix)):
            move_down = len(matrix) - 1
            print('Você não pode andar para a baixo\n')
        if matrix[move_down][indice_col] != 'x':
            matrix[indice_row][indice_col] = 'o'
            matrix[move_down][indice_col] = '#'
            return matrix
        else:
            print('Você não pode andar para baixo\n')
            return False

    def play(self):
        clear('cls')
        matrix = self.final_matrix()
        matrix[0][0] = '#'
        first_play = True

        while matrix[-1][-1] != '#':

            if first_play == True:
                print('REGRAS: Você só pode mover o robo (#) para baixo (S) ou para direita (D)')
                print('        Você NÃO pode mover o robo para as casas marcadas com `x´')
                print('        O objetivo é mover o robo até o canto inferior direito\n')
                self.print_matrix(matrix)
                first_play = False
            movement = input('Informe uma jogada. D para direita ou S para baixo. Aperte ENTER para sair. ')
            clear('cls')

            if movement == 'd' or movement == 'D':
                self.move_right(matrix)
                first_play = False
            elif movement == 's' or movement == 'S':
                self.move_down(matrix)
                first_play = False
            elif movement == '':
                return
            self.print_matrix(matrix)
            if self.possible(matrix) == True:
                break
        if self.win(matrix) == True:
            print('\n********************** PARABÉNS VOCÊ GANHOU!!! **********************\n')
        self.new()
        return

    def new(self):
        a = input('Quer começar de novo? S para SIM ou qualquer outra para NÃO. ')
        if a == 'S' or a == 's':
            clear('cls')
            self.play()
        else:
            return

    def possible(self, matrix):
        m = numpyarray(matrix)
        indices = numpywhere(m == '#')
        indice_row = int(indices[0])
        indice_col = int(indices[-1])
        move_right = indice_col + 1
        move_down = indice_row + 1
        if int(move_right) >= int(len(matrix[0])):
            move_right = len(matrix[0]) - 1
        if matrix[indice_row][move_right] == 'x' and matrix[move_down][indice_col] == 'x':
            print('\n!!!Fim das jogadas possíveis!!!')
            print('   ######  GAME OVER   #####   ')
            print('')
            return True
        else:
            return False

    def win(self, matrix):
        if matrix[-1][-1] == '#':
            return True
        else:
            return False

def main():
    jogo = Grid()
    v = jogo.play()

main()



