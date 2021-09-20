from colorama import Fore, Back, Style

def tabla4(listing):
    print(Fore.RED + " P  Q  R  S")
    print("------------|")
    print(Fore.RESET +" 0  0  0  1 " + Fore.RED + "| [1]")
    print(Fore.RESET +" 0  0  0  0 " + Fore.RED + "| [2]")
    print(Fore.RESET +" 0  0  1  1 " + Fore.RED + "| [3]")
    print(Fore.RESET +" 0  0  1  0 " + Fore.RED + "| [4]")
    print(Fore.RESET +" 0  1  0  1 " + Fore.RED + "| [5]")
    print(Fore.RESET +" 0  1  0  0 " + Fore.RED + "| [6]")
    print(Fore.RESET +" 0  1  1  1 " + Fore.RED + "| [7]")
    print(Fore.RESET +" 1  1  1  0 " + Fore.RED + "| [8]")
    print(Fore.RESET +" 1  0  0  1 " + Fore.RED + "| [9]")
    print(Fore.RESET +" 1  0  0  0 " + Fore.RED + "| [10]")
    print(Fore.RESET +" 1  0  1  1 " + Fore.RED + "| [11]")
    print(Fore.RESET +" 1  0  1  0 " + Fore.RED + "| [12]")
    print(Fore.RESET +" 1  1  0  1 " + Fore.RED + "| [13]")
    print(Fore.RESET +" 1  1  0  0 " + Fore.RED + "| [14]")
    print(Fore.RESET +" 1  1  1  1 " + Fore.RED + "| [15]")
    print(Fore.RESET +" 1  1  1  0 " + Fore.RED + "| [16]")

    print("\n")
    posib = 16 
    var = " "

    for i in range (0, posib):
        while var != 0 and var != 1:
            print(Fore.RESET + "Variables para " + Fore.RED + "[ ", i ," ]" + Fore.RESET);
            var = int(input())
        listing.append(var)
        var = " "

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

    print("\n")

    print(Fore.LIGHTYELLOW_EX + "  PQ \ RS      00      01      11      10")
    print("          |-------------------------------")
    print("    00    |  ", listing[0] ,"  |  ",listing[1],"  |  ",listing[3],"  |  ",listing[2]," |")
    print("          |-------------------------------")
    print("    01    |  ", listing[4] ,"  |  ",listing[5],"  |  ",listing[7],"  |  ",listing[6]," |")
    print("          |-------------------------------")
    print("    11    |  ", listing[12] ,"  |  ",listing[13],"  |  ",listing[15],"  |  ",listing[14]," |")
    print("          |-------------------------------")
    print("    10    |  ", listing[8] ,"  |  ",listing[9],"  |  ",listing[11],"  |  ",listing[10]," |")

    print("\n")

    print(Fore.LIGHTBLUE_EX + "  PQ \ RS      00      01      11      10")
    print("          |---------------------------------")
    print("    00    |  [1]  |  [2]  |  [3]   |  [4]  |")
    print("          |---------------------------------")
    print("    01    |  [5]  |  [6]  |  [7]   |  [8]  |")
    print("          |---------------------------------")
    print("    11    |  [9]  |  [10] |  [11]  |  [12] |")
    print("          |---------------------------------")
    print("    10    |  [13] |  [14] |  [15]  |  [16] |")

    print("\n" + Fore.WHITE)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Para todos ceros 
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
    if          line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("No hay grupos")
        print("Funcion simplificada, f(P, Q, R, S) = 0")


    #1	2	3	a	
    #4	<=	a	<=	16		

    elif        line1 == (1, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    #1	2	b	a	
    #4	<=	b	<=	15		
    #5	<=	a	<=	16		

    # b == 4

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 5

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    #1	c	b	a	
    #2	<=	c	<=	14		
    #3	<=	b	<=	15		
    #4	<=	a	<=	16		

    ## c = 3

    # b == 4

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 5

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 4

    # b == 5

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 5

    # b == 6

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (1, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    #d	c	b	a	
    #2	<=	d	<=	13		
    #3	<=	c	<=	14		
    #4	<=	b	<=	15		
    #5	<=	a	<=	16		

    ### d = 2

    ## c = 3

    # b == 4

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 5

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 4

    # b == 5

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 5

    # b == 6

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 1, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 3

    ## c = 4

    # b == 5

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 6

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 5

    # b == 6

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 1, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 4

    ## c = 5

    # b == 6

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 7

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 6

    # b == 7

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 1) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 5

    ## c = 6

    # b == 7

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 8

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (1, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 6

    ## c = 7

    # b == 8

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 1, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 7

    ## c = 8

    # b == 9

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 1, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 8

    ## c = 9

    # b == 10

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 1) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 9

    ## c = 10

    # b == 11

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 1) \
            and line4 == (0, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 1, 0) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 1, 0, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (1, 0, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 10

    ## c = 11

    # b == 12

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (1, 0, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 1) \
            and line4 == (0, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 1, 0) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 1, 0, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 11

    ## c = 12

    # b == 13

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 1, 0, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (1, 0, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 1) \
            and line4 == (0, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 1, 0) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 12

    ## c = 13

    # b == 14

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 1, 0):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 1, 0, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (1, 0, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 1) \
            and line4 == (0, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    ### d = 13

    ## c = 14

    # b == 15

    elif        line1 == (0, 0, 0, 0) \
            and line2 == (0, 0, 0, 0) \
            and line3 == (0, 0, 0, 0) \
            and line4 == (1, 1, 1, 1):
        print("Grupo de 1 = { [14] }")
        print("Grupo de 2 = { [1], [5] }")
        print("Funcion simplificada, f(P, Q, R, S) = ")


    print("\n\n")
