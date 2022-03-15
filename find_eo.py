from cube import *
from fm_materials import *


def find_eo(scramble):
    eos = []
    eos_dict = []

    # s - number of eos
    s = 0
    '''5 moves eo on normal'''
    c = Cube()
    c.scramble(scramble)
    or_F = orientation_F(c)
    or_R = orientation_R(c)
    or_U = orientation_U(c)
    with open("D:\\INFORMATYKA\\python\\rubiks\\eos_sub3_with_orientation_FB.txt", "r+") as f:
        for line in f:
            if line.rstrip().split(" ")[-1] == or_F:
                if line.rsplit(' ', 1)[0] not in eos:
                    eos.append(line.rsplit(' ', 1)[0])
                    eos_dict.append({'n': line.rsplit(' ', 1)[0].split(), 'i': []})
                    # print(line.rsplit(' ', 1)[0].split())
                    s = s + 1
    with open("eos_sub5_with_orientation_RL.txt", "r+") as f:
        for line in f:
            if line.rstrip().split(" ")[-1] == or_R:
                if line.rsplit(' ', 1)[0] not in eos:
                    eos.append(line.rsplit(' ', 1)[0])
                    eos_dict.append({'n': line.rsplit(' ', 1)[0].split(), 'i': []})
                    s = s + 1
    with open("eos_sub5_with_orientation_UD.txt", "r+") as f:
        for line in f:
            if line.rstrip().split(" ")[-1] == or_U:
                if line.rsplit(' ', 1)[0] not in eos:
                    eos.append(line.rsplit(' ', 1)[0])
                    eos_dict.append({'n': line.rsplit(' ', 1)[0].split(), 'i': []})
                    s = s + 1
    '''5 moves eo on inverse'''
    c = Cube()
    c.scramble_with_inverse(scramble)
    or_F = orientation_F(c)
    or_R = orientation_R(c)
    or_U = orientation_U(c)
    with open("eos_sub5_with_orientation_FB.txt", "r+") as f:
        for line in f:
            if line.rstrip().split(" ")[-1] == or_F:
                if f"({line.rsplit(' ', 1)[0]})" not in eos:
                    eos.append(f"({line.rsplit(' ', 1)[0]})")
                    eos_dict.append({'n': [], 'i': line.rsplit(' ', 1)[0].split()})
                    s = s + 1
    with open("eos_sub5_with_orientation_RL.txt", "r+") as f:
        for line in f:
            if line.rstrip().split(" ")[-1] == or_R:
                if f"({line.rsplit(' ', 1)[0]})" not in eos:
                    eos.append(f"({line.rsplit(' ', 1)[0]})")
                    eos_dict.append({'n': [], 'i': line.rsplit(' ', 1)[0].split()})
                    s = s + 1
    with open("eos_sub5_with_orientation_UD.txt", "r+") as f:
        for line in f:
            if line.rstrip().split(" ")[-1] == or_U:
                if f"({line.rsplit(' ', 1)[0]})" not in eos:
                    eos.append(f"({line.rsplit(' ', 1)[0]})")
                    eos_dict.append({'n': [], 'i': line.rsplit(' ', 1)[0].split()})
                    s = s + 1

    for m1 in fm_moves:
        for m2 in fm_basic_moves:
            if m2 not in forbidden_second[m1] or (m1 + m2 in ["FB", "BF", "RL", "LR", "UD", "DU"]):
                c = Cube()
                c.move(move_inverse[m2])
                c.move(move_inverse[m1])
                c.scramble(scramble)
                if m2 in ['F', 'B']:
                    or_F = orientation_F(c)
                    with open("eos_sub3_with_orientation_FB.txt", "r+") as f:
                        for line in f:
                            if line.rstrip().split(" ")[-1] == or_F:
                                # print(f"({m1} {m2}) {line.rsplit(' ', 1)[0]}")
                                if f"({m1} {m2}) {line.rsplit(' ', 1)[0]}" not in eos:
                                    eos.append(f"({m1} {m2}) {line.rsplit(' ', 1)[0]}")
                                    eos_dict.append({'n': line.rsplit(' ', 1)[0].split(), 'i': [m1, m2]})
                                    s = s + 1
                if m2 in ['R', 'L']:
                    or_R = orientation_R(c)
                    with open("eos_sub3_with_orientation_RL.txt", "r+") as f:
                        for line in f:
                            if line.rstrip().split(" ")[-1] == or_R:
                                # print(f"({m1} {m2}) {line.rsplit(' ', 1)[0]}")
                                if f"({m1} {m2}) {line.rsplit(' ', 1)[0]}" not in eos:
                                    eos.append(f"({m1} {m2}) {line.rsplit(' ', 1)[0]}")
                                    eos_dict.append({'n': line.rsplit(' ', 1)[0].split(), 'i': [m1, m2]})
                                    s = s + 1
                if m2 in ['U', 'D']:
                    or_U = orientation_U(c)
                    with open("eos_sub3_with_orientation_UD.txt", "r+") as f:
                        for line in f:
                            if line.rstrip().split(" ")[-1] == or_U:
                                # print(f"({m1} {m2}) {line.rsplit(' ', 1)[0]}")
                                if f"({m1} {m2}) {line.rsplit(' ', 1)[0]}" not in eos:
                                    eos.append(f"({m1} {m2}) {line.rsplit(' ', 1)[0]}")
                                    eos_dict.append({'n': line.rsplit(' ', 1)[0].split(), 'i': [m1, m2]})
                                    s = s + 1

    for m1 in fm_moves:
        for m2 in fm_basic_moves:
            if m2 not in forbidden_second[m1] or (m1 + m2 in ["FB", "BF", "RL", "LR", "UD", "DU"]):
                c = Cube()
                c.move(move_inverse[m2])
                c.move(move_inverse[m1])
                c.scramble_with_inverse(scramble)
                if m2 in ['F', 'B']:
                    or_F = orientation_F(c)
                    with open("eos_sub3_with_orientation_FB.txt", "r+") as f:
                        for line in f:
                            if line.rstrip().split(" ")[-1] == or_F:
                                # print(f"({line.rsplit(' ', 1)[0]}) {m1} {m2}")
                                if f"({line.rsplit(' ', 1)[0]}) {m1} {m2}" not in eos:
                                    eos.append(f"({line.rsplit(' ', 1)[0]}) {m1} {m2}")
                                    eos_dict.append({'n': [m1, m2], 'i': line.rsplit(' ', 1)[0].split()})
                                    s = s + 1
                if m2 in ['R', 'L']:
                    or_R = orientation_R(c)
                    with open("eos_sub3_with_orientation_RL.txt", "r+") as f:
                        for line in f:
                            if line.rstrip().split(" ")[-1] == or_R:
                                # print(f"({line.rsplit(' ', 1)[0]}) {m1} {m2}")
                                if f"({line.rsplit(' ', 1)[0]}) {m1} {m2}" not in eos:
                                    eos.append(f"({line.rsplit(' ', 1)[0]}) {m1} {m2}")
                                    eos_dict.append({'n': [m1, m2], 'i': line.rsplit(' ', 1)[0].split()})
                                    s = s + 1
                if m2 in ['U', 'D']:
                    or_U = orientation_U(c)
                    with open("eos_sub3_with_orientation_UD.txt", "r+") as f:
                        for line in f:
                            if line.rstrip().split(" ")[-1] == or_U:
                                # print(f"({line.rsplit(' ', 1)[0]}) {m1} {m2}")
                                if f"({line.rsplit(' ', 1)[0]}) {m1} {m2}" not in eos:
                                    eos.append(f"({line.rsplit(' ', 1)[0]}) {m1} {m2}")
                                    eos_dict.append({'n': [m1, m2], 'i': line.rsplit(' ', 1)[0].split()})
                                    s = s + 1

    for m1 in fm_moves:
        for m2 in fm_basic_moves:
            c = Cube()
            c.move(move_inverse[m2])
            c.scramble(scramble)
            c.move(m1)
            if is_done_eo(c) and m1 in fm_basic_moves and m2 in forbidden[m1]:
                # print(f"({m2}) {m1}")
                if f"({m2}) {m1}" not in eos:
                    eos.append(f"({m2}) {m1}")
                    eos_dict.append({'n': [m1], 'i': [m2]})
                    s = s + 1
            if m2 in ['F', 'B']:
                or_F = orientation_F(c)
                with open("eos_sub3_with_orientation_FB.txt", "r+") as f:
                    for line in f:
                        if line.rstrip().split(" ")[-1] == or_F and line.rstrip().split(" ")[0] not in forbidden[m1] \
                                and (len(line.rstrip().split(" ")) < 3 or not (
                                line.rstrip().split(" ")[0] in forbidden_second[m1]
                                and line.rstrip().split(" ")[1] in forbidden[m1])):
                            # print(f"({m2}) {m1} {line.rsplit(' ', 1)[0]}")
                            if f"({m2}) {m1} {line.rsplit(' ', 1)[0]}" not in eos:
                                eos.append(f"({m2}) {m1} {line.rsplit(' ', 1)[0]}")
                                eos_dict.append({'n': [m1] + line.rsplit(' ', 1)[0].split(), 'i': [m2]})
                                s = s + 1
            if m2 in ['R', 'L']:
                or_R = orientation_R(c)
                with open("eos_sub3_with_orientation_RL.txt", "r+") as f:
                    for line in f:
                        if line.rstrip().split(" ")[-1] == or_R and line.rstrip().split(" ")[0] not in forbidden[m1] \
                                and (len(line.rstrip().split(" ")) < 3 or not (
                                line.rstrip().split(" ")[0] in forbidden_second[m1]
                                and line.rstrip().split(" ")[1] in forbidden[m1])):
                            # print(f"({m2}) {m1} {line.rsplit(' ', 1)[0]}")
                            if f"({m2}) {m1} {line.rsplit(' ', 1)[0]}" not in eos:
                                eos.append(f"({m2}) {m1} {line.rsplit(' ', 1)[0]}")
                                eos_dict.append({'n': [m1] + line.rsplit(' ', 1)[0].split(), 'i': [m2]})
                                s = s + 1
            if m2 in ['U', 'D']:
                or_U = orientation_U(c)
                with open("eos_sub3_with_orientation_UD.txt", "r+") as f:
                    for line in f:
                        if line.rstrip().split(" ")[-1] == or_U and line.rstrip().split(" ")[0] not in forbidden[m1] \
                                and (len(line.rstrip().split(" ")) < 3 or not (
                                line.rstrip().split(" ")[0] in forbidden_second[m1]
                                and line.rstrip().split(" ")[1] in forbidden[m1])):
                            # print(f"({m2}) {m1} {line.rsplit(' ', 1)[0]}")
                            if f"({m2}) {m1} {line.rsplit(' ', 1)[0]}" not in eos:
                                eos.append(f"({m2}) {m1} {line.rsplit(' ', 1)[0]}")
                                eos_dict.append({'n': [m1] + line.rsplit(' ', 1)[0].split(), 'i': [m2]})
                                s = s + 1
    for m1 in fm_moves:
        for m2 in fm_basic_moves:
            c = Cube()
            c.move(move_inverse[m2])
            c.scramble_with_inverse(scramble)
            c.move(m1)
            if is_done_eo(c) and m1 in fm_basic_moves and m2 in forbidden[m1]:
                # print(f"({m1}) {m2}")
                if f"({m2}) {m1}" not in eos:
                    eos.append(f"({m2}) {m1}")
                    eos_dict.append({'n': [m1], 'i': [m2]})
                    s = s + 1
            if m2 in ['F', 'B']:
                or_F = orientation_F(c)
                with open("eos_sub3_with_orientation_FB.txt", "r+") as f:
                    for line in f:
                        if line.rstrip().split(" ")[-1] == or_F and line.rstrip().split(" ")[0] not in forbidden[m1] \
                                and (len(line.rstrip().split(" ")) < 3 or not (
                                line.rstrip().split(" ")[0] in forbidden_second[m1]
                                and line.rstrip().split(" ")[1] in forbidden[m1])):
                            # print(f"({m1} {line.rsplit(' ', 1)[0]}) {m2}")
                            if f"({m1} {line.rsplit(' ', 1)[0]}) {m2}" not in eos:
                                eos.append(f"({m1} {line.rsplit(' ', 1)[0]}) {m2}")
                                eos_dict.append({'n': [m1] + line.rsplit(' ', 1)[0].split(), 'i': [m2]})
                                s = s + 1
            if m2 in ['R', 'L']:
                or_R = orientation_R(c)
                with open("eos_sub3_with_orientation_RL.txt", "r+") as f:
                    for line in f:
                        if line.rstrip().split(" ")[-1] == or_R and line.rstrip().split(" ")[0] not in forbidden[m1] \
                                and (len(line.rstrip().split(" ")) < 3 or not (
                                line.rstrip().split(" ")[0] in forbidden_second[m1]
                                and line.rstrip().split(" ")[1] in forbidden[m1])):
                            # print(f"({m1} {line.rsplit(' ', 1)[0]}) {m2}")
                            if f"({m1} {line.rsplit(' ', 1)[0]}) {m2}" not in eos:
                                eos.append(f"({m1} {line.rsplit(' ', 1)[0]}) {m2}")
                                eos_dict.append({'n': [m1] + line.rsplit(' ', 1)[0].split(), 'i': [m2]})
                                s = s + 1
            if m2 in ['U', 'D']:
                or_U = orientation_U(c)
                with open("eos_sub3_with_orientation_UD.txt", "r+") as f:
                    for line in f:
                        if line.rstrip().split(" ")[-1] == or_U and line.rstrip().split(" ")[0] not in forbidden[m1] \
                                and (len(line.rstrip().split(" ")) < 3 or not (
                                line.rstrip().split(" ")[0] in forbidden_second[m1]
                                and line.rstrip().split(" ")[1] in forbidden[m1])):
                            # print(f"({m1} {line.rsplit(' ', 1)[0]}) {m2}")
                            if f"({m1} {line.rsplit(' ', 1)[0]}) {m2}" not in eos:
                                eos.append(f"({m1} {line.rsplit(' ', 1)[0]}) {m2}")
                                eos_dict.append({'n': [m1] + line.rsplit(' ', 1)[0].split(), 'i': [m2]})
                                s = s + 1

    # print(eos)
    # print(s)
    # print(len(eos))
    eos = sorted(eos, key=lambda x: len(x.split(" ")))
    eos_dict = sorted(eos_dict, key=lambda z: (len(z['n']) + len(z['i'])))
    # for eo in eos:
    #    print(eo)
    # print(len(eo.split(" ")))
    odrzucone = []
    eos_ostateczne = []
    odrzucone_dict = []
    eos_dict_ostateczne = []
    for eo in eos:
        czy = True
        for i in range(len(eo.split(" ")) - 1):
            if i != len(eo.split(" ")) - 1:
                x = eo.split(" ")[i]
                if x[0] == '(':
                    x = x[1:]
                if x[-1] == ')':
                    continue
                y = eo.split(" ")[i + 1][0]

                # print(f"{eo}    {x}     {y}")
                if x in forbidden_second[y] and (x in forbidden["D"] or x in forbidden["L"] or x in forbidden["B"]):
                    czy = False
                    break
        if czy:
            eos_ostateczne.append(eo)
        else:
            odrzucone.append(eo)

    for eo in eos_dict:
        czy = True
        for i in range(len(eo['i']) - 1):
            if i != len(eo['i']) - 1:
                x = eo['i'][i]
                y = eo['i'][i+1]
                if x in forbidden_second[y] and (x in forbidden["D"] or x in forbidden["L"] or x in forbidden["B"]):
                    czy = False
                    break
        for i in range(len(eo['n']) - 1):
            if i != len(eo['n']) - 1:
                x = eo['n'][i]
                y = eo['n'][i+1]
                if x in forbidden_second[y] and (x in forbidden["D"] or x in forbidden["L"] or x in forbidden["B"]):
                    czy = False
                    break


        if czy:
            eos_dict_ostateczne.append(eo)
        else:
            odrzucone_dict.append(eo)
    c = Cube()
    c.scramble(scramble)
    if is_done_eo(c):
        eos_ostateczne.append("eoskip")
        eos_dict_ostateczne.append([])
    '''
    for eo in eos_ostateczne:
        print(eo)
    print(len(eos_ostateczne))
    '''
    return eos_ostateczne, eos_dict_ostateczne


if __name__ == "__main__":
    scramble = "R"
    eos, eos_dict = find_eo(scramble)
    for eo in eos:
        print(eo)
    print(len(eos))
