import socket
import _thread


def abandon():
    clientSocket.close()
    _thread.exit()


serverName = '127.0.0.1'
serverPort = 8888

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

start = input('Introduceti comanda: ')
clientSocket.send(start.encode())  # trimis 1

# COMANDA START -------------------------------------------------------------------------------------------------------1
while 1:
    tabel = clientSocket.recv(200)  # receptat 2
    if 'ABANDON' in tabel.decode():
        abandon()
    elif "COMANDA ERONATA" in tabel.decode():
        print(tabel.decode())
        start = input('Reintroduceti comanda: ')
        clientSocket.send(start.encode())  # trimis 1
    else:
        print(tabel.decode())
        break
# ---------------------------------------------------------------------------------------------------------------------1

arunca = input()
clientSocket.send(arunca.encode())  # trimis 3
# COMANDA ARUNCA ------------------------------------------------------------------------------------------------------2
while 1:
    numbers = clientSocket.recv(20)  # receptat 4
    if 'ABANDON' in numbers.decode():
        abandon()
    elif "COMANDA ERONATA" in numbers.decode():
        print(numbers.decode())
        arunca = input('Reintroduceti comanda: ')
        clientSocket.send(arunca.encode())  # trimis 3
    else:
        print(numbers.decode(), end=" R=")
        break

R = clientSocket.recv(10)  # receptat 5
print(R.decode())
#----------------------------------------------------------------------------------------------------------------------2
opreste_alege = input()
clientSocket.send(opreste_alege.encode())

comandafull = "N1N2N3N4N5N6JOKERTRIPLACHINTAFULLCAREUYAMS"
# COMANDA OPRESTE SAU KEEP --------------------------------------------------------------------------------------------3
while 1:
    opreste_alege = clientSocket.recv(20)
    if 'ABANDON' in opreste_alege.decode():
        abandon()
    elif "COMANDA ERONATA" in opreste_alege.decode():
        print(opreste_alege.decode())
        opreste_alege = input('Reintroduceti comanda: ')
        clientSocket.send(opreste_alege.encode())  # trimis 3
    elif 'PUNCTAJ' in opreste_alege.decode():
        varianta = clientSocket.recv(200)
        print(varianta.decode())
        opreste_alege = input()
        clientSocket.send(opreste_alege.encode())
    elif opreste_alege.decode() in comandafull:
        # COMANDA OPRESTE ---------------------------------------------------------------------------------------------4
        dureaza = 12
        ok = True
        while 1:
            dureaza -= 1
            if ok:
                clientSocket.send(opreste_alege)
            else:
                comanda1 = input("Ce comanda doriti sa introduceti: ")
                clientSocket.send(comanda1.encode())
            ok = False
            varianta = clientSocket.recv(200)
            if 'ABANDON' in varianta.decode():
                abandon()
            elif "COMANDA ERONATA" in varianta.decode():
                dureaza += 1
            elif "SCORUL ACESTA A FOST DEJA SETAT" in varianta.decode():
                dureaza += 1
            print(varianta.decode())
            if dureaza == 0:
                break
            #----------------------------------------------------------------------------------------------------------4
        break
    elif 'KEEP' in opreste_alege.decode():
        # COMANDA KEEP1 -----------------------------------------------------------------------------------------------5
        nr_noi = clientSocket.recv(20)
        R = clientSocket.recv(10)
        print(nr_noi.decode(), end=" R=")
        print(R.decode())
        # -------------------------------------------------------------------------------------------------------------5
        nr_noi2 = input()
        clientSocket.send(nr_noi2.encode())
        while 1:
            nr_noi2 = clientSocket.recv(20)

            if 'COMANDA ERONATA' in nr_noi2.decode():
                print(nr_noi2.decode())
                nr_noi2 = input("Reintroduceti comanda: ")
                clientSocket.send(nr_noi2.encode())
            elif nr_noi2.decode() in comandafull:
                # COMANDA OPRESTE2 ------------------------------------------------------------------------------------6
                dureaza = 12
                ok = True
                while 1:
                    dureaza -= 1
                    if ok:
                        clientSocket.send(nr_noi2)
                    else:
                        nr_noi2 = input("Ce comanda doriti sa introduceti: ")
                        clientSocket.send(nr_noi2.encode())
                    ok = False
                    varianta = clientSocket.recv(200)
                    if 'ABANDON' in varianta.decode():
                        abandon()
                    elif "COMANDA ERONATA" in varianta.decode():
                        dureaza += 1
                    elif "SCORUL ACESTA A FOST DEJA SETAT" in varianta.decode():
                        dureaza += 1
                    print(varianta.decode())
                    if dureaza == 0:
                        break
                    #--------------------------------------------------------------------------------------------------6
                break
            elif 'ABANDON' in nr_noi2.decode():
                abandon()
            else:
                # COMANDA KEEP2 ---------------------------------------------------------------------------------------7
                R = clientSocket.recv(10)
                print(nr_noi2.decode(), end=" R=")
                print(R.decode())
                break
        nr_noi2 = input("Ce comanda doriti sa introduceti: ")
        clientSocket.send(nr_noi2.encode())

        while 1:
            nr_noi2 = clientSocket.recv(200)
            #----------------------------------------------------------------------------------------------------------7
            if 'COMANDA ERONATA' in nr_noi2.decode():
                print(nr_noi2.decode())
                nr_noi2 = input("Reintroduceti comanda: ")
                clientSocket.send(nr_noi2.encode())
            elif 'ABANDON' in nr_noi2.decode():
                abandon()
                break
            elif nr_noi2.decode() in comandafull:
                # COMANDA OPRESTE2 ------------------------------------------------------------------------------------8
                dureaza = 12
                ok = True
                while 1:
                    dureaza -= 1
                    if ok:
                        clientSocket.send(nr_noi2)
                    else:
                        nr_noi2 = input("Ce comanda doriti sa introduceti: ")
                        clientSocket.send(nr_noi2.encode())
                    ok = False
                    varianta = clientSocket.recv(200)

                    if 'ABANDON' in varianta.decode():
                        abandon()
                    elif "COMANDA ERONATA" in varianta.decode():
                        dureaza += 1
                    elif "SCORUL ACESTA A FOST DEJA SETAT" in varianta.decode():
                        dureaza += 1
                    print(varianta.decode())
                    if dureaza == 0:
                        break
                break
                #------------------------------------------------------------------------------------------------------8
        break

clientSocket.close()
