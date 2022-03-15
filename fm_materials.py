from cube import *

oriented_edges = {
    'FB': ['UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR'],
    'RL': ['UF', 'UR', 'UL', 'UB', 'LF', 'RF', 'LB', 'RB', 'DF', 'DL', 'DB', 'DR'],
    'UD': ['LF', 'RF', 'LB', 'RB', 'LU', 'RU', 'LD', 'RD', 'UF', 'UB', 'DF', 'DB']
}

FB_oriented = ['UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR']
RL_oriented = ['UR', 'UB', 'UF', 'UL', 'RF', 'RB', 'LF', 'LB', 'DR', 'DF', 'DL', 'DB']
UD_oriented = ['LU', 'LB', 'LF', 'LD', 'UF', 'UB', 'DF', 'DB', 'RU', 'RF', 'RD', 'RB']

UD_edges_stickers = ['UF', 'UR', 'UB', 'UL', 'DF', 'DR', 'DL', 'DB']
UD_corners_stickers = ['UFR', 'UFL', 'UBL', 'UBR', 'DFR', 'DFL', 'DBL', 'DBR']
RL_edges_stickers = ['LF', 'LU', 'LB', 'LD', 'RF', 'RU', 'RD', 'RB']
RL_corners_stickers = ['LUF', 'LDF', 'LDB', 'LUB', 'RUF', 'RDF', 'RDB', 'RUB']
corners_stickers = ['UFR', 'FUR', 'RUF', 'UFL', 'FUL', 'LUF', 'UBL', 'BUL', 'LUB', 'UBR', 'RUB', 'BUR', 'DFR', 'FDR',
                    'RDF', 'DFL',
                    'FDL', 'LDF', 'DBL', 'LDB', 'BDL', 'DBR', 'RDB', 'BDR']

corners_rotation_numbers = {
    'UFR': 0,
    'FUR': 1,
    'RUF': 2,
    'UFL': 0,
    'FUL': 2,
    'LUF': 1,
    'UBL': 0,
    'BUL': 1,
    'LUB': 2,
    'UBR': 0,
    'RUB': 1,
    'BUR': 2,
    'DFL': 0,
    'FDL': 1,
    'LDF': 2,
    'DFR': 0,
    'FDR': 2,
    'RDF': 1,
    'DBL': 0,
    'LDB': 1,
    'BDL': 2,
    'DBR': 0,
    'RDB': 2,
    'BDR': 1
}

cube_stickers = ['UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR', 'FU', 'RU', 'LU', 'BU', 'FD',
                 'RD', 'BD', 'LD', 'RF', 'LF', 'RB', 'LB']

fm_moves = ['R', 'R2', "R'", 'U', 'U2', "U'", 'F', 'F2', "F'", 'L', 'L2', "L'", 'D', 'D2', "D'", 'B', 'B2', "B'"]

fm_moves_after_eo = ['R2', 'U', 'U2', "U'", 'F2', 'L2', 'D', 'D2', "D'", 'B2']

fm_basic_moves = ['R', 'U', 'F', 'D', 'B', 'L']


def inverse(moves):
    res = ""
    for m in reversed(moves.split(' ')):
        res += move_inverse[m]
        res += ' '
    return res


move_inverse = {
    'R': "R'",
    'R2': 'R2',
    "R'": 'R',
    'U': "U'",
    'U2': 'U2',
    "U'": 'U',
    'F': "F'",
    'F2': 'F2',
    "F'": 'F',
    'L': "L'",
    'L2': 'L2',
    "L'": 'L',
    'D': "D'",
    'D2': 'D2',
    "D'": 'D',
    'B': "B'",
    'B2': 'B2',
    "B'": 'B'
}

forbidden = {
    '': [''],
    'R': ["R'", 'R', 'R2'],
    'R2': ["R'", 'R', 'R2'],
    "R'": ["R'", 'R', 'R2'],
    'U': ["U'", 'U', 'U2'],
    'U2': ["U'", 'U', 'U2'],
    "U'": ["U'", 'U', 'U2'],
    'F': ["F'", 'F', 'F2'],
    'F2': ["F'", 'F', 'F2'],
    "F'": ["F'", 'F', 'F2'],
    'L': ["L'", 'L', 'L2'],
    'L2': ["L'", 'L', 'L2'],
    "L'": ["L'", 'L', 'L2'],
    'D': ["D'", 'D', 'D2'],
    'D2': ["D'", 'D', 'D2'],
    "D'": ["D'", 'D', 'D2'],
    'B': ['B', 'B2', "B'"],
    'B2': ['B', 'B2', "B'"],
    "B'": ['B', 'B2', "B'"]
}

forbidden_second = {
    '': [''],
    'R': ["R'", 'R', 'R2', "L'", 'L', 'L2'],
    'R2': ["R'", 'R', 'R2', "L'", 'L', 'L2'],
    "R'": ["R'", 'R', 'R2', "L'", 'L', 'L2'],
    'U': ["U'", 'U', 'U2', "D'", 'D', 'D2'],
    'U2': ["U'", 'U', 'U2', "D'", 'D', 'D2'],
    "U'": ["U'", 'U', 'U2', "D'", 'D', 'D2'],
    'F': ["F'", 'F', 'F2', 'B', 'B2', "B'"],
    'F2': ["F'", 'F', 'F2', 'B', 'B2', "B'"],
    "F'": ["F'", 'F', 'F2', 'B', 'B2', "B'"],
    'L': ["L'", 'L', 'L2', "R'", 'R', 'R2'],
    'L2': ["L'", 'L', 'L2', "R'", 'R', 'R2'],
    "L'": ["L'", 'L', 'L2', "R'", 'R', 'R2'],
    'D': ["D'", 'D', 'D2', "U'", 'U', 'U2'],
    'D2': ["D'", 'D', 'D2', "U'", 'U', 'U2'],
    "D'": ["D'", 'D', 'D2', "U'", 'U', 'U2'],
    'B': ['B', 'B2', "B'", "F'", 'F', 'F2'],
    'B2': ['B', 'B2', "B'", "F'", 'F', 'F2'],
    "B'": ['B', 'B2', "B'", "F'", 'F', 'F2']
}

axis_group = {
    'FB': ['F', 'B'],
    'RL': ['R', 'L'],
    'UD': ['U', 'D']
}


def same_group(x, y):
    for a in ['FB', 'RL', 'UD']:
        if x in axis_group[a] and y in axis_group[a]:
            return True
    return False


def ile_nonoriented_FB(cube):
    s = 0
    for e in FB_oriented:
        if cube.edges[e] not in FB_oriented:
            s = s + 1
    return s


def ile_nonoriented_RL(cube):
    s = 0
    for e in RL_oriented:
        if cube.edges[e] not in RL_oriented:
            s = s + 1
    return s


def ile_nonoriented_UD(cube):
    s = 0
    for e in UD_oriented:
        if cube.edges[e] not in UD_oriented:
            s = s + 1
    return s


def ile_nonoriented(cube):
    return [ile_nonoriented_FB(cube), ile_nonoriented_RL(cube), ile_nonoriented_UD(cube)]


FB_edges = ['UL', 'UR', 'DL', 'DR']
RL_edges = ['UF', 'UB', 'DF', 'DB']
UD_edges = ['RF', 'LF', 'RB', 'LB']


def dwa_ruchable_FB(cube):
    x = ile_nonoriented_FB(cube)
    if x not in [0, 4, 8]:
        return False
    if x == 0:
        return True
    if x == 8:
        if cube.edges['UL'] in FB_oriented and cube.edges['UR'] in FB_oriented and cube.edges['DL'] in FB_oriented and \
                cube.edges['DR'] in FB_oriented:
            return True
        else:
            for e in FB_edges:
                if e not in [cube.edges[f] for f in FB_oriented]:
                    return False
            return True
    if x == 4:
        l = not_F(cube) + not_B(cube)
        if 3 not in l and 4 not in l:
            return False
        return True
    return True


def dwa_ruchable_RL(cube):
    x = ile_nonoriented_RL(cube)
    if x not in [0, 4, 8]:
        return False
    if x == 0:
        return True
    if x == 8:
        if cube.edges['UF'] in RL_oriented and cube.edges['UB'] in RL_oriented and cube.edges['DF'] in RL_oriented and \
                cube.edges['DB'] in RL_oriented:
            return True
        else:
            for e in RL_edges:
                if e not in [cube.edges[f] for f in RL_oriented]:
                    return False
            return True
    if x == 4:
        l = not_R(cube) + not_L(cube)
        if 3 not in l and 4 not in l:
            return False
        return True
    return True


def dwa_ruchable_UD(cube):
    x = ile_nonoriented_UD(cube)
    if x not in [0, 4, 8]:
        return False
    if x == 0:
        return True
    if x == 8:
        if cube.edges['LF'] in UD_oriented and cube.edges['RF'] in UD_oriented and cube.edges['LB'] in UD_oriented and \
                cube.edges['RB'] in UD_oriented:
            return True
        else:
            for e in UD_edges:
                if e not in [cube.edges[f] for f in UD_oriented]:
                    return False
            return True
    if x == 4:
        l = not_U(cube) + not_D(cube)
        if 3 not in l and 4 not in l:
            return False
        return True
    return True


def dwa_ruchable(cube):
    return dwa_ruchable_FB(cube) or dwa_ruchable_RL(cube) or dwa_ruchable_UD(cube)


F_sciana = ['UF', 'FL', 'FR', 'DF']
B_sciana = ['UB', 'BL', 'BR', 'DB']
R_sciana = ['UR', 'RF', 'RB', 'DR']
L_sciana = ['UL', 'LF', 'LB', 'DL']
U_sciana = ['LU', 'UF', 'RU', 'UB']
D_sciana = ['LD', 'RD', 'DF', 'DB']


def not_F(cube):
    r = 0
    s = 0
    for e in F_sciana:
        if cube.edges[e] not in FB_oriented:
            r = r + 1
    for e in F_sciana:
        if e not in [cube.edges[f] for f in FB_oriented]:
            s = s + 1
    return [r, s]


def not_B(cube):
    r = 0
    s = 0
    for e in B_sciana:
        if cube.edges[e] not in FB_oriented:
            r = r + 1
    for e in B_sciana:
        if e not in [cube.edges[f] for f in FB_oriented]:
            s = s + 1
    return [r, s]


def not_R(cube):
    r = 0
    s = 0
    for e in R_sciana:
        if cube.edges[e] not in RL_oriented:
            r = r + 1
    for e in R_sciana:
        if e not in [cube.edges[f] for f in RL_oriented]:
            s = s + 1
    return [r, s]


def not_L(cube):
    r = 0
    s = 0
    for e in L_sciana:
        if cube.edges[e] not in RL_oriented:
            r = r + 1
    for e in L_sciana:
        if e not in [cube.edges[f] for f in RL_oriented]:
            s = s + 1
    return [r, s]


def not_U(cube):
    r = 0
    s = 0
    for e in U_sciana:
        if cube.edges[e] not in UD_oriented:
            r = r + 1
    for e in U_sciana:
        if e not in [cube.edges[f] for f in UD_oriented]:
            s = s + 1
    return [r, s]


def not_D(cube):
    r = 0
    s = 0
    for e in D_sciana:
        if cube.edges[e] not in UD_oriented:
            r = r + 1
    for e in D_sciana:
        if e not in [cube.edges[f] for f in UD_oriented]:
            s = s + 1
    return [r, s]


def not_all(cube):
    return not_F(cube) + not_B(cube) + not_R(cube) + not_L(cube) + not_U(cube) + not_D(cube)


def mieszaj(cube, normal, inwersja, scramble):
    for r in inwersja:
        cube.move(move_inverse[r])
    cube.scramble(scramble)
    for r in normal:
        cube.move(r)


def is_eo_axis(axis, cube):
    for sticker in cube_stickers:
        if bool(sticker in oriented_edges[axis]) != bool(cube.edges[sticker] in oriented_edges[axis]):
            return False
    return True


def is_done_eo(cube):
    return is_eo_axis('FB', cube) or is_eo_axis('RL', cube) or is_eo_axis('UD', cube)


def dr_orientation_F_UD(cube):
    # kolejność: 'UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR'
    # kolejność: 'UFR', 'UFL', 'UBL', 'UBR', 'DFR', 'DFL', 'DBL', 'DBR'
    r = ""
    for m in FB_oriented:
        if cube.edges[m] in UD_edges_stickers:
            r = r + "0"
        else:
            r = r + "1"
    for m in corners_stickers:
        if cube.corners[m] in UD_corners_stickers:
            r = r + str(corners_rotation_numbers[m])
    return r


def count_orientation_F_UD(cube):
    e = 0
    c = 0
    for m in ['FL', 'FR', 'BL', 'BR']:
        if cube.edges[m] in UD_edges_stickers:
            e = e + 1
    for m in UD_corners_stickers:
        if cube.corners[m] not in UD_corners_stickers:
            c = c + 1

    return c, e


def count_orientation_F_RL(cube):
    e = 0
    c = 0
    for m in ['FD', 'FU', 'BD', 'BU']:
        if cube.edges[m] in RL_edges_stickers:
            e = e + 1
    for m in RL_corners_stickers:
        if cube.corners[m] not in RL_corners_stickers:
            c = c + 1

    return c, e


'''
def count_orientation_F_UD(cube):
    e = 0
    c = 0
    for m in ['FL', 'FR', 'BL', 'BR']:
        if cube.edges[m] in UD_edges_stickers:
            e = e + 1
    for m in UD_corners_stickers:
        if cube.corners[m] not in UD_corners_stickers:
            c = c + 1

    return c, e


def count_orientation_F_UD(cube):
    e = 0
    c = 0
    for m in ['FL', 'FR', 'BL', 'BR']:
        if cube.edges[m] in UD_edges_stickers:
            e = e + 1
    for m in UD_corners_stickers:
        if cube.corners[m] not in UD_corners_stickers:
            c = c + 1

    return c, e


def count_orientation_F_UD(cube):
    e = 0
    c = 0
    for m in ['FL', 'FR', 'BL', 'BR']:
        if cube.edges[m] in UD_edges_stickers:
            e = e + 1
    for m in UD_corners_stickers:
        if cube.corners[m] not in UD_corners_stickers:
            c = c + 1

    return c, e


def count_orientation_F_UD(cube):
    e = 0
    c = 0
    for m in ['FL', 'FR', 'BL', 'BR']:
        if cube.edges[m] in UD_edges_stickers:
            e = e + 1
    for m in UD_corners_stickers:
        if cube.corners[m] not in UD_corners_stickers:
            c = c + 1

    return c, e
'''


def orientation_F(cube):
    # kolejność: 'UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR'
    r = ""
    for m in FB_oriented:
        if cube.edges[m] in FB_oriented:
            r = r + "O"
        else:
            r = r + "U"
    return r


def orientation_R(cube):
    # kolejność: 'UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR'
    r = ""
    for m in RL_oriented:
        if cube.edges[m] in RL_oriented:
            r = r + "O"
        else:
            r = r + "U"
    return r


def orientation_U(cube):
    # kolejność: 'UF', 'UR', 'UL', 'UB', 'FL', 'FR', 'BL', 'BR', 'DF', 'DL', 'DB', 'DR'
    r = ""
    for m in UD_oriented:
        if cube.edges[m] in UD_oriented:
            r = r + "O"
        else:
            r = r + "U"
    return r


def FB_to_RL(move):
    x = move[0]
    if x == "F":
        x = "R"
    elif x == "R":
        x = "B"
    elif x == "B":
        x = "L"
    elif x == "L":
        x = "F"
    return x + move[1:]


def FB_to_UD(move):
    x = move[0]
    if x == "F":
        x = "U"
    elif x == "R":
        x = "B"
    elif x == "B":
        x = "D"
    elif x == "L":
        x = "F"
    elif x == "D":
        x = "R"
    elif x == "U":
        x = "L"
    return x + move[1:]


# prints eo in dict format
def eo_print(eo):
    res = ""
    if eo['i']:
        res += '('
        for i in range(len(eo['i'])):
            res += f"{eo['i'][i]}"
            if i != len(eo['i']) - 1:
                res += " "
        res += ') '
    if eo['n']:
        for i in range(len(eo['n'])):
            res += f"{eo['n'][i]}"
            if i != len(eo['n']) - 1:
                res += " "
    return res
