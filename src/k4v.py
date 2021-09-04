def tabla4(listing):
    print(" P  Q  R  S")
    print("------------|")
    print(" 0  0  0  1 | [1]")
    print(" 0  0  0  0 | [2]")
    print(" 0  0  1  1 | [3]")
    print(" 0  0  1  0 | [4]")
    print(" 0  1  0  1 | [5]")
    print(" 0  1  0  0 | [6]")
    print(" 0  1  1  1 | [7]")
    print(" 1  1  1  0 | [8]")
    print(" 1  0  0  1 | [9]")
    print(" 1  0  0  0 | [10]")
    print(" 1  0  1  1 | [11]")
    print(" 1  0  1  0 | [12]")
    print(" 1  1  0  1 | [13]")
    print(" 1  1  0  0 | [14]")
    print(" 1  1  1  1 | [15]")
    print(" 1  1  1  0 | [16]")

    print("\n\n")
    posib = 16 
    var = " "

    for i in range (0, posib):
        print("variables para [", i , "]");
        listing.append(int(input(var)))

    return listing

def k4v(listing):
    posib = 16
    var = " "
    line1 = ()
    line2 = ()
    line3 = ()
    line4 = ()

    line1 = (listing[0], listing[1], listing[3], listing[2])
    line2 = (listing[4], listing[5], listing[7], listing[6])
    line3 = (listing[12], listing[13], listing[15], listing[14])
    line4 = (listing[8], listing[9], listing[11], listing[10])

    print("\n\n")

    print("  PQ \ RS      00      01      11      10")
    print("          |-------------------------------")
    print("    00    |  ", listing[0] ,"  |  ",listing[1],"  |  ",listing[3],"  |  ",listing[2]," |")
    print("          |-------------------------------")
    print("    01    |  ", listing[4] ,"  |  ",listing[5],"  |  ",listing[7],"  |  ",listing[6]," |")
    print("          |-------------------------------")
    print("    11    |  ", listing[12] ,"  |  ",listing[13],"  |  ",listing[15],"  |  ",listing[14]," |")
    print("          |-------------------------------")
    print("    10    |  ", listing[8] ,"  |  ",listing[9],"  |  ",listing[11],"  |  ",listing[10]," |")

    print("\n\n")

    print("  PQ \ RS      00      01      11      10")
    print("          |---------------------------------")
    print("    00    |  [1]  |  [2]  |  [3]   |  [4]  |")
    print("          |---------------------------------")
    print("    01    |  [5]  |  [6]  |  [7]   |  [8]  |")
    print("          |---------------------------------")
    print("    11    |  [9]  |  [10] |  [11]  |  [12] |")
    print("          |---------------------------------")
    print("    10    |  [13] |  [14] |  [15]  |  [16] |")

    print("\n\n")

# Para todos ceros 
    if          line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("No hay grupos")
        print("Funcion simplificada, S(P, Q, R, S) = 0")

# Para todos unos
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 16 = { [1], [2], [3], [4], [5], [6], [7], [8], ",
                "\n[9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Funcion simplificada, S(P, Q, R, S) = 1")

# Para grupos de 15 unos
    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, S(P, Q, R, S) = S + R + Q + P")
    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")

        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, S(P, Q, R, S) = S' + R + Q + P")
    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, S(P, Q, R, S) = R' + S' + Q + P")
    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")
        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")

        print("Funcion simplificada, S(P, Q, R, S) = R' + S + Q + P")
# ---
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, S(P, Q, R, S) = Q' + S + R + P")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")

        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, S(P, Q, R, S) = Q' + S' + R + P")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, S(P, Q, R, S) = Q' + R' + S' + P")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Grupo de 8 = { [9], [10], [11], [12], [13], [14], [15], [16] }")
        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")

        print("Funcion simplificada, S(P, Q, R, S) = Q' + R' + S + P")
# --- 
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + Q' + S + R")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")

        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + Q' + S' + R")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + Q' + R' + S'")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Grupo de 8 = { [13], [14], [15], [16], [1], [2], [3], [4] }")
        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + Q' + R' + S")
# --- 
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")

        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + S + R + Q")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 8 = { [3], [4], [7], [8], [11], [12], [15], [16] }")
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")

        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + S' + R' + Q")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 8 = { [1], [4], [8], [5], [12], [9], [16], [13] }")
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")

        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + R' + S' + Q")
    elif        line1 == (1, 1, 1, 1) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 8 = { [1], [2], [5], [6], [9], [10], [13], [14] }")
        print("Grupo de 8 = { [2], [3], [6], [7], [10], [11], [14], [15] }")

        print("Grupo de 8 = { [1], [2], [3], [4], [5], [6], [7], [8] }")
        print("Grupo de 8 = { [5], [6], [7], [8], [9], [10], [11], [12] }")

        print("Funcion simplificada, S(P, Q, R, S) = P' + R' + S + Q")

# Para grupos de 15 unos
# Para grupos de 14 unos
# Para grupos de 13 unos
# Para grupos de 12 unos
# Para grupos de 11 unos
# Para grupos de 10 unos
# Para grupos de 9 unos
# Para grupos de 8 unos
# Para grupos de 7 unos
# Para grupos de 6 unos
# Para grupos de 5 unos
# Para grupos de 4 unos
# Para grupos de 3 unos
# Para grupos de 2 unos
        # Grupo verticales de 2
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'R'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [2], [6] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'R'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [3], [7] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'RS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [4], [8] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'RS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [5], [9] }")
        print("Funcion simplificada, S(P, Q, R, S) = QR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [6], [10] }")
        print("Funcion simplificada, S(P, Q, R, S) = QR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [7], [11] }")
        print("Funcion simplificada, S(P, Q, R, S) = QRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [8], [12] }")
        print("Funcion simplificada, S(P, Q, R, S) = QRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 2 = { [9], [13] }")
        print("Funcion simplificada, S(P, Q, R, S) = PR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 2 = { [10], [14] }")
        print("Funcion simplificada, S(P, Q, R, S) = PR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 2 = { [11], [15] }")
        print("Funcion simplificada, S(P, Q, R, S) = PRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 2 = { [12], [16] }")
        print("Funcion simplificada, S(P, Q, R, S) = PRS'")
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 2 = { [13], [1] }")
        print("Funcion simplificada, S(P, Q, R, S) = Q'R'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 2 = { [14], [2] }")
        print("Funcion simplificada, S(P, Q, R, S) = Q'R'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 2 = { [15], [3] }")
        print("Funcion simplificada, S(P, Q, R, S) = Q'RS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 2 = { [16], [4] }")
        print("Funcion simplificada, S(P, Q, R, S) = Q'RS'")

        # Grupo horizontales de 2
    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [1], [2] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'R'")
    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [2], [3] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'S")
    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [3], [4] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'R")
    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [4, [1] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'S'")
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [5], [6] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QR'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [6], [7] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [7], [8] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QR")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [8, [9] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QS'")
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [9], [10] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQR'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [10], [11] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [11], [12] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQR")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 2 = { [12], [13] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQS'")
        # ------
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 2 = { [13], [14] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'R'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 2 = { [14], [15] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 2 = { [15], [16] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'R")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 2 = { [16], [17] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'R")
        # 2 variables, Grupos de unos
        # TODO HACER LOS GRUPOS DE UNOS


# Para grupos de 1 unos
    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [1] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'R'S'")
    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [2] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'R'S")
    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [3] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'RS")
    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [4] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'Q'RS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [5] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [6] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [7] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [8] }")
        print("Funcion simplificada, S(P, Q, R, S) = P'QRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [9] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQR'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [10] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQR'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [11] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQRS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [12] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQRS'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [13] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'R'S'")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'R'S")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [15] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'RS")
    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [16] }")
        print("Funcion simplificada, S(P, Q, R, S) = PQ'RS'")

    print("\n\n")
