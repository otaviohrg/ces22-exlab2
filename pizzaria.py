class PizzaComponent:
	def getDescription(self):
		return self.__class__.__name__
	def getTotalCost(self):
		return self.__class__.cost

class Massa(PizzaComponent):
	cost = 15.0

class Decorator(PizzaComponent):
	def __init__(self, pizzaComponent):
		self.component = pizzaComponent

	def getTotalCost(self):
		return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

	def getDescription(self):
		return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)

class BordaCheddar(Decorator):
	cost = 4.0
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class BordaCatupiry(Decorator):
	cost = 2.0
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Pepperoni(Decorator):
	cost = 1.0
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Mussarela(Decorator):
	cost = 0.75
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Tomate(Decorator):
	cost = 0.5
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Bacon(Decorator):
	cost = 1.25
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Cebola(Decorator):
	cost = 0.75
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Brocolis(Decorator):
	cost = 1.25
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Milho(Decorator):
	cost = 0.5
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Frango(Decorator):
	cost = 1.5
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Lombo(Decorator):
	cost = 1.75
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Ovo(Decorator):
	cost = 2.00
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class Presunto(Decorator):
	cost = 1.75
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

class MolhoTomate(Decorator):
	cost = 1.00
	def __init__(self, pizzaComponent):
		Decorator.__init__(self, pizzaComponent)

portuguesa = BordaCatupiry(MolhoTomate(Cebola(Ovo(Tomate(Presunto(Mussarela(Massa())))))))
print(portuguesa.getDescription() + ": $" + str(portuguesa.getTotalCost()))
lombinho = BordaCheddar(MolhoTomate(Cebola(Lombo(Mussarela(Massa())))))
print(lombinho.getDescription() + ": $" + str(lombinho.getTotalCost()))
vegetariana = Mussarela(Tomate(Cebola(Brocolis(Milho(MolhoTomate(Massa()))))))
print(vegetariana.getDescription() + ": $" + str(vegetariana.getTotalCost()))
