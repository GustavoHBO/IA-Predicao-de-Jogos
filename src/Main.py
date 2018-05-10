from model.Partida import *
from model.TimeFutebol import *

class Main(object):
	"""docstring for Main"""

	listaTimes = []
	listaEstadios = []
	listaPartidas = []

	def __init__(self):
		super(Main, self).__init__()

		objeto = TimeFutebol("Vasco")
		objeto2 = TimeFutebol("Fluminense")
		Main.listaTimes.insert(1, objeto)
		Main.listaTimes.insert(2, objeto2)
		objeto3 = Main.listaTimes[1]
		print (objeto3.id)
		print (objeto3.nome)

executar = Main()