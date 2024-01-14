


def TimingRoutine(Lista, tempo):
    return 0
def EventRotine(Evento, s, Lista):
    return 0

def LibraryRotine():
    return 0

def ReporterGeneretor():
    return 0

def SetCalculoLinear():
    Na = int(input("Escolha um numero aleatorio para as entradas: "))
    Ns = int(input("Escolha um numero aleatorio para as Saidas: "))
    A = int(input("A: "))
    C = int(input("C: "))
    M = int(input("Modulo: "))
    print("-------------------------------")
    Cinicial = int(input("Menor tempo de Chegada"))
    Cfinal = int(input("Maior tempo de Chegada"))
    print("-------------------------------")
    Sinicial = int(input("Menor tempo de Saida"))
    Sfinal = int(input("Mair tempo de Saida"))

    Clinear = [Na, Ns, A, C, M, Cinicial, Cfinal, Sinicial, Sfinal]
    return Clinear

def GeradorDeEntradas(Calculo):
    linear = (Calculo[0] * Calculo[2] + Calculo[3]) % Calculo[4]
    Calculo[0] = linear
    print(linear)
    linear = linear/Calculo[4]
    print(linear)
    linear = Calculo[5] + (Calculo[6] - Calculo[5]) * linear
    print(linear)

    return linear, Calculo
def GeradorDeSaidas(Calculo):
    return 0


def MainProgram():

    calculo = SetCalculoLinear()
    sla = GeradorDeEntradas(calculo)


    As = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9]
    Ss = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6]
    Entradas = 0
    Saidas = 0



    Clientes = []
    contCliente = 0
    Atra = []

    saida = False


    servidor = 0
    NumeroEmFila = 0
    Fila = []
    TempoDoUltimoEvento = 0
    Clock = 0
    ListaEntrada = []
    ListaSaida = []
    ListaEntrada.append(0.4)
    ListaSaida.append(0)





    QtdeClientAtendidos = 0
    EsperaTotal = 0
    AreaSobQt = 0
    AreaSobBt = 0
    while QtdeClientAtendidos <= 4:

    #TimingRoutine
        if ListaSaida[Saidas] != 0:
            if ListaEntrada[Entradas] < ListaSaida[Saidas]:

                Evento = 0
            else:
                Evento = 1
        else:
            Evento = 0
            ListaSaida.pop(Saidas)
            saida = True


        #EventRotine
        if Clock == 0:

            TempoDoUltimoEvento = Clock
            Clock = ListaEntrada[Entradas]

            Entradas += 1
            ListaEntrada.append(Clock + As[Entradas])

            Atra.append(0)

            ListaSaida.append(Ss[Saidas] + Clock)

            servidor = 1


        else:
            if Evento == 0:
                if servidor == 0:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaEntrada[Entradas]

                    if saida:
                        ListaSaida.append(Ss[Saidas] + Clock)
                        saida = False
                    else:
                        ListaSaida.append(Ss[Saidas] + Clock)
                        Saidas += 1
                        saida = False



                    Entradas += 1
                    ListaEntrada.append((Clock + As[Entradas]))


                    servidor = 1


                else:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaEntrada[Entradas]


                    Fila.append(Clock)
                    NumeroEmFila += 1

                    Entradas += 1
                    ListaEntrada.append((Clock + As[Entradas]))



            else:
                if NumeroEmFila == 0:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaSaida[Saidas]

                    Atra.append(Clock - ListaSaida[Saidas])

                    ListaSaida.append(0)
                    Saidas += 1

                    servidor = 0

                    QtdeClientAtendidos += 1

                    Clientes.append((ListaEntrada[contCliente], Atra[contCliente], ListaSaida[contCliente]))
                    contCliente += 1

                else:

                    TempoDoUltimoEvento = Clock
                    Clock = ListaSaida[Saidas]


                    Atra.append(ListaSaida[Saidas] - Fila[0])


                    Fila.pop(0)
                    NumeroEmFila -= 1
                    QtdeClientAtendidos += 1

                    Saidas += 1
                    ListaSaida.append(Ss[Saidas] + Clock)

                    Clientes.append((ListaEntrada[contCliente], Atra[contCliente], ListaSaida[contCliente]))
                    contCliente += 1


        print("Clock", Clock)
        print("Fila", Fila)
        print("Entradas", ListaEntrada)
        print("Atrasos", Atra)
        print("Saidas", ListaSaida)
        print("Numero em Fila:", NumeroEmFila, "Numeros entradas:", Entradas, "numero saidas:", Saidas)
        print("Clientes Atendidos", QtdeClientAtendidos)
        print("-----------------------")
    print(Clientes)



MainProgram()

