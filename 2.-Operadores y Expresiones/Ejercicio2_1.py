
while True:
    numero_base = int(input("Indicame un número entre el 1 y el 10:   "))

    if numero_base >= 1 and numero_base <= 10:

        por_uno = f"1 x {numero_base}: {1*numero_base} "
        por_dos = f"2 x {numero_base}: {2*numero_base} "
        por_tres = f"3 x {numero_base}: {3*numero_base} "
        por_cuatro = f"4 x {numero_base}: {4*numero_base} "
        por_cinco = f"5 x {numero_base}: {5*numero_base} "
        por_seis = f"6 x {numero_base}: {6*numero_base} "
        por_siete = f"7 x {numero_base}: {7*numero_base} "
        por_ocho = f"8 x {numero_base}: {8*numero_base} "
        por_nueve = f"9 x {numero_base}: {9*numero_base} "
        por_diez = f"10 x {numero_base}: {10*numero_base} "

    else:
        print("Introduce un número que este entre el 1 y el 10 mamahuevo")
        continue

    print(por_uno)
    print(por_dos)  
    print(por_tres)
    print(por_cuatro)
    print(por_cinco)
    print(por_seis)
    print(por_siete)
    print(por_ocho)
    print(por_nueve)
    print(por_diez)

