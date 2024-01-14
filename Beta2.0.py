from numpy import log as ln


def SetCalculo():

    print("Calculo:")
    print("1-Congruente Linear")
    print(("2-Quadrado Médio"))
    calculo = input("Digite no numero indicado para escolher:")
    print("-------------------------------")
    Minicial = int(input("Tempo Médio entre chegadas (exponencial): "))
    Mfinal = int(input("Tempo médio de atendimento (exponencial:): "))

    print("-------------------------------")

    if calculo == "1":

        X = int(input("Escolha um numero aleatorio para a semente: "))
        A = int(input("A: "))
        C = int(input("C: "))
        M = int(input("Modulo: "))

        Clinear = [1, X, A, C, M, Minicial, Mfinal]
        return Clinear

    elif calculo == "2":
        print("escolha a quantidade de digitos")
        print("2 digitos")
        print("4 digitos")
        digito = input("Digite qual deles você quer com o numero:")

        if digito == "2":
            Na = int(input("Escolha um numero aleatorio de 2 digitos para as entradas: "))
            Clinear = [2.1, Na, Minicial, Mfinal]
            return Clinear

        elif digito == "4":
            Na = int(input("Escolha um numero aleatorio de 4 digitos para as entradas: "))
            Clinear = [2.2, Na, Minicial, Mfinal]
            return Clinear
def GeradorDeEntradas(Calculo):
    if Calculo[0] == 1:
        linear = (Calculo[1] * Calculo[2] + Calculo[3]) % Calculo[4]
        Calculo[1] = linear

        linear = linear/Calculo[4]-1

        linear = ln(linear)/Calculo[5]

        return linear, Calculo

    elif Calculo[0] == 2.1:

        String = str(int(Calculo[1]) ** 2)

        while len(String) != 4:
            String = "0" + String
        Calculo[1] = int(String[1:3])
        npa = int(String[1:3])/99
        npa = ln(npa)/Calculo[2]
        return npa, Calculo

    elif Calculo[0] == 2.2:

        String = str(int(Calculo[1]) ** 2)

        while len(String) != 8:
            String = "0" + String
        Calculo[1] = int(String[2:6])
        npa = int(String[2:6]) / 9999
        npa = ln(npa)/Calculo[2]

        return npa, Calculo
def GeradorDeSaidas(Calculo):

    if Calculo[0] == 1:
        linear = (Calculo[1] * Calculo[2] + Calculo[3]) % Calculo[4]
        Calculo[1] = linear

        linear = linear/Calculo[4]-1

        linear = ln(linear)/Calculo[6]

        return linear, Calculo

    elif Calculo[0] == 2.1:

        String = str(int(Calculo[1]) ** 2)

        while len(String) != 4:
            String = "0" + String
        Calculo[2] = int(String[1:3])
        npa = int(String[1:3]) / 99
        npa = ln(npa)/Calculo[3]

        return npa, Calculo

    elif Calculo[0] == 2.2:

        String = str(int(Calculo[1]) ** 2)

        while len(String) != 8:
            String = "0" + String
        Calculo[2] = int(String[2:6])
        npa = int(String[2:6]) / 9999
        npa = ln(npa)/Calculo[3]

        return npa, Calculo
def MainProgram():

    calculo = SetCalculo()
    sla = GeradorDeEntradas(calculo)
    isso = GeradorDeSaidas(calculo)
    Entradas = 0
    Saidas = 0
    Clientes = []
    contCliente = 0
    Atra = []
    saida = False
    servidor = 0
    ocioso = True
    NumeroEmFila = 0
    Fila = []
    TempoDoUltimoEvento = 0
    Clock = 0
    ListaEntrada = []
    ListaSaida = []
    ListaEntrada.append(sla[0])
    ListaSaida.append(0)
    Tevent = ""
    QtdeClientAtendidos = 0
    espera = 0
    EsperaTotal = 0
    AreaSobQt = NumeroEmFila * (Clock - TempoDoUltimoEvento)
    AreaSobBt = servidor * (Clock - TempoDoUltimoEvento)
    Ca = input("Quantal tempo até o fim da simulção? : ")
    Cerao = False

    while Clock <= int(Ca) or Cerao:

        # TimingRoutine
        if ListaSaida[Saidas] != 0:
            if ListaEntrada[Entradas] < ListaSaida[Saidas] and Cerao:
                Evento = 0
                Tevent = "Entrada"
            else:
                Evento = 1
                Tevent = "Saida"
        else:
            Evento = 0
            Tevent = "Entrada"
            ListaSaida.pop(Saidas)
            saida = True

        # EventRotine
        if Clock == 0:

            TempoDoUltimoEvento = Clock
            Clock = ListaEntrada[Entradas]

            sla = GeradorDeEntradas(sla[1])
            isso = GeradorDeSaidas(calculo)


            Entradas += 1
            ListaEntrada.append(Clock + sla[0])

            Atra.append(0)

            ListaSaida.append(isso[0] + Clock)

            servidor = 1

            mostraSistema(Clock, Tevent, TempoDoUltimoEvento, servidor, NumeroEmFila, Fila, ListaEntrada, Entradas, ListaSaida, Saidas, QtdeClientAtendidos, EsperaTotal, AreaSobQt, AreaSobBt)

        else:
            if Evento == 0:
                if servidor == 0:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaEntrada[Entradas]

                    servidor = 1

                    Atra.append(0)

                    sla = GeradorDeEntradas(sla[1])
                    isso = GeradorDeSaidas(isso[1])

                    if saida:
                        ListaSaida.append(isso[0] + Clock)
                        saida = False
                    else:
                        ListaSaida.append(isso[0] + Clock)
                        Saidas += 1
                        saida = False


                    Entradas += 1
                    ListaEntrada.append((Clock + sla[0]))




                    ocioso = False
                else:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaEntrada[Entradas]


                    Fila.append(Clock)
                    NumeroEmFila += 1

                    sla = GeradorDeEntradas(sla[1])

                    Entradas += 1
                    ListaEntrada.append((Clock + sla[0]))
            else:
                if NumeroEmFila == 0:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaSaida[Saidas]

                    Clientes.append((ListaEntrada[contCliente], Atra[contCliente], ListaSaida[contCliente]))
                    contCliente += 1

                    QtdeClientAtendidos += 1

                    ListaSaida.append(0)
                    Saidas += 1

                    ocioso = True

                else:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaSaida[Saidas]

                    Clientes.append((ListaEntrada[contCliente], Atra[contCliente], ListaSaida[contCliente]))
                    contCliente += 1
                    QtdeClientAtendidos += 1

                    Fila.pop(0)
                    NumeroEmFila -= 1
                    Atra.append(ListaSaida[Saidas] - Fila[0])

                    isso = GeradorDeSaidas(isso[1])
                    Saidas += 1
                    ListaSaida.append(isso[0] + Clock)

            for atrasos in Atra:
                espera = espera + atrasos
            EsperaTotal = espera
            espera = 0

            AreaSobQt = AreaSobQt + NumeroEmFila * (Clock - TempoDoUltimoEvento)
            AreaSobBt = AreaSobBt + servidor * (Clock - TempoDoUltimoEvento)

            if ocioso: servidor = 0
            else: servidor = 1
            mostraSistema(Clock, Tevent, TempoDoUltimoEvento, servidor, NumeroEmFila, Fila, ListaEntrada, Entradas,ListaSaida, Saidas, QtdeClientAtendidos, EsperaTotal, AreaSobQt, AreaSobBt)
            print(ListaEntrada)
            print(ListaSaida)
            mostraClientes(Clientes)

    Cerao = DepoisDoEspediente(Clock, NumeroEmFila, Ca)

def DepoisDoEspediente(Clock, NumeroEmFila, Ca):
    if Clock == int(Ca):
        if NumeroEmFila == 0:
            return False
        else:
            return True
    else:
        return False
def mostraSistema(Clock, Tevent, TempoDoUltimoEvento, servidor, NumeroEmFila, Fila, ListaEntrada, Entradas, ListaSaida, Saidas, QtdeClientAtendidos, EsperaTotal, AreaSobQt, AreaSobBt):
    print( "-----------------------------------------------------------------------------------------------------------------------------------------")
    print("|", "              ", "Clock: ", Clock, "      ", "Evento: ", Tevent, "   ", "Ultimo Evento: ", TempoDoUltimoEvento)
    print("|", "                  ", "Servidor: ", servidor, "           ", "Numero em fila: ", NumeroEmFila)
    print("|", "                                                                                                                                    ", "|")
    print("|", "                                   ", "Fila: ", Fila)
    print("|", "                                                                                                                                    ", "|")
    print("|", "                Proxima entrada: ", ListaEntrada[Entradas], "", "Proxima saida: ", ListaSaida[Saidas])
    print("|", "                                                                                                                                    ", "|")
    print("|", "                                                                                                                                    ", "|")
    print("|", "Clientes Atendidos: ", QtdeClientAtendidos, "|", "Espera Total: ", EsperaTotal, "|", "Área sob Q(t): ", AreaSobQt, "|", "Área sob B(t): ", AreaSobBt)
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
def mostraClientes(Clientes):
    print("Id", "Entrada", "Atraso", "Saida")
    cont = 1
    for c in Clientes:
        print(cont, c)
        cont += 1

MainProgram()
continua = input("Aperte enter para continuar...")


