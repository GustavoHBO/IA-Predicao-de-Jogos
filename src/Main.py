from model.Partida import Partida
from model.TimeFutebol import TimeFutebol
from model.Estadio import Estadio

class Main(object):
	"""docstring for Main"""

	id_times = 0
	id_estadio = 0

	listaTimes = []
	listaEstadios = []
	listaPartidas = []

	def __init__(self):
		super(Main, self).__init__()

		caminhoBaseDados = "./base_de_dados/"
		self.carregar_arquivo(caminhoBaseDados)

	def carregar_arquivo(self, caminho_base_dados):
		ano_base = 2003
		qtn_anos = 15
		for ano in range(ano_base, ano_base+qtn_anos):
			nome_arquivo = caminho_base_dados + str(ano) + "[formated].txt"
			arquivo = open(nome_arquivo, "r")
			texto_arquivo = arquivo.readlines()
			for linha in texto_arquivo:
				partida_linha = linha.split("\t")
				time_casa = self.adicionar_time(partida_linha[3])
				time_visitante = self.adicionar_time(partida_linha[7])
				estadio = self.adicionar_estadio(partida_linha[8])
				partida = Partida(time_casa.id, partida_linha[4], partida_linha[6], time_visitante.id, 
				partida_linha[0], estadio.id, partida_linha[1])
				self.listaPartidas.append(partida)

	def adicionar_time(self, nome_time):
		time = self.buscar_time(nome_time)
		if time == None:
			self.id_times += 1
			novo_time = TimeFutebol(nome_time.upper(), self.id_times)
			Main.listaTimes.append(novo_time)
			return novo_time
		else :
			return time

	def buscar_time(self, nome_time):
		for time in self.listaTimes:
			if time.nome == nome_time.upper():
				return time
		return None

	def adicionar_estadio(self, nome_estadio):
		estadio = self.buscar_estadio(nome_estadio)
		if estadio == None:
			self.id_estadio += 1
			estadio = Estadio(nome_estadio.upper(), self.id_estadio)
			self.listaEstadios.append(estadio)
		return estadio

	def buscar_estadio(self, nome_stadio):
		for estadio in self.listaEstadios:
			if estadio.nome == nome_stadio.upper():
				return estadio
		return None

	def exibir_times(self):
		for time in self.listaTimes:
			print(time.nome)

executar = Main()