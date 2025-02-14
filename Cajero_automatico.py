class Cajero:
    monto = 50000
    print('BEM-VINDO AO SEU CAIXA ELETRÔNICO FAVORITO DE CONFIANÇA')
    def Operaciones(self):
        self.opcion = int(input('''
        ________________________________________________
        POR FAVOR, INDIQUE QUAL OPERAÇÃO DESEJA REALIZAR..
        1. CONSULTAR SEU SALDO ATUAL.
        2. DEPOSITAR DINHEIRO NA SUA CONTA.
        3. RETIRAR DINHEIRO DA SUA CONTA.
        4. CANCELAR E FECHAR SESSÃO.'''))
        self.control=0
        while self.control==0:
            if self.opcion==1:
                self.consultabalance()
            elif self.opcion==2:
                self.depositar()
            elif self.opcion==3:
                self.retirar()
            elif self.opcion==4:
                self.control=1
                self.salir()
            else:
                print('OPÇÃO NÃO VÁLIDA. TENTE NOVAMENTE, POR FAVOR.')
                self.Operaciones()

    def consultabalance(self):
        print('SEU SALDO ATUAL NA CONTA É ', self.monto)
        print('DESEJA REALIZAR ALGUMA OUTRA OPERAÇÃO?')
        self.Operaciones()

    def depositar(self):
        self.deposito = int(input('POR FAVOR, INDIQUE A QUANTIA DE DINHEIRO A DEPOSITAR.'))
        self.monto = self.monto + self.deposito
        self.consultabalance()

    def retirar(self):
        self.retiro = int(input('POR FAVOR, INDIQUE A QUANTIA DE DINHEIRO A RETIRAR.'))
        self.control = 0
        while self.control == 0:
            if self.retiro>self.monto:
                print('''VOCÊ NÃO TEM ESSA QUANTIA DE DINHEIRO NA SUA CONTA.
                POR FAVOR, INGRESE UMA QUANTIA MENOR.
                _________________________________________________________''')
                self.retiro = int(input('POR FAVOR, INDIQUE A QUANTIA DE DINHEIRO A RETIRAR.'))
            elif self.retiro<=self.monto:
                self.monto=self.monto-self.retiro
                self.control=1
                print('QUANTIA RETIRADA:',self.retiro)
                self.consultabalance()

    def salir(self):
        print('===============================================')
        print('AGRADECEMOS POR USAR NOSSOS SERVIÇOS BANCÁRIOS.')
        print('===============================================')

ejecucion = Cajero()
ejecucion.Operaciones()