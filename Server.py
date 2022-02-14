import socket
import random


def ordonare(number):
    for i in range(len(number) - 1):
        for j in range(i, len(number)):
            if number[i] > number[j]:
                x = number[i]
                number[i] = number[j]
                number[j] = x


def aruncare_zaruri(number):
    for i in range(len(number)):
        number[i] = random.randint(1, 6)


def N1(number):
    sum = 0
    for i in range(5):
        if number[i] == 1:
            sum += number[i]
    return sum


def N2(number):
    sum = 0
    for i in range(5):
        if number[i] == 2:
            sum += number[i]
    return sum


def N3(number):
    sum = 0
    for i in range(5):
        if number[i] == 3:
            sum += number[i]
    return sum


def N4(number):
    sum = 0
    for i in range(5):
        if number[i] == 4:
            sum += number[i]
    return sum


def N5(number):
    sum = 0
    for i in range(5):
        if number[i] == 5:
            sum += number[i]
    return sum


def N6(number):
    sum = 0
    for i in range(5):
        if number[i] == 6:
            sum += number[i]
    return sum


def JOKER(number):
    sum = 0
    for i in range(5):
        sum += number[i]
    return sum


def TRIPLA(number):
    verif = [0, 0, 0, 0, 0, 0]
    sum = 0
    for i in range(5):
        sum += number[i]
        verif[number[i] - 1] += 1
    for i in range(6):
        if verif[i] == 3:
            print(i + 1)
            return sum
    return 0


def CHINTA(number):
    for i in range(4):
        j = i + 1
        if number[i] != number[j] - 1:
            return 0
    return 20


def FULL(number):
    verif, ok2, ok3 = [0, 0, 0, 0, 0, 0], False, False

    for i in range(5):
        verif[number[i] - 1] += 1
    for i in range(6):
        if verif[i] == 3:
            ok3 = True
        if verif[i] == 2:
            ok2 = True
    if ok2 and ok3:
        return 30
    else:
        return 0


def CAREU(number):
    verif = [0, 0, 0, 0, 0, 0]
    for i in range(5):
        verif[number[i] - 1] += 1
    for i in range(6):
        if verif[i] == 4:
            return 40
    return 0


def YAMS(number):
    verif = [0, 0, 0, 0, 0, 0]
    for i in range(5):
        verif[number[i] - 1] += 1
    for i in range(6):
        if verif[i] == 5:
            return 50
    return 0


def N1_rez():
    if ok[0] == 1:
        return N1(numbers)
    else:
        return ''


def N2_rez():
    if ok[1] == 1:
        return N2(numbers)
    else:
        return ''


def N3_rez():
    if ok[2] == 1:
        return N3(numbers)
    else:
        return ''


def N4_rez():
    if ok[3] == 1:
        return N4(numbers)
    else:
        return ''


def N5_rez():
    if ok[4] == 1:
        return N5(numbers)
    else:
        return ''


def N6_rez():
    if ok[5] == 1:
        return N6(numbers)
    else:
        return ''


def JOKER_rez():
    if ok[6] == 1:
        return JOKER(numbers)
    else:
        return ''


def TRIPLA_rez():
    if ok[7] == 1:
        return TRIPLA(numbers)
    else:
        return ''


def CHINTA_rez():
    if ok[8] == 1:
        return CHINTA(numbers)
    else:
        return ''


def FULL_rez():
    if ok[9] == 1:
        return FULL(numbers)
    else:
        return ''


def CAREU_rez():
    if ok[10] == 1:
        return CAREU(numbers)
    else:
        return ''


def YAMS_rez():
    if ok[11] == 1:
        return YAMS(numbers)
    else:
        return ''


def comenzi():
    global total, bonus
    global ok

    dureaza = 12
    while 1:
        dureaza -= 1
        comanda1 = connectionSocket.recv(200)
        if 'ABANDON' in comanda1.decode():
            connectionSocket.send("ABANDON".encode())
            break
        elif 'N1' in comanda1.decode():
            if ok[0] == 0:
                ok[0] = 1
                total += N1(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'N2' in comanda1.decode():
            if ok[1] == 0:
                ok[1] = 1
                total += N2(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'N3' in comanda1.decode():
            if ok[2] == 0:
                ok[2] = 1
                total += N3(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'N4' in comanda1.decode():
            if ok[3] == 0:
                ok[3] = 1
                total += N4(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'N5' in comanda1.decode():
            if ok[4] == 0:
                ok[4] = 1
                total += N5(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'N6' in comanda1.decode():
            if ok[5] == 0:
                ok[5] = 1
                total += N6(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'JOKER' in comanda1.decode():
            if ok[6] == 0:
                ok[6] = 1
                total += JOKER(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'TRIPLA' in comanda1.decode():
            if ok[7] == 0:
                ok[7] = 1
                total += TRIPLA(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'CHINTA' in comanda1.decode():
            if ok[8] == 0:
                ok[8] = 1
                total += CHINTA(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'FULL' in comanda1.decode():
            if ok[9] == 0:
                ok[9] = 1
                total += FULL(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'CAREU' in comanda1.decode():
            if ok[10] == 0:
                ok[10] = 1
                total += CAREU(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        elif 'YAMS' in comanda1.decode():
            if ok[11] == 0:
                ok[11] = 1
                total += YAMS(numbers)
                if total > 62:
                    bonus = 50
                    if ok[12] == 0:
                        total += bonus
                        ok[12] = 1
                mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> ' \
                               f'{N4_rez()}\nN5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> '\
                               f'{JOKER_rez()}\nTRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> ' \
                               f'{FULL_rez()}\nCAREU --> {CAREU_rez()}' \
                               f'\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
                connectionSocket.send(mesaj_rezult.encode())
            else:
                connectionSocket.send("SCORUL ACESTA A FOST DEJA SETAT".encode())
                dureaza += 1
        else:
            connectionSocket.send("COMANDA ERONATA".encode())
            dureaza += 1
        if dureaza == 0:
            break


def comenzi2():
    global opreste_alege, R, numbers, continuare
    # COMANDA KEEP1 ---------------------------------------------------------------------------------------------------5
    if 'KEEP' in opreste_alege.decode():  # acest if poate fi sters
        lista = opreste_alege.decode()
        print(lista)
        j = 0

        for i in range(len(lista)):  # verificam cate cifre au fost date
            if lista[i].isdigit():
                j += 1

        nr = [0] * j  # numarul numerelor ce vor fi pastrate, memorate intr o lista initializata cu 0
        j = 0
        for i in range(len(lista)):
            if lista[i].isdigit():
                nr[j] = int(lista[i])  # memorarea numerelor date
                j += 1

        ordonare(nr)
        nr_noi = [0] * (5 - j)  # generarea de noi valori
        aruncare_zaruri(nr_noi)
        ordonare(nr_noi)
        j, k = 0, 0
        for i in range(len(numbers)):  # schimbarea numerelor neselectate in numere noi generate
            if j == len(nr):
                numbers[i] = nr_noi[k]
                k += 1
            elif not (numbers[i] == nr[j]):
                numbers[i] = nr_noi[k]
                k += 1
            else:
                j += 1

        print("Numere generate " + str(nr_noi))
        ordonare(numbers)
        print(numbers)
        connectionSocket.send(str(nr_noi).encode())
        R -= 1
        connectionSocket.send((str(R).encode()))
    # -----------------------------------------------------------------------------------------------------------------5
    # al doilea KEEP

    while 1:
        opreste_alege = connectionSocket.recv(100)

        if 'ABANDON' in opreste_alege.decode():
            connectionSocket.send("ABANDON".encode())
            continuare = False
            break
        elif opreste_alege.decode() in comandafull:
            # COMANDA OPRESTE2 ----------------------------------------------------------------------------------------6
            continuare = False
            connectionSocket.send(opreste_alege)
            comenzi()
            break
            # ---------------------------------------------------------------------------------------------------------6
        elif 'KEEP' in opreste_alege.decode():
            # COMANDA KEEP2 -------------------------------------------------------------------------------------------7
            lista = opreste_alege.decode()
            print(lista)
            j = len(nr)
            print("Numere memorate anterior " + str(nr))
            n = 0
            # memorarea numerelor salvate la al doilea KEEP
            for i in range(len(lista)):  # verificam cate cifre au fost date SI LE adaugam
                if lista[i].isdigit():
                    n += 1

            nr2 = [0] * n  # numarul numerelor ce vor fi pastrate, memorate intr o lista initializata cu 0
            n = 0
            for i in range(len(lista)):
                if lista[i].isdigit():
                    nr2[n] = int(lista[i])  # memorarea numerelor date
                    n += 1
            ordonare(nr2)
            # o lista noua cu memorarea tutror numerelor salvate
            nr3 = [0] * j
            for i in range(len(nr)):
                nr3[i] = nr[i]
            for i in range(len(nr2)):
                nr3.append(int(nr2[i]))

            ordonare(nr3)
            print("Toate numerele memorate " + str(nr3))
            # memorarea numerelor noi2

            nr_noi2 = [0] * (5 - (j + n))  # generarea de noi valori
            aruncare_zaruri(nr_noi2)
            print("Numere generate " + str(nr_noi2))

            z, k = 0, 0
            for i in range(len(numbers)):  # schimbarea numerelor neselectate in numere noi generate
                if z == len(nr3):
                    numbers[i] = nr_noi2[k]
                    k += 1
                elif not (numbers[i] == nr3[z]):
                    numbers[i] = nr_noi2[k]
                    k += 1
                elif numbers[i] == nr3[z] and z < len(nr3):
                    z += 1

            ordonare(nr_noi2)
            ordonare(numbers)
            print(numbers)
            connectionSocket.send(str(nr_noi2).encode())
            R -= 1
            connectionSocket.send((str(R).encode()))
            break
            # ---------------------------------------------------------------------------------------------------------7
        else:
            connectionSocket.send("COMANDA ERONATA".encode())


def punctaj():
    global total, bonus

    mesaj_rezult = f'N1 -----> {N1_rez()}\nN2 -----> {N2_rez()}\nN3 -----> {N3_rez()}\nN4 -----> {N4_rez()}\n' \
                   f'N5 -----> {N5_rez()}\nN6 -----> {N6_rez()}\nBONUS --> {bonus}\nJOKER --> {JOKER_rez()}\n' \
                   f'TRIPLA -> {TRIPLA_rez()}\nCHINTA -> {CHINTA_rez()}\nFULL ---> {FULL_rez()}\nCAREU --> ' \
                   f'{CAREU_rez()}\nYAMS ---> {YAMS_rez()}\nTOTAL --> {total}'
    connectionSocket.send(mesaj_rezult.encode())


serverPort = 8888
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('Serverul TCP este pregatit de lucru.')
while 1:

    total = bonus = 0
    ok = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # COMANDA START ---------------------------------------------------------------------------------------------------1
    peste = True
    while 1:
        if peste:
            connectionSocket, clientAddress = serverSocket.accept()
            print('Accesat de catre client:', clientAddress)
        start = connectionSocket.recv(10)
        if 'START' in start.decode():
            connectionSocket.send("N1 ----->\nN2 ----->\nN3 ----->\nN4 ----->\nN5 ----->\nN6 ----->\nBONUS -->\nJOKER "
                                  "-->\nTRIPLA ->\nCHINTA ->\nFULL --->\nCAREU -->\nYAMS --->\nTOTAL -->".encode())
            peste = True
            break
        elif 'ABANDON' in start.decode():
            connectionSocket.send("ABANDON".encode())
            peste = True
            connectionSocket.close()
        else:
            peste = False
            connectionSocket.send("COMANDA ERONATA".encode())
    # -----------------------------------------------------------------------------------------------------------------1
    while 1:
        # COMANDA ARUNCA ----------------------------------------------------------------------------------------------2
        arunca = connectionSocket.recv(10)
        if "ARUNCA" in arunca.decode():
            numbers = [1, 2, 3, 4, 5]
            R = 2
            aruncare_zaruri(numbers)
            ordonare(numbers)
            print(numbers)
            connectionSocket.send(str(numbers).encode())
            connectionSocket.send(str(R).encode())
            break
        elif 'ABANDON' in arunca.decode():
            connectionSocket.send("ABANDON".encode())
            peste = False
            connectionSocket.close()
            break
        else:
            connectionSocket.send("COMANDA ERONATA".encode())
    # -----------------------------------------------------------------------------------------------------------------2
    comandafull = "N1N2N3N4N5N6JOKERTRIPLACHINTAFULLCAREUYAMS"
    # COMANDA OPRESTE SAU KEEP ----------------------------------------------------------------------------------------3
    if peste:
        while 1:
            opreste_alege = connectionSocket.recv(20)
            if "PUNCTAJ" in opreste_alege.decode():
                connectionSocket.send("PUNCTAJ".encode())
                punctaj()
            elif opreste_alege.decode() in comandafull:
                # COMANDA OPRESTE -------------------------------------------------------------------------------------4
                connectionSocket.send(opreste_alege)
                continuare = False
                comenzi()
                break
                # -----------------------------------------------------------------------------------------------------4
            elif "KEEP" in opreste_alege.decode():
                # COMANDA KEEP1 ---------------------------------------------------------------------------------------5
                connectionSocket.send("KEEP".encode())
                continuare = True
                comenzi2()
                break
                # -----------------------------------------------------------------------------------------------------5
            elif 'ABANDON' in opreste_alege.decode():
                connectionSocket.send("ABANDON".encode())
                continuare = False
                break
            else:
                connectionSocket.send("COMANDA ERONATA".encode())

        # COMANDA OPRESTE2 --------------------------------------------------------------------------------------------8

        if continuare:
            while 1:
                opreste_alege = connectionSocket.recv(200)
                if 'ABANDON' in opreste_alege.decode():
                    connectionSocket.send("ABANDON".encode())
                    break
                elif opreste_alege.decode() in comandafull:
                    connectionSocket.send(opreste_alege)
                    comenzi()
                    break
                else:
                    connectionSocket.send("COMANDA ERONATA".encode())
    # -----------------------------------------------------------------------------------------------------------------8
    peste = True
    continuare = True
    print("conexiunea s a terminat")
    connectionSocket.close()
