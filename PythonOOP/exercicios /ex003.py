class ContaBancaria:
    """
    Cria uma conta bancária básica com depósitos, saques e transferências.
    """

    def __init__(self, id, nome, saldo):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print('Seja bem-vindo à sua nova conta na Express Agent! É um prazer recebê-lo!!!')
        print('_' * 90)
        print(f'Conta {self.id} bancária criada. Saldo atual: {self.saldo:,.2f} dólares.')

    def __str__(self):
        print('_' * 90)
        return f"A conta do ID {self.id} do titular {self.titular} possui saldo de {self.saldo:,.2f} dólares."

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de {valor:,.2f} dólares autorizado com sucesso!')
        else:
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print(f'Saque de {valor:,.2f} dólares efetuado com sucesso!')
                print(f'Saldo atual: {self.saldo:,.2f} dólares')
            else:
                print('Saldo insuficiente ou valor inválido!')

            # Testando a classe
        c1 = ContaBancaria(369, 'Victor Miguel', 5987580)
        print(c1)
        c1.sacar(150000)  # Valor mais realista para teste
        c1.depositar(5000)
        print(c1)
        print('Valor inválido para depósito!')

    def sacar(self, valor):
