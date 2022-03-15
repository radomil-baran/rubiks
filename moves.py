real_moves = {
    'U': 'U',
    'D': 'D',
    'F': 'F',
    'B': 'B',
    'R': 'R',
    'L': 'L'
}
wide_moves_rotations = {
    'Rw': ['U', 'B', 'D', 'F'],
    'Uw': ['F', 'L', 'B', 'R'],
    'Fw': ['U', 'R', 'D', 'L'],
    'Dw': ['F', 'R', 'B', 'L'],
    'Lw': ['U', 'F', 'D', 'B'],
    'Bw': ['U', 'L', 'D', 'R']
}
wide_moves = {
    'Rw': 'L',
    'Uw': 'D',
    'Fw': 'B',
    'Dw': 'U',
    'Lw': 'R',
    'Bw': 'F'
}
moves = {
    'U': [['UF', 'UL', 'UB', 'UR'], ['FU', 'LU', 'BU', 'RU'],
          ['UFR', 'UFL', 'UBL', 'UBR'], ['FUR', 'LUF', 'BUL', 'RUB'], ['RUF', 'FUL', 'LUB', 'BUR']],
    'D': [['DF', 'DR', 'DB', 'DL'], ['FD', 'RD', 'BD', 'LD'],
          ['DFR', 'DBR', 'DBL', 'DFL'], ['FDR', 'RDB', 'BDL', 'LDF'], ['RDF', 'BDR', 'LDB', 'FDL']],
    'R': [['UR', 'BR', 'DR', 'FR'], ['RU', 'RB', 'RD', 'RF'],
          ['UFR', 'BUR', 'DBR', 'FDR'], ['FUR', 'UBR', 'BDR', 'DFR'], ['RUF', 'RUB', 'RDB', 'RDF']],
    'L': [['UL', 'FL', 'DL', 'BL'], ['LU', 'LF', 'LD', 'LB'],
          ['UFL', 'FDL', 'DBL', 'BUL'], ['FUL', 'DFL', 'BDL', 'UBL'], ['LUF', 'LDF', 'LDB', 'LUB']],
    'F': [['UF', 'RF', 'DF', 'LF'], ['FU', 'FR', 'FD', 'FL'],
          ['UFR', 'RDF', 'DFL', 'LUF'], ['FUR', 'FDR', 'FDL', 'FUL'], ['RUF', 'DFR', 'LDF', 'UFL']],
    'B': [['UB', 'LB', 'DB', 'RB'], ['BU', 'BL', 'BD', 'BR'],
          ['UBR', 'LUB', 'DBL', 'RDB'], ['BUR', 'BUL', 'BDL', 'BDR'], ['RUB', 'UBL', 'LDB', 'DBR']],
    "U'": [['UF', 'UR', 'UB', 'UL'], ['FU', 'RU', 'BU', 'LU'],
          ['UFR', 'UBR', 'UBL', 'UFL'], ['FUR', 'RUB', 'BUL', 'LUF'], ['RUF', 'BUR', 'LUB', 'FUL']],
    "D'": [['DF', 'DL', 'DB', 'DR'], ['FD', 'LD', 'BD', 'RD'],
          ['DFR', 'DFL', 'DBL', 'DBR'], ['FDR', 'LDF', 'BDL', 'RDB'], ['RDF', 'FDL', 'LDB', 'BDR']],
    "R'": [['UR', 'FR', 'DR', 'BR'], ['RU', 'RF', 'RD', 'RB'],
          ['UFR', 'FDR', 'DBR', 'BUR'], ['FUR', 'DFR', 'BDR', 'UBR'], ['RUF', 'RDF', 'RDB', 'RUB']],
    "L'": [['UL', 'BL', 'DL', 'FL'], ['LU', 'LB', 'LD', 'LF'],
          ['UFL', 'BUL', 'DBL', 'FDL'], ['FUL', 'UBL', 'BDL', 'DFL'], ['LUF', 'LUB', 'LDB', 'LDF']],
    "F'": [['UF', 'LF', 'DF', 'RF'], ['FU', 'FL', 'FD', 'FR'],
          ['UFR', 'LUF', 'DFL', 'RDF'], ['FUR', 'FUL', 'FDL', 'FDR'], ['RUF', 'UFL', 'LDF', 'DFR']],
    "B'": [['UB', 'RB', 'DB', 'LB'], ['BU', 'BR', 'BD', 'BL'],
          ['UBR', 'RDB', 'DBL', 'LUB'], ['BUR', 'BDR', 'BDL', 'BUL'], ['RUB', 'DBR', 'LDB', 'UBL']],
    'M': [['UF', 'FD', 'DB', 'BU'], ['FU', 'DF', 'BD', 'UB']],
    'S': [['UR', 'RD', 'DL', 'LU'], ['RU', 'DR', 'LD', 'UL']],
    'E': [['FL', 'RF', 'BR', 'LB'], ['LF', 'FR', 'RB', 'BL']]
}


def move_cycle(cycle, elements):
    """perform cycle on elements (should be done better)"""
    temp = elements[cycle[-1]]
    for i in range(3, 0, -1):
        # print(i)
        elements[cycle[i]] = elements[cycle[i - 1]]
    elements[cycle[0]] = temp


def number_of_moves(single_move):
    """counts the number of moves in single_move"""
    number = 0
    if single_move[-1] in ['2', "\'"]:
        if single_move[-1] == "\'":
            number = 3
        if single_move[-1] == '2':
            number = 2
    else:
        number = 1
    return number


def is_wide(single_move):
    return 'w' in single_move
