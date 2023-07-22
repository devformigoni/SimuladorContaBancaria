### Program developed by Prof. MSc. Paulo O. Formigoni, Ph.D and Sc.D ###
### profpauloformigoni@gmail.com ###


class ContaBancaria: # definindo a classe ContaBancaria, que representa uma conta bancária.
    def __init__(self, nome_titular, saldo_inicial=0):
        #O método especial __init__ é o construtor da classe, que é chamado automaticamente
        #quando um objeto da classe é criado. Ele inicializa os atributos da classe. self é
        #uma referência ao próprio objeto sendo criado. nome_titular e saldo_inicial
        #são parâmetros do construtor.
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        #atribuindo os valores dos parâmetros nome_titular e saldo_inicial aos atributos
        #self.nome_titular e self.saldo, respectivamente.

    def depositar(self, valor):
        #definindo o método depositar, que permite ao titular da conta depositar dinheiro
        #na conta. self é usado novamente para referenciar o objeto atual.
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        #estamos adicionando o valor depositado ao saldo da conta (self.saldo += valor)
        #e imprimindo uma mensagem informando o valor depositado e o saldo atual da conta.

    def sacar(self, valor):
        #definindo o método sacar, que permite ao titular da conta sacar dinheiro da conta.
        #Mais uma vez, self é usado para referenciar o objeto atual.
        if self.saldo >= valor:
            #verificamos se o saldo atual da conta (self.saldo) é maior ou igual ao valor
            #que o titular deseja sacar.
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
            #Se o saldo for suficiente para o saque, subtraímos o valor do saldo (self.saldo -= valor)
            #e imprimimos uma mensagem informando o valor sacado e o novo saldo.
        else:
            print("Saldo insuficiente. Operação de saque não realizada.")
            #Caso o saldo não seja suficiente para o saque, imprimimos uma mensagem
            #informando que a operação de saque não pode ser realizada.

    def verificar_saldo(self):
        #definindo o método verificar_saldo, que permite ao titular da conta verificar
        #o saldo atual. self é usado para referenciar o objeto atual.
        print(f"Saldo atual da conta: R${self.saldo:.2f}")
        # imprimimos uma mensagem mostrando o saldo atual da conta.


def main():
    #definimos a função main, que será responsável por executar o programa e interagir com o usuário.
    print("Bem-vindo ao Simulador de Conta Bancária!")
    nome_titular = input("Digite o nome do titular da conta: ")
    conta = ContaBancaria(nome_titular)
    #exibimos uma mensagem de boas-vindas e solicitamos ao usuário que digite o nome do titular da conta.
    #Em seguida, criamos um objeto conta da classe ContaBancaria, passando o nome do titular como argumento
    #para o construtor.

    while True:
        #estamos iniciando um loop infinito para manter o programa em execução
        #até que o usuário escolha sair.
        print("\nOpções:")
        print("1 - Depositar dinheiro")
        print("2 - Sacar dinheiro")
        print("3 - Verificar saldo")
        print("4 - Sair")
        #opções disponíveis para o usuário

        opcao = input("Digite o número da opção desejada: ")
        #solicitamos ao usuário que digite o número da opção desejada.

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor_deposito)
            #Se o usuário escolher a opção 1, pedimos o valor a ser depositado e
            #chamamos o método depositar da classe ContaBancaria.

        elif opcao == "2":
            valor_saque = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor_saque)
            #Se o usuário escolher a opção 2, pedimos o valor a ser sacado e chamamos o
            #método sacar da classe ContaBancaria.

        elif opcao == "3":
            conta.verificar_saldo()
            #Se o usuário escolher a opção 3, chamamos o método verificar_saldo da classe ContaBancaria.

        elif opcao == "4":
            print("Obrigado por utilizar o Simulador de Conta Bancária. Volte sempre!")
            break
            #Se o usuário escolher a opção 4, exibimos uma mensagem de despedida e saímos
            #do loop infinito usando break, encerrando o programa.

        else:
            print("Opção inválida. Digite novamente.")
            #Se o usuário digitar uma opção inválida, exibimos uma mensagem de erro e o loop continuará.


if __name__ == "__main__":
    main()
    #verificamos se o programa está sendo executado como um script principal
    #(__name__ == "__main__") e chamamos a função main() para iniciar a execução do programa.






