from moves import *
from fm_materials import *

class Cube:
    def __init__(self):
        self.edges = {
            'UF': 'UF',
            'FU': 'FU',
            'UR': 'UR',
            'RU': 'RU',
            'UL': 'UL',
            'LU': 'LU',
            'UB': 'UB',
            'BU': 'BU',
            'FL': 'FL',
            'LF': 'LF',
            'FD': 'FD',
            'DF': 'DF',
            'FR': 'FR',
            'RF': 'RF',
            'BL': 'BL',
            'LB': 'LB',
            'BD': 'BD',
            'DB': 'DB',
            'BR': 'BR',
            'RB': 'RB',
            'DL': 'DL',
            'LD': 'LD',
            'DR': 'DR',
            'RD': 'RD'
        }

        self.corners = {
            'UFR': 'UFR',
            'FUR': 'FUR',
            'RUF': 'RUF',
            'UFL': 'UFL',
            'FUL': 'FUL',
            'LUF': 'LUF',
            'UBL': 'UBL',
            'BUL': 'BUL',
            'LUB': 'LUB',
            'UBR': 'UBR',
            'RUB': 'RUB',
            'BUR': 'BUR',
            'DFL': 'DFL',
            'FDL': 'FDL',
            'LDF': 'LDF',
            'DFR': 'DFR',
            'FDR': 'FDR',
            'RDF': 'RDF',
            'DBL': 'DBL',
            'LDB': 'LDB',
            'BDL': 'BDL',
            'DBR': 'DBR',
            'RDB': 'RDB',
            'BDR': 'BDR'
        }
        self.edges_inverse = {
            'UF': 'UF',
            'FU': 'FU',
            'UR': 'UR',
            'RU': 'RU',
            'UL': 'UL',
            'LU': 'LU',
            'UB': 'UB',
            'BU': 'BU',
            'FL': 'FL',
            'LF': 'LF',
            'FD': 'FD',
            'DF': 'DF',
            'FR': 'FR',
            'RF': 'RF',
            'BL': 'BL',
            'LB': 'LB',
            'BD': 'BD',
            'DB': 'DB',
            'BR': 'BR',
            'RB': 'RB',
            'DL': 'DL',
            'LD': 'LD',
            'DR': 'DR',
            'RD': 'RD'
        }

        self.corners_inverse = {
            'UFR': 'UFR',
            'FUR': 'FUR',
            'RUF': 'RUF',
            'UFL': 'UFL',
            'FUL': 'FUL',
            'LUF': 'LUF',
            'UBL': 'UBL',
            'BUL': 'BUL',
            'LUB': 'LUB',
            'UBR': 'UBR',
            'RUB': 'RUB',
            'BUR': 'BUR',
            'DFL': 'DFL',
            'FDL': 'FDL',
            'LDF': 'LDF',
            'DFR': 'DFR',
            'FDR': 'FDR',
            'RDF': 'RDF',
            'DBL': 'DBL',
            'LDB': 'LDB',
            'BDL': 'BDL',
            'DBR': 'DBR',
            'RDB': 'RDB',
            'BDR': 'BDR'
        }

    def wide_move(self, single_move):
        """applies rotation and change wide move to not wide move"""
        move_cycle(wide_moves_rotations[single_move[0:2]], real_moves)
        single_move = wide_moves[single_move[0:2]]
        self.not_wide_move(single_move)

    def not_wide_move(self, single_move):
        """performs a move"""
        single_move = single_move[0:1]
        single_move = real_moves[single_move]
        if single_move in moves.keys():
            move_cycle(moves[single_move][0], self.edges)
            move_cycle(moves[single_move][1], self.edges)
            move_cycle([self.edges[x] for x in moves[move_inverse[single_move]][0]], self.edges_inverse)
            move_cycle([self.edges[x] for x in moves[move_inverse[single_move]][1]], self.edges_inverse)
            if single_move not in ['M', 'S', 'E']:
                move_cycle(moves[single_move][2], self.corners)
                move_cycle(moves[single_move][3], self.corners)
                move_cycle(moves[single_move][4], self.corners)
                move_cycle([self.corners[x] for x in moves[move_inverse[single_move]][2]], self.corners_inverse)
                move_cycle([self.corners[x] for x in moves[move_inverse[single_move]][3]], self.corners_inverse)
                move_cycle([self.corners[x] for x in moves[move_inverse[single_move]][4]], self.corners_inverse)

    def not_wide_move_inverse(self, single_move):
        """performs a move"""
        single_move = single_move[0:1]
        single_move = real_moves[single_move]
        if single_move in moves.keys():
            move_cycle(moves[single_move][0], self.edges_inverse)
            move_cycle(moves[single_move][1], self.edges_inverse)
            move_cycle([self.edges_inverse[x] for x in moves[move_inverse[single_move]][0]], self.edges)
            move_cycle([self.edges_inverse[x] for x in moves[move_inverse[single_move]][1]], self.edges)
            if single_move not in ['M', 'S', 'E']:
                move_cycle(moves[single_move][2], self.corners_inverse)
                move_cycle(moves[single_move][3], self.corners_inverse)
                move_cycle(moves[single_move][4], self.corners_inverse)
                move_cycle([self.corners_inverse[x] for x in moves[move_inverse[single_move]][2]], self.corners)
                move_cycle([self.corners_inverse[x] for x in moves[move_inverse[single_move]][3]], self.corners)
                move_cycle([self.corners_inverse[x] for x in moves[move_inverse[single_move]][4]], self.corners)

    def move_inverse(self, single_move):
        number = number_of_moves(single_move)
        while number > 0:
            number -= 1
            self.not_wide_move_inverse(single_move)

    def move(self, single_move):
        number = number_of_moves(single_move)
        while number > 0:
            number -= 1
            '''
            if is_wide(single_move):
                self.wide_move(single_move)
            else:
                self.not_wide_move(single_move)
            '''
            self.not_wide_move(single_move)

    def scramble(self, scramble):
        for move in scramble.split(' '):
            #print(move)
            self.move(move)

    def scramble_inverse(self, scramble):
        for move in scramble.split(' '):
            #print(move)
            self.move_inverse(move)

    def scramble_with_inverse(self, scramble):
        for move in reversed(scramble.split(' ')):
            #print(move)
            self.move(move_inverse[move])
if __name__ == "__main__":
    cube = Cube()
    cube.scramble("L' F' U2 F D2 L2 D2 B L2 U2 B U F D2 U2 F' L' D' F' U")
    print(cube.edges)
    print(cube.corners)
    cube2 = Cube()
    cube2.scramble_with_inverse("L' F' U2 F D2 L2 D2 B L2 U2 B U F D2 U2 F' L' D' F' U")
    print(cube2.edges)
