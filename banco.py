from abc import ABC, abstractmethod

class Action(ABC): #Command

	@abstractmethod
	def execute(self):
		pass


class WithdrawAction(Action): #ConcreteCommand

	def __init__(self, account, value):
		self.account = account
		self.value = value

	def execute(self):
		self.account.withdraw(self.value)


class DepositAction(Action): #ConcreteCommand

	def __init__(self, account, value):
		self.account = account
		self.value = value

	def execute(self):
		self.account.deposit(self.value)


class TransferAction(Action): #ConcreteCommand

	def __init__(self, account, destination, value):
		self.account = account
		self.destination = destination
		self.value = value

	def execute(self):
		self.account.transfer(self.destination, self.value)


class BalanceAction(Action): #ConcreteCommand

	def __init__(self, account):
		self.account = account

	def execute(self):
		self.account.balance()


class ExtractAction(Action): #ConcreteCommand

	def __init__(self, account):
		self.account = account

	def execute(self):
		self.account.extract()


class AccountManager: #Receiver

	def deposit(self, value):
		print("You will deposit $" + str(value) + ".")

	def withdraw(self, value):
		print("You will withdraw $" + str(value) + ".")

	def balance(self):
		print("You will check your balance.")

	def extract(self):
		print("You will receive a extract of your account.")

	def transfer(self, destination, value):
		print("You will transfer $" + str(value) + " to account " + destination +".")

class Bank: #Invoker

	def __init__(self):
		self.__order_queue = []

	def place_order(self, order):
		self.__order_queue.append(order)

	def execute_order(self):
		order = self.__order_queue.pop(0)
		order.execute()

	def execute_all(self):
		while(len(self.__order_queue)):
			self.execute_order()


#Cliente
Conta = AccountManager()
deposito1 = DepositAction(Conta, 100)
deposito2 = DepositAction(Conta, 535)
saque1 = WithdrawAction(Conta, 200)
saque2 = WithdrawAction(Conta, 15)
pix1 = TransferAction(Conta, "12.345-0", 20)
pix2 = TransferAction(Conta, "12.121-2", 150)
extrato = ExtractAction(Conta)
saldo = BalanceAction(Conta)

#Invoker
Banco = Bank()
Banco.place_order(deposito1)
Banco.place_order(deposito2)
Banco.place_order(saque1)
Banco.place_order(saque2)
Banco.place_order(pix1)
Banco.place_order(pix2)
Banco.place_order(extrato)
Banco.place_order(saldo)
Banco.execute_all()