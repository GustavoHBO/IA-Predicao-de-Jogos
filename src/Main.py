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
		ano_base = 2003 
		qtn_anos = 15
		self.carregar_arquivo(caminhoBaseDados, ano_base, qtn_anos)
		
		time = self.buscar_time_nome("São Paulo")
		lista = self.buscar_partidas_ano(self.listaPartidas, 2017)
		lista = self.buscar_partidas_time(lista, time.id, 0)

		self.exibir_partidas(lista)

	def carregar_arquivo(self, caminho_base_dados, ano_base, qtn_anos):
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
		time = self.buscar_time_nome(nome_time)
		if time == None:
			self.id_times += 1
			novo_time = TimeFutebol(nome_time.upper(), self.id_times)
			Main.listaTimes.append(novo_time)
			return novo_time
		else :
			return time

	def buscar_time_nome(self, nome_time):
		for time in self.listaTimes:
			if time.nome == nome_time.upper():
				return time
		return None

	def buscar_time_id(self, id_time):
		for time in self.listaTimes:
			if time.id == id_time:
				return time
		return None

	def adicionar_estadio(self, nome_estadio):
		estadio = self.buscar_estadio_nome(nome_estadio)
		if estadio == None:
			self.id_estadio += 1
			estadio = Estadio(nome_estadio.upper(), self.id_estadio)
			self.listaEstadios.append(estadio)
		return estadio

	def buscar_estadio_nome(self, nome_stadio):
		for estadio in self.listaEstadios:
			if estadio.nome == nome_stadio.upper():
				return estadio
		return None

	def exibir_times(self, lista_times):
		for time in lista_times:
			print(time.nome)

	def exibir_partidas(self, lista_partidas):
		for partida in lista_partidas:
			print(partida.rodada +" "+ str(partida.dia) + "/" + str(partida.mes) + "/" + str(partida.ano) +" "+ self.buscar_time_id(partida.timeCasa).nome +" "+ partida.golsTimeCasa +" x "+ partida.golsTimeVisitante +" "+ self.buscar_time_id(partida.timeVisitante).nome)

	"""Retorna uma lista de partidas de determinado time. Busca igual a 0 retorna os jogos como mandante e como visitante, quando igual a 1 somente os jogos como mandante e quando 2 somente os jogos como visitante"""
	def buscar_partidas_time(self, lista_partidas, id_time, busca):
		lista = []
		for partida in lista_partidas:
			if partida.timeCasa == id_time and busca != 2:
				lista.append(partida)
			if partida.timeVisitante == id_time and busca != 1:
				lista.append(partida)
		return lista

	"""Retorna uma lista com as partidas em determinado ano"""
	def buscar_partidas_ano(self, lista_partidas, ano):
		lista = []
		for partida in lista_partidas:
			if partida.ano == ano:
				lista.append(partida)
		return lista

	def buscar_gols_time(self, lista_partidas, id_time):
		lista = []
		for partida in lista_partidas:
			if partida.time_casa == id_time:
				lista.append(partida.golsTimeCasa)
			if partida.time_visitante == id_time:
				lista.append(partida.golsTimeVisitante)
		return lista

executar = Main()