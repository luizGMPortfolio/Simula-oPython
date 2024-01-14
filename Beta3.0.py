from numpy import log as ln

def texteQuiQuadradoMCL(X, A, C, M):
    valido = False
    while not valido:
        Npa = X
        count = 0
        Separador = [0, 0, 0, 0, 0]
        Lista = []

        while count <= 100:
            Npa = (Npa * A + C) % M
            N = Npa/(M-1)
            Lista.append(Npa)
            if N < 0.2:
                Separador[0] += 1
            elif N > 0.2 and N < 0.4:
                Separador[1] += 1
            elif N > 0.4 and N < 0.6:
                Separador[2] += 1
            elif N > 0.6 and N < 0.8:
                Separador[3] += 1
            elif N > 0.8 and N < 1:
                Separador[4] += 1
            count += 1

        quiQuadrado = ((Separador[0] - 20) ** 2)/20 + ((Separador[1] - 20) ** 2)/20 + ((Separador[2] - 20) ** 2)/20 + ((Separador[3] - 20) ** 2)/20 + ((Separador[4] - 20) ** 2)/20
        if quiQuadrado < 9.49:
            print("Sua semente é valida")
            valido = True
            return X, A, C, M
        else:
            print("Sua semente é invalida")
            print("Informe uma semente valida")
            X = int(input("Escolha um numero aleatorio para a semente: "))
            A = int(input("A: "))
            C = int(input("C: "))
            M = int(input("Modulo: "))
def SetCalculo():

    print("Método de Geração das NPAs: ")
    print("1-Congruente Linear")
    print(("2-Quadrado Médio"))
    Metodo = input("Digite no numero indicado para escolher: ")
    print("Tipo de Distribuição: ")
    print("1-Exponencial")
    print("2-Uniforme")
    Distribuicao = input("Digite no numero indicado para escolher: ")


    print("-------------------------------")

    if Distribuicao == "1":
        Minicial = float(input("Tempo Médio entre chegadas (exponencial): "))
        Mfinal = float(input("Tempo médio de atendimento (exponencial:): "))

        if Metodo == "1":
            X = int(input("Escolha um numero aleatorio para a semente: "))
            A = int(input("A: "))
            C = int(input("C: "))
            M = int(input("Modulo: "))

            resultado = texteQuiQuadradoMCL(X, A, C, M)
            Ns = resultado[0]

            Clinear = ["Exponencial", 1, resultado[0], Ns, resultado[1], resultado[2], resultado[3], Minicial, Mfinal]
            return Clinear
        elif Metodo == "2":
            print("escolha a quantidade de digitos")
            print("2 digitos")
            print("4 digitos")
            digito = input("Digite qual deles você quer com o numero:")

            if digito == "2":
                Na = int(input("Escolha um numero aleatorio de 2 digitos para as entradas: "))
                Ns = Na
                Clinear = ["Exponencial", 2, Na, Ns, Minicial, Mfinal]
                return Clinear

            elif digito == "4":
                Na = int(input("Escolha um numero aleatorio de 4 digitos para as entradas: "))
                Ns = Na
                Clinear = ["Exponencial", 4, Na, Ns, Minicial, Mfinal]
                return Clinear

    elif Distribuicao == "2":
        Cinicial = int(input("Menor tempo de Chegada: "))
        Cfinal = int(input("Maior tempo de Chegada: "))
        print("-------------------------------")
        Sinicial = float(input("Menor tempo de atendimento possivel: "))
        Sfinal = float(input("Maior tempo de atendimento possivel: "))

        if Metodo == "1":
            X = int(input("Escolha um numero aleatorio para a semente: "))
            A = int(input("A: "))
            C = int(input("C: "))
            M = int(input("Modulo: "))

            resultado = texteQuiQuadradoMCL(X, A, C, M)
            Ns = resultado[0]

            Clinear = ["Uniforme", 1, resultado[0], Ns, resultado[1], resultado[2], resultado[3], Cinicial, Cfinal, Sinicial, Sfinal]
            return Clinear
        elif Metodo == "2":
            print("escolha a quantidade de digitos")
            print("2 digitos")
            print("4 digitos")
            digito = input("Digite qual deles você quer com o numero:")

            if digito == "2":
                Na = int(input("Escolha um numero aleatorio de 2 digitos para as entradas: "))
                Clinear = ["Unifome", 2, Na, Cinicial, Cfinal, Sinicial, Sfinal]
                return Clinear

            elif digito == "4":
                Na = int(input("Escolha um numero aleatorio de 4 digitos para as entradas: "))
                Clinear = ["Uniforme", 4, Na, Cinicial, Cfinal, Sinicial, Sfinal]
                return Clinear
def GeradorDeEntradas(Calculo):
    if Calculo[1] == 1:
        linear = (Calculo[2] * Calculo[4] + Calculo[5]) % Calculo[6]
        if linear == 0:
            linear = (linear * Calculo[4] + Calculo[5]) % Calculo[6]

        Calculo[2] = linear
        linear = linear/(Calculo[6]-1)
        if Calculo[0] == "Exponencial":
            linear = abs(ln(linear) * Calculo[7])
        elif Calculo[0] == "Uniforme":
            linear = Calculo[7] + (Calculo[8] - Calculo[7]) * linear
        return linear, Calculo
    elif Calculo[1] == 2:
        String = str(int(Calculo[2]) ** 2)
        while len(String) != 4:
            String = "0" + String
        Calculo[2] = int(String[1:3])
        npa = int(String[1:3])/99
        if Calculo[0] == "Exponencial":
            npa = abs(ln(npa)/Calculo[3])
        elif Calculo[0] == "Uniforme":
            npa = Calculo[3] + (Calculo[4] - Calculo[3]) * npa
        return npa, Calculo
    elif Calculo[1] == 4:
        String = str(int(Calculo[2]) ** 2)
        while len(String) != 8:
            String = "0" + String
        Calculo[2] = int(String[2:6])
        npa = int(String[2:6]) / 9999
        if Calculo[0] == "Exponencial":
            npa = abs(ln(npa) / Calculo[3])
        elif Calculo[0] == "Uniforme":
            npa = Calculo[3] + (Calculo[4] - Calculo[3]) * npa
        return npa, Calculo
def GeradorDeSaidas(Calculo):
    if Calculo[1] == 1:
        linear = (Calculo[3] * Calculo[4] + Calculo[5]) % Calculo[6]
        if linear == 0:
            linear = (linear * Calculo[4] + Calculo[5]) % Calculo[6]

        Calculo[3] = linear
        linear = linear/(Calculo[6]-1)
        if Calculo[0] == "Exponencial":
            linear = abs(ln(linear) * Calculo[8])
        elif Calculo[0] == "Uniforme":
            linear = Calculo[9] + (Calculo[10] - Calculo[9]) * linear
        return linear, Calculo
    elif Calculo[1] == 2:
        String = str(int(Calculo[2]) ** 2)
        while len(String) != 4:
            String = "0" + String
        Calculo[2] = int(String[1:3])
        npa = int(String[1:3]) / 99
        if Calculo[0] == "Exponencial":
            npa = abs(ln(npa) / Calculo[4])
        elif Calculo[0] == "Uniforme":
            npa = Calculo[5] + (Calculo[6] - Calculo[5]) * npa
        return npa, Calculo
    elif Calculo[1] == 4:
        String = str(int(Calculo[2]) ** 2)
        while len(String) != 8:
            String = "0" + String
        Calculo[2] = int(String[2:6])
        npa = int(String[2:6]) / 9999
        if Calculo[0] == "Exponencial":
            npa = abs(ln(npa) / Calculo[4])
        elif Calculo[0] == "Uniforme":
            npa = Calculo[5] + (Calculo[6] - Calculo[5]) * npa
        return npa, Calculo
def MainProgram():

    calculo = SetCalculo()
    sla = GeradorDeEntradas(calculo)
    isso = GeradorDeSaidas(calculo)


    saida = False
    Cerao = False
    ocioso = True

    Clock = 0
    servidor = 0
    TempoDoUltimoEvento = 0

    Entradas = 0
    Saidas = 0
    contCliente = 0
    NumeroEmFila = 0
    QtdeClientAtendidos = 0
    espera = 0
    EsperaTotal = 0
    AreaSobQt = 0
    AreaSobBt = 0

    Fila = []
    ListaEntrada = []
    ListaSaida = []
    Atra = []
    Clientes = []
    numerosEmFila = []

    ListaEntrada.append(sla[0])
    ListaSaida.append(0)

    Tevent = ""
    mostra = "s"


    Ca = input("Quantal tempo até o fim da simulção? : ")

    while Clock <= int(Ca) or Cerao:

        # TimingRoutine
        if ListaSaida[Saidas] != 0:
            if ListaEntrada[Entradas] < ListaSaida[Saidas] and not Cerao:
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

        if Evento == 0:
            if servidor == 0:

                if Clock != 0:
                    isso = GeradorDeSaidas(isso[1])

                TempoDoUltimoEvento = Clock
                Clock = ListaEntrada[Entradas]

                ocioso = False

                Atra.append(0)

                sla = GeradorDeEntradas(sla[1])

                if saida:
                    ListaSaida.append(isso[0] + Clock)
                    saida = False
                else:
                    ListaSaida.append(isso[0] + Clock)
                    Saidas += 1
                    saida = False

                Entradas += 1
                ListaEntrada.append((Clock + sla[0]))
            else:

                TempoDoUltimoEvento = Clock
                Clock = ListaEntrada[Entradas]

                Fila.append(Clock)
                NumeroEmFila += 1

                sla = GeradorDeEntradas(sla[1])

                Entradas += 1
                ListaEntrada.append((Clock + sla[0]))

                AreaSobQt = AreaSobQt + NumeroEmFila * (Clock - TempoDoUltimoEvento)
                AreaSobBt = AreaSobBt + servidor * (Clock - TempoDoUltimoEvento)

        else:
            if NumeroEmFila == 0:

                TempoDoUltimoEvento = Clock
                Clock = ListaSaida[Saidas]

                Clientes.append((ListaEntrada[contCliente], Atra[contCliente], ListaSaida[contCliente]))
                contCliente += 1

                AreaSobBt = AreaSobBt + servidor * (Clock - TempoDoUltimoEvento)

                QtdeClientAtendidos += 1

                ListaSaida.append(0)
                Saidas += 1

                ocioso = True
            else:

                TempoDoUltimoEvento = Clock
                Clock = ListaSaida[Saidas]

                Clientes.append((ListaEntrada[contCliente], Atra[contCliente], ListaSaida[contCliente]))
                contCliente += 1

                AreaSobQt = AreaSobQt + NumeroEmFila * (Clock - TempoDoUltimoEvento)

                QtdeClientAtendidos += 1

                Atra.append(Clock - Fila[0])
                Fila.pop(0)
                NumeroEmFila -= 1

                isso = GeradorDeSaidas(isso[1])
                Saidas += 1
                ListaSaida.append(isso[0] + Clock)


        for atrasos in Atra:
            espera = espera + atrasos
        EsperaTotal = espera
        espera = 0

        if ocioso: servidor = 0
        else: servidor = 1
        if mostra == "s":
            mostraSistema(Clock, Tevent, TempoDoUltimoEvento, servidor, NumeroEmFila, Fila, ListaEntrada, Entradas,ListaSaida, Saidas, QtdeClientAtendidos, EsperaTotal, AreaSobQt, AreaSobBt)
            mostra = input("deseja continuar mostrando s/n: ")

        numerosEmFila.append(NumeroEmFila)
        Cerao = DepoisDoEspediente(Clock, NumeroEmFila, Ca)

    mostraSistema(Clock, Tevent, TempoDoUltimoEvento, servidor, NumeroEmFila, Fila, ListaEntrada, Entradas, ListaSaida,Saidas, QtdeClientAtendidos, EsperaTotal, AreaSobQt, AreaSobBt)
    mostraResultados(Clientes, numerosEmFila, Ca, AreaSobQt, AreaSobBt)
    mostraClientes(Clientes)
    print(ListaEntrada)
    print(ListaSaida)
def DepoisDoEspediente(Clock, NumeroEmFila, Ca):
    if Clock >= int(Ca):
        if NumeroEmFila == 0:
            return False
        else:
            return True
    else:
        return False
def mostraSistema(Clock, Tevent, TempoDoUltimoEvento, servidor, NumeroEmFila, Fila, ListaEntrada, Entradas, ListaSaida, Saidas, QtdeClientAtendidos, EsperaTotal, AreaSobQt, AreaSobBt):
    print( "-----------------------------------------------------------------------------------------------------------------------------------------")
    print("|", "Clock: ", round(Clock, 2), "      ", "Evento: ", Tevent, "   ", "Ultimo Evento: ", round(TempoDoUltimoEvento, 2))
    print("|", "Servidor: ", round(servidor, 2), "           ", "Numero em fila: ", round(NumeroEmFila, 2))
    print("|", "                                                                                                                                    ", "|")
    print("|", "Fila: ")
    for l in Fila:
        print("| ", l)
    print("|", "                                                                                                                                    ", "|")
    print("|", "Proxima entrada: ", round(ListaEntrada[Entradas], 2), "", "Proxima saida: ", round(ListaSaida[Saidas], 2))
    print("|", "                                                                                                                                    ", "|")
    print("|", "                                                                                                                                    ", "|")
    print("|", "Clientes Atendidos: ", QtdeClientAtendidos, "|", "Espera Total: ", round(EsperaTotal, 2), "|", "Área sob Q(t): ", round(AreaSobQt, 2), "|", "Área sob B(t): ", round(AreaSobBt, 2))
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
def mostraClientes(Clientes):
    mostraC = input("mostrar lista de clientes? s/n: ")
    if mostraC == "s":
        print("Id", "Entrada", "Atraso", "Saida")
        cont = 1
        for c in Clientes:
            print(cont, "  ", round(c[0], 2), "  ", round(c[1], 2), "  ", round(c[2], 2))
            cont += 1
def mostraResultados(Clientes, numeroEmFila, Ca, AreaSobQt, AreaSobBt):
    TempoMedioEspera = 0
    NumeroMedioFila = 0
    semAtraso = 0
    ComAtraso = 0
    guarda = 0
    Porcnt = 0
    a = []
    for c in Clientes:
        TempoMedioEspera += c[1]
        if c[1] == 0.0 and c[0] != Clientes[0][0]:
            a.append(c[0] - guarda[2])
            Porcnt = (c[0] - guarda[2]) + Porcnt
            guarda = c
        else:
            guarda = c

    for c in Clientes:
        if c[1] == 0:
            semAtraso += 1
        else:
            ComAtraso += 1
    TempoMedioEspera = TempoMedioEspera/ComAtraso
    for n in numeroEmFila:
        NumeroMedioFila += n
    NumeroMedioFila = AreaSobQt/int(Ca)
    Porcnt = 100 - ((Porcnt * 100)/int(Ca))


    print("Tempo Média na fila: ", round(TempoMedioEspera, 2))
    print("Numero médio na fila", round(NumeroMedioFila, 2))
    print("numero de Clientes sem atraso: ", semAtraso)
    print("numero de clientes com atraso:", ComAtraso)
    print("Taxa de ocupação do servidor: ", round(Porcnt, 2), "%", "Calculo baseado em Regra de 3")


Rodando = True

while Rodando:
    MainProgram()
    continua = input("Fazer uma nova Simulação s/n: ")
    if continua != "s":
        Rodando = False

