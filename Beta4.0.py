
from numpy import log as ln
import time


Sementes = []
Resultados = []
avanca = 0.5

from tkinter import *
class Application(Frame):

    def __init__(self):

        self.avanca = 0.8
        self.semSleep = False
        self.rapido = False

        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.geometry("550x460+500+200")

        self.a = StringVar()
        self.X0 = StringVar()
        self.c = StringVar()
        self.m = StringVar()

        self.Av = False
        self.Retro = False
        self.Prox = False
        self.An = False

        self.Vuni = []

        #calculo crongruente linear
        self.caixaDocalculo = Frame(self.master, borderwidth=0.5, relief="groove")
        self.caixaDocalculo.place(width=350, height=50, x=0, y=0)
        self.textoDocalculo = Label(self.caixaDocalculo, text="Calculo Congruente Linear")
        self.textoDocalculo.place(width=200, height=15, x=50, y=2)

        self.VariavelX0texto = Label(self.caixaDocalculo, text='x0')
        self.VariavelX0texto.place(width=15, height=15, x=15, y=30)
        self.VariavelX0 = Entry(self.caixaDocalculo, relief="groove", textvariable=self.X0)
        self.VariavelX0.place(width=35, height=15, x=30, y=30)

        self.VariavelAtexto = Label(self.caixaDocalculo, text='a')
        self.VariavelAtexto.place(width=15, height=15, x=80, y=30)
        self.VariavelA = Entry(self.caixaDocalculo, relief="groove", textvariable=self.a)
        self.VariavelA.place(width=35, height=15, x=95, y=30)

        self.VariavelCtexto = Label(self.caixaDocalculo, text='c')
        self.VariavelCtexto.place(width=15, height=15, x=145, y=30)
        self.VariavelC = Entry(self.caixaDocalculo, relief="groove", textvariable=self.c)
        self.VariavelC.place(width=35, height=15, x=160, y=30)

        self.VariavelMtexto = Label(self.caixaDocalculo, text='m')
        self.VariavelMtexto.place(width=15, height=15, x=210, y=30)
        self.VariavelM = Entry(self.master, relief="groove", textvariable=self.m)
        self.VariavelM.place(width=35, height=15, x=225, y=30)


        self.QuantSementes = Entry(self.master, font=('arial', 10, 'bold'))
        self.QuantSementes.place(width=10, height=15, x=270, y=29)
        self.Adicionar = Button(self.caixaDocalculo, text="+")
        self.Adicionar.place(width=17, height=17, x=280, y=28)
        self.Adicionar.bind('<Button-1>', self.texteQuiQuadradoMCL)

        self.Verificar = Button(self.caixaDocalculo, text=">")
        self.Verificar.place(width=40, height=17, x=298, y=28)
        #------------------------------------

        self.CaixaCalculoExponencial = Frame(self.master, borderwidth=0.5, relief="groove")
        self.CaixaCalculoExponencial.place(width=350, height=50, x=0, y=50)
        self.TextoCaixaCalculoExponencial = Label(self.CaixaCalculoExponencial, text='Exponencial')
        self.TextoCaixaCalculoExponencial.place(width=110, height=15, x=100, y=5)
        self.TextoVariavelinicial = Label(self.CaixaCalculoExponencial, text='Entrada:')
        self.TextoVariavelinicial.place(width=40, height=15, x=28, y=28)
        self.VariavelInicial = Entry(self.CaixaCalculoExponencial, relief="groove")
        self.VariavelInicial.place(width=40, height=15, x=72, y=30)
        self.TextoVariavelFinal = Label(self.CaixaCalculoExponencial, text='Atendimento')
        self.TextoVariavelFinal.place(width=110, height=15, x=128, y=28)
        self.VariavelFinal = Entry(self.CaixaCalculoExponencial, relief="groove")
        self.VariavelFinal.place(width=40, height=15, x=220, y=30)


        self.IniciarGeracao = Frame(self.master, borderwidth=0.5, relief="groove")
        self.IniciarGeracao.place(width=300, height=30, x=0, y=100)
        self.QuantiNumtexto = Label(self.IniciarGeracao, text='Tempo:')
        self.QuantiNumtexto.place(width=35, height=15, x=80, y=5)
        self.CaixaQuantiNum = Entry(self.IniciarGeracao, relief="groove")
        self.CaixaQuantiNum.place(width=40, height=15, x=120, y=7)
        self.botaoCriaLista = Label(self.IniciarGeracao, text="minutos", padx=0)
        self.botaoCriaLista.place(width=50, height=18, x=160, y=4)

        #---------------------------------------------------
        self.tm = StringVar()
        self.Timer = Label(self.master, text="Timer")
        self.Timer.place(width=60, height=25, x=10, y=140)
        self.ValorTimer = Label(self.master, textvariable=self.tm, relief="groove")
        self.ValorTimer.place(width=40, height=15, x=60, y=145)

        self.Ent = StringVar()
        self.Entrada = Label(self.master, text="Prox_Entrada")
        self.Entrada.place(width=70, height=25, x=110, y=140)
        self.ValorEntrada = Label(self.master, textvariable=self.Ent, relief="groove")
        self.ValorEntrada.place(width=40, height=15, x=185, y=145)

        self.Out = StringVar()
        self.Saida = Label(self.master, text="Prox_Saida")
        self.Saida.place(width=60, height=25, x=230, y=140)
        self.ValorSaida = Label(self.master, textvariable=self.Out, relief="groove")
        self.ValorSaida.place(width=40, height=15, x=295, y=145)
        #----------------------------------------------------

        self.f = StringVar()
        self.TextoFilaQuant = Label(self.master, text="Fila")
        self.TextoFilaQuant.place(width=50, height=20, x=10, y=370)
        self.FilaQuant = Label(self.master, textvariable=self.f, relief="groove")
        self.FilaQuant.place(width=50, height=15, x=10, y=390)

        self.Ca = StringVar()
        self.TextoClienteAtendidos = Label(self.master, text="C.atendidos")
        self.TextoClienteAtendidos.place(width=70, height=20, x=60, y=370)
        self.ClientesAtendidos = Label(self.master, textvariable=self.Ca, relief="groove")
        self.ClientesAtendidos.place(width=50, height=15, x=70, y=390)

        self.Te = StringVar()
        self.TextoTempoDeEspera = Label(self.master, text="T.espera")
        self.TextoTempoDeEspera.place(width=70, height=20, x=127, y=370)
        self.TempoDeEspera = Label(self.master, textvariable=self.Te, relief="groove")
        self.TempoDeEspera.place(width=50, height=15, x=137, y=390)

        self.Qt = StringVar()
        self.TextoAreaSobQt = Label(self.master, text="AreaSobQt")
        self.TextoAreaSobQt.place(width=70, height=20, x=190, y=370)
        self.AreaSobQt = Label(self.master, textvariable=self.Qt, relief="groove")
        self.AreaSobQt.place(width=50, height=15, x=200, y=390)


        self.Bt = StringVar()
        self.TextoAreaSobBt = Label(self.master, text="AreaSobBt")
        self.TextoAreaSobBt.place(width=70, height=20, x=260, y=370)
        self.AreaSobBt = Label(self.master,  relief="groove", textvariable=self.Bt)
        self.AreaSobBt.place(width=50, height=15, x=270, y=390)


        self.BotaoComecar = Button(self.master, text="Play")
        self.BotaoComecar.place(width=50, height=20, x=114, y=320)
        self.BotaoComecar.bind('<Button-1>', self.MainProgram)
        self.BotaoAvancar = Button(self.master, text=">")
        self.BotaoAvancar.place(width=30, height=20, x=164, y=320)
        self.BotaoAvancar.bind('<Button-1>', self.Avanca)
        self.BotaoRetroceder = Button(self.master, text="<")
        self.BotaoRetroceder.place(width=30, height=20, x=84, y=320)
        self.BotaoRetroceder.bind('<Button-1>', self.Desacerela)
        self.BotaoProximo = Button(self.master, text=">|")
        self.BotaoProximo.place(width=46, height=20, x=194, y=320)
        self.BotaoProximo.bind('<Button-1>', self.Proximo)
        self.BotaoAnterior = Button(self.master, text="|<")
        self.BotaoAnterior.place(width=46, height=20, x=38, y=320)


        self.TelaSimulacao = Frame(self.master, borderwidth=0.5, relief="sunken", bg='white')
        self.TelaSimulacao.place(width=200, height=150, x=40, y=170)

        self.Fila = Label(self.TelaSimulacao, bg='light gray')
        self.Fila.place(width=110, height=45, x=50, y=100)

        self.imagemPessoa = PhotoImage(file=r"dist/image/iconsCinza.png").subsample(3, 3)
        self.imagemPessoaGreen = PhotoImage(file=r"dist/image/iconsVerde.png").subsample(3, 3)
        self.imagemPessoaRed = PhotoImage(file=r"dist/image/iconsVermelho.png").subsample(3, 3)
        self.FilaAcento1 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento1.grid(column=0, row=0)
        self.FilaAcento2 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento2.grid(column=1, row=0)
        self.FilaAcento3 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento3.grid(column=2, row=0)
        self.FilaAcento4 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento4.grid(column=3, row=0)
        self.FilaAcento5 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento5.grid(column=4, row=0)
        self.FilaAcento6 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento6.grid(column=0, row=1)
        self.FilaAcento7 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento7.grid(column=1, row=1)
        self.FilaAcento8 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento8.grid(column=2, row=1)
        self.FilaAcento9 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento9.grid(column=3, row=1)
        self.FilaAcento10 = Label(self.Fila, image=self.imagemPessoa, bg='#9c9b9a')
        self.FilaAcento10.grid(column=4, row=1)

        self.PortaEntradaP = Label(self.TelaSimulacao, bg='#07fd3a', width=2, height=2)
        self.PortaEntradaP.place(x=0, y=50)
        self.PortaEntrada = Label(self.TelaSimulacao, bg='#07fd3a', image=self.imagemPessoaGreen, width=16, height=30)
        self.PortaEntrada.place(x=0, y=50)

        self.PortaSaidaP = Label(self.TelaSimulacao, bg='#f6101e', width=2, height=2)
        self.PortaSaidaP.place(x=179, y=50)
        self.PortaSaida = Label(self.TelaSimulacao, bg='#f6101e', image=self.imagemPessoaRed, width=20, height=30)
        self.PortaSaida.place(x=179, y=50)

        self.imagemPessoaM = PhotoImage(file=r"dist/image/iconsCinza.png").subsample(2, 2)
        self.sinalVerde = PhotoImage(file=r"dist/image/icons8-esfera-50verde.png").subsample(3, 3)
        self.sinalvermelho = PhotoImage(file=r"dist/image/icons8-esfera-50vermelha.png").subsample(3, 3)
        self.LocalAtendimento = Label(self.TelaSimulacao, bg="#9c9b9a")
        self.LocalAtendimento.place(width=50, height=45, x=75, y=20)
        self.Bacao = Label(self.TelaSimulacao, bg="#752400", relief="groove")
        self.Bacao.place(width=50, height=15, x=75, y=20)
        self.imagem = Label(self.LocalAtendimento, image=self.imagemPessoaM, bg='#9c9b9a', width=15, height=15)
        self.imagem.place(x=13, y=22)
        self.imagemStatus = Label(self.TelaSimulacao, image=self.sinalVerde, bg="white", width=15, height=15)
        self.imagemStatus.place(x=100, y=0)
        self.imagemStatus1 = Label(self.TelaSimulacao, image=self.sinalvermelho, bg="white", width=15, height=15)
        self.imagemStatus1.place(x=100, y=0)

        #--------------------------------------------------------------

        self.TextoHistorico = Label(self.master, text="Historico")
        self.TextoHistorico.place(width=50, height=15, x=270, y=170)
        self.Historico = Listbox(self.master, bg="white", relief="sunken")
        self.Historico.place(width=100, height=173, x=245, y=190)

        self.listadeNPAs = Listbox(self.master)
        self.listadeNPAs.place(width=200, height=500, x=350, y=0)

        self.TelaDeMensagem = Entry(self.master, relief="groove", bg='white')
        self.TelaDeMensagem.place(width=350, height=40, x=1, y=420)

    def texteQuiQuadradoMCL(self, event):
        self.listadeNPAs.delete(0, 1000)
        self.TelaDeMensagem.delete(0, 1000)

        X = int(self.VariavelX0.get())
        A = int(self.VariavelA.get())
        C = int(self.VariavelC.get())
        M = int(self.VariavelM.get())

        Npa = X
        count = 0
        Separador = [0, 0, 0, 0, 0]
        Lista = []

        while count <= 100:
            Npa = (Npa * A + C) % M
            N = Npa / (M - 1)
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

        quiQuadrado = ((Separador[0] - 20) ** 2) / 20 + ((Separador[1] - 20) ** 2) / 20 + ((Separador[2] - 20) ** 2) / 20 + ((Separador[3] - 20) ** 2) / 20 + (
                                  (Separador[4] - 20) ** 2) / 20
        if quiQuadrado < 9.49:
            self.QuantSementes.delete(0, str(len(Sementes)))
            self.TelaDeMensagem.insert(0, "Sua semente é valida")
            Sementes.append((X, A, C, M))
            self.QuantSementes.insert(0, str(len(Sementes)))
            count = 0
            for item in Lista:
                self.listadeNPAs.insert(count, item)
                count = count + 1

        else:
            self.TelaDeMensagem.insert(0, "Sua semente é invalida")
    def GeradorDeEntradas(self, Calculo):

        global linear
        linear = (Calculo[0] * Calculo[2] + Calculo[3]) % Calculo[4]
        if linear == 0:
            linear = (linear * Calculo[2] + Calculo[3]) % Calculo[4]
        Calculo[0] = linear
        linear = linear / (Calculo[4] - 1)
        linear = abs(ln(linear) * Calculo[5])

        return linear, Calculo
    def GeradorDeSaidas(self, Calculo):

        global linear

        linear = (Calculo[1] * Calculo[2] + Calculo[3]) % Calculo[4]
        if linear == 0:
            linear = (linear * Calculo[2] + Calculo[3]) % Calculo[4]
        Calculo[1] = linear
        linear = linear / (Calculo[4] - 1)
        linear = abs(ln(linear) * Calculo[6])

        return linear, Calculo

    def MainProgram(self, event):

        for s in Sementes:
            self.EsqueceTudo(s)

            calculo = [s[0], s[0], s[1], s[2], s[3], int(self.VariavelInicial.get()), float(self.VariavelFinal.get())]
            sla = self.GeradorDeEntradas(calculo)
            isso = self.GeradorDeSaidas(calculo)

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
            Historico = []

            ListaEntrada.append(sla[0])
            ListaSaida.append(0)

            Tevent = ""
            mostra = "s"

            while Clock <= int(self.CaixaQuantiNum.get()) or Cerao:

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
                            isso = self.GeradorDeSaidas(isso[1])

                        TempoDoUltimoEvento = Clock
                        Historico.append((round(TempoDoUltimoEvento, 2), Tevent))
                        Clock = ListaEntrada[Entradas]

                        ocioso = False

                        Atra.append(0)

                        sla = self.GeradorDeEntradas(sla[1])

                        if saida:
                            ListaSaida.append(isso[0] + Clock)
                            saida = False
                        else:
                            ListaSaida.append(isso[0] + Clock)
                            Saidas += 1
                            saida = False

                        Entradas += 1
                        ListaEntrada.append((Clock + sla[0]))

                        self.LembraEntrada()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Entrada do Cliente...")
                        if not self.rapido:
                            if not self.semSleep:
                                time.sleep(avanca)
                            self.master.update()


                        self.EsqueceEntrada()
                        if not self.rapido:
                            if not self.semSleep:
                                time.sleep(avanca)
                            self.master.update()

                        self.Ocupado()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Servidor Ocupado...")
                        if not self.rapido:
                            if not self.semSleep:
                                time.sleep(avanca)
                            self.master.update()



                    else:

                        TempoDoUltimoEvento = Clock
                        Historico.append((round(TempoDoUltimoEvento, 2), Tevent))
                        Clock = ListaEntrada[Entradas]

                        Fila.append(Clock)
                        NumeroEmFila += 1

                        sla = self.GeradorDeEntradas(sla[1])

                        Entradas += 1
                        ListaEntrada.append((Clock + sla[0]))

                        AreaSobQt = AreaSobQt + NumeroEmFila * (Clock - TempoDoUltimoEvento)
                        AreaSobBt = AreaSobBt + servidor * (Clock - TempoDoUltimoEvento)

                        self.LembraEntrada()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Entrada do Cliente")
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)
                        self.EsqueceEntrada()
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)

                else:
                    if NumeroEmFila == 0:

                        TempoDoUltimoEvento = Clock
                        Historico.append((round(TempoDoUltimoEvento, 2), Tevent))
                        Clock = ListaSaida[Saidas]

                        Clientes.append((round(ListaEntrada[contCliente], 2), round(Atra[contCliente], 2),
                                         round(ListaSaida[contCliente], 2)))
                        contCliente += 1

                        AreaSobBt = AreaSobBt + servidor * (Clock - TempoDoUltimoEvento)

                        QtdeClientAtendidos += 1

                        ListaSaida.append(0)
                        Saidas += 1

                        ocioso = True

                        self.Livre()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Servidor Livre...")
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)
                        self.LembraSaida()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Saida do Cliente...")
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)
                        self.EsqueceSaida()
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)


                    else:

                        TempoDoUltimoEvento = Clock
                        Historico.append((round(TempoDoUltimoEvento, 2), Tevent))
                        Clock = ListaSaida[Saidas]

                        Clientes.append((round(ListaEntrada[contCliente], 2), round(Atra[contCliente], 2),
                                         round(ListaSaida[contCliente], 2)))
                        contCliente += 1

                        AreaSobQt = AreaSobQt + NumeroEmFila * (Clock - TempoDoUltimoEvento)

                        QtdeClientAtendidos += 1

                        Atra.append(Clock - Fila[0])
                        Fila.pop(0)
                        NumeroEmFila -= 1

                        isso = self.GeradorDeSaidas(isso[1])
                        Saidas += 1
                        ListaSaida.append(isso[0] + Clock)

                        self.Livre()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Sevidor Livre...")
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)
                        self.LembraSaida()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Saida do Cliente...")
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)
                        self.EsqueceSaida()
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)
                        self.Ocupado()
                        self.TelaDeMensagem.delete(0, 1000)
                        self.TelaDeMensagem.insert(0, "Servidor Ocupado...")
                        if not self.rapido:
                            self.master.update()
                            if not self.semSleep:
                                time.sleep(avanca)

                for atrasos in Atra:
                    espera = espera + atrasos
                EsperaTotal = espera
                espera = 0

                if ocioso:
                    servidor = 0
                else:
                    servidor = 1

                self.AtualizaFila(NumeroEmFila)
                self.TelaDeMensagem.delete(0, 1000)
                self.TelaDeMensagem.insert(0, "Atualizando Fila...")
                if not self.rapido:
                    self.master.update()
                    if not self.semSleep:
                        time.sleep(avanca)

                if not self.rapido:
                    self.master.update()
                    self.tm.set(round(Clock, 2))
                    self.Ent.set(round(ListaEntrada[Entradas], 2))
                    self.Out.set(round(ListaSaida[Saidas], 2))
                    self.Te.set(round(EsperaTotal, 2))
                    self.Qt.set(round(AreaSobQt, 2))
                    self.Bt.set(round(AreaSobBt, 2))
                    self.Ca.set(str(QtdeClientAtendidos))
                    self.f.set(str(NumeroEmFila))

                    self.Historico.delete(0, 1000)
                    cont = 1
                    for h in Historico:
                        self.Historico.insert(cont, h)
                        cont += 1

                    self.listadeNPAs.delete(0, 1000)
                    self.listadeNPAs.insert(0, "Id  Entrada  Atraso  Saida")
                    cont = 1
                    for c in Clientes:
                        self.listadeNPAs.insert(cont, c)
                        cont += 1
                    self.master.update()

                Cerao = self.DepoisDoEspediente(Clock, NumeroEmFila, self.CaixaQuantiNum.get())

            if self.rapido:
                self.master.update()
                self.tm.set(round(Clock, 2))
                self.Ent.set(round(ListaEntrada[Entradas], 2))
                self.Out.set(round(ListaSaida[Saidas], 2))
                self.Te.set(round(EsperaTotal, 2))
                self.Qt.set(round(AreaSobQt, 2))
                self.Bt.set(round(AreaSobBt, 2))
                self.Ca.set(str(QtdeClientAtendidos))
                self.f.set(str(NumeroEmFila))

                self.Historico.delete(0, 1000)
                cont = 1
                for h in Historico:
                    self.Historico.insert(cont, h)
                    cont += 1

                self.listadeNPAs.delete(0, 1000)
                self.listadeNPAs.insert(0, "Id  Entrada  Atraso  Saida")
                cont = 1
                for c in Clientes:
                    self.listadeNPAs.insert(cont, c)
                    cont += 1
                self.master.update()


            self.mostraResultados(Clientes, self.CaixaQuantiNum.get(), AreaSobQt, AreaSobBt, QtdeClientAtendidos, Clock)
        self.ResultadoFinal()
    def DepoisDoEspediente(self, Clock, NumeroEmFila, Ca):
        if Clock >= int(Ca):
            if NumeroEmFila == 0:
                return False
            else:
                return True
        else:
            return False

    def mostraResultados(self ,Clientes, Ca, AreaSobQt, AreaSobBt, QtdeClientAtendidos, Clock):
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

        TempoMedioEspera = TempoMedioEspera / ComAtraso
        NumeroMedioFila = AreaSobQt / int(Ca)
        Porcnt = 100 - ((Porcnt * 100) / int(Ca))

        Resultados.append((round(TempoMedioEspera, 2), round(NumeroMedioFila, 2), round(Porcnt, 2), semAtraso, ComAtraso, QtdeClientAtendidos, round(Clock, 2)))
    def ResultadoFinal(self):

        resultado = Toplevel(self.master)
        cont = 1

        TE = 0
        NF = 0
        Por = 0
        SA = 0
        CS = 0
        CA = 0
        TM = 0

        self.Linha = Label(resultado, relief="groove", width=75, height=2)
        self.Linha.grid(row=0, column=0)
        self.C = Label(self.Linha, text="Semente")
        self.C.place(width=70, height=20, x=3, y=0)
        self.TM = Label(self.Linha, text="Esp.Média")
        self.TM.place(width=70, height=20, x=75, y=0)
        self.NM = Label(self.Linha, text="Fila.Média")
        self.NM.place(width=70, height=20, x=150, y=0)
        self.Por = Label(self.Linha, text="Ocupação")
        self.Por.place(width=70, height=20, x=225, y=0)
        self.SA = Label(self.Linha, text="Atraso")
        self.SA.place(width=70, height=20, x=300, y=0)
        self.CA = Label(self.Linha, text="SemAtraso")
        self.CA.place(width=70, height=20, x=375, y=0)
        self.QT = Label(self.Linha, text="C.Atendidos")
        self.QT.place(width=70, height=20, x=450, y=0)
        self.CK = Label(self.Linha, text="Tempo")
        self.CK.place(width=70, height=20, x=525, y=0)

        for r in Resultados:
            self.Linha = Label(resultado, relief="groove", width=75, height=2)
            self.Linha.grid(row=cont, column=0)
            self.C = Label(self.Linha, text=cont)
            self.C.place(width=27, height=20, x=10, y=0)
            self.TM = Label(self.Linha, text=r[0])
            self.TM.place(width=27, height=20, x=90, y=0)
            self.NM = Label(self.Linha, text=r[1])
            self.NM.place(width=27, height=20, x=165, y=0)
            self.Por = Label(self.Linha, text=r[2])
            self.Por.place(width=27, height=20, x=240, y=0)
            self.SA = Label(self.Linha, text=r[3])
            self.SA.place(width=27, height=20, x=315, y=0)
            self.CA = Label(self.Linha, text=r[4])
            self.CA.place(width=30, height=20, x=390, y=0)
            self.QT = Label(self.Linha, text=r[5])
            self.QT.place(width=30, height=20, x=465, y=0)
            self.CK = Label(self.Linha, text=r[6])
            self.CK.place(width=30, height=20, x=540, y=0)
            cont += 1

            TE = r[0] + TE
            NF = r[1] + NF
            Por = r[2] + Por
            SA = r[3] + SA
            CS = r[4] + CS
            CA = r[5] + CA
            TM = r[6] + TM

        self.Linha = Label(resultado, relief="groove", width=75, height=2)
        self.Linha.grid(row=cont, column=0)

        self.media = Label(self.Linha, text="Média:")
        self.media.place(width=60, height=20, x=5, y=0)
        self.TM = Label(self.Linha, text=round(TE/len(Resultados), 2))
        self.TM.place(width=27, height=20, x=90, y=0)
        self.NM = Label(self.Linha, text=round(NF/len(Resultados), 2))
        self.NM.place(width=27, height=20, x=165, y=0)
        self.Por = Label(self.Linha, text=round(Por/len(Resultados), 2))
        self.Por.place(width=27, height=20, x=240, y=0)
        self.SA = Label(self.Linha, text=round(SA/len(Resultados), 2))
        self.SA.place(width=27, height=20, x=315, y=0)
        self.CA = Label(self.Linha, text=round(CS/len(Resultados), 2))
        self.CA.place(width=32, height=20, x=390, y=0)
        self.QT = Label(self.Linha, text=round(CA/len(Resultados), 2))
        self.QT.place(width=32, height=20, x=465, y=0)
        self.CK = Label(self.Linha, text=round(TM/len(Resultados), 2))
        self.CK.place(width=32, height=20, x=540, y=0)

    def EsqueceTudo(self, s):
        self.FilaAcento10.grid_forget()
        self.FilaAcento9.grid_forget()
        self.FilaAcento8.grid_forget()
        self.FilaAcento7.grid_forget()
        self.FilaAcento6.grid_forget()
        self.FilaAcento5.grid_forget()
        self.FilaAcento4.grid_forget()
        self.FilaAcento3.grid_forget()
        self.FilaAcento2.grid_forget()
        self.FilaAcento1.grid_forget()
        self.PortaEntrada.place_forget()
        self.PortaSaida.place_forget()
        self.imagem.place_forget()

        self.tm.set("0")
        self.Ent.set("0")
        self.Out.set("0")
        self.Te.set("0")
        self.Qt.set("0")
        self.Bt.set("0")
        self.Ca.set("0")
        self.f.set("0")

        self.Historico.delete(0, 1000)
        self.listadeNPAs.delete(0, 1000)
        self.TelaDeMensagem.delete(0, 1000)

        self.X0.set(s[0])
        self.a.set(s[1])
        self.c.set(s[2])
        self.m.set(s[3])

        self.master.update()
        time.sleep(0.8)
    def AtualizaFila(self, NumEmFila):
        self.FilaAcento10.grid_forget()
        self.FilaAcento9.grid_forget()
        self.FilaAcento8.grid_forget()
        self.FilaAcento7.grid_forget()
        self.FilaAcento6.grid_forget()
        self.FilaAcento5.grid_forget()
        self.FilaAcento4.grid_forget()
        self.FilaAcento3.grid_forget()
        self.FilaAcento2.grid_forget()
        self.FilaAcento1.grid_forget()

        if NumEmFila == 1:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
            self.FilaAcento7.grid_forget()
            self.FilaAcento6.grid_forget()
            self.FilaAcento5.grid_forget()
            self.FilaAcento4.grid_forget()
            self.FilaAcento3.grid_forget()
            self.FilaAcento2.grid_forget()
        elif NumEmFila == 2:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
            self.FilaAcento7.grid_forget()
            self.FilaAcento6.grid_forget()
            self.FilaAcento5.grid_forget()
            self.FilaAcento4.grid_forget()
            self.FilaAcento3.grid_forget()
        elif NumEmFila == 3:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
            self.FilaAcento7.grid_forget()
            self.FilaAcento6.grid_forget()
            self.FilaAcento5.grid_forget()
            self.FilaAcento4.grid_forget()
        elif NumEmFila == 4:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
            self.FilaAcento7.grid_forget()
            self.FilaAcento6.grid_forget()
            self.FilaAcento5.grid_forget()
        elif NumEmFila == 5:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento5.grid(column=4, row=0)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
            self.FilaAcento7.grid_forget()
            self.FilaAcento6.grid_forget()
        elif NumEmFila == 6:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento5.grid(column=4, row=0)
            self.FilaAcento6.grid(column=0, row=1)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
            self.FilaAcento7.grid_forget()
        elif NumEmFila == 7:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento5.grid(column=4, row=0)
            self.FilaAcento6.grid(column=0, row=1)
            self.FilaAcento7.grid(column=1, row=1)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
            self.FilaAcento8.grid_forget()
        elif NumEmFila == 8:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento5.grid(column=4, row=0)
            self.FilaAcento6.grid(column=0, row=1)
            self.FilaAcento7.grid(column=1, row=1)
            self.FilaAcento8.grid(column=2, row=1)
            self.FilaAcento10.grid_forget()
            self.FilaAcento9.grid_forget()
        elif NumEmFila == 9:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento5.grid(column=4, row=0)
            self.FilaAcento6.grid(column=0, row=1)
            self.FilaAcento7.grid(column=1, row=1)
            self.FilaAcento8.grid(column=2, row=1)
            self.FilaAcento9.grid(column=3, row=1)
            self.FilaAcento10.grid_forget()
        elif NumEmFila == 10:
            self.FilaAcento1.grid(column=0, row=0)
            self.FilaAcento2.grid(column=1, row=0)
            self.FilaAcento3.grid(column=2, row=0)
            self.FilaAcento4.grid(column=3, row=0)
            self.FilaAcento5.grid(column=4, row=0)
            self.FilaAcento6.grid(column=0, row=1)
            self.FilaAcento7.grid(column=1, row=1)
            self.FilaAcento8.grid(column=2, row=1)
            self.FilaAcento9.grid(column=3, row=1)
            self.FilaAcento10.grid(column=4, row=1)
    def EsqueceEntrada(self):
        self.PortaEntrada.place_forget()
    def LembraEntrada(self):
        self.PortaEntrada.place(x=0, y=50)
    def EsqueceSaida(self):
        self.PortaSaida.place_forget()
    def LembraSaida(self):
        self.PortaSaida.place(x=179, y=50)
    def Ocupado(self):
        self.imagemStatus.place_forget()
        self.imagemStatus1.place(x=100, y=0)
        self.imagem.place(x=13, y=22)
    def Livre(self):
        self.imagemStatus1.place_forget()
        self.imagem.place_forget()
        self.imagemStatus.place(x=100, y=0)

    def Proximo(self, event):
        self.rapido = True
    def Avanca(self, event):
        self.avanca = 0
    def Desacerela(self, event):
        self.avanca = 0.5


Application().mainloop()