class Partida(object):
	"""docstring for Partida"""
	def __init__(self, timeCasa, golsTimeCasa, golsTimeVisitante, timeVisitante, rodada, stadio, data):
		super(Partida, self).__init__()
		self.timeCasa = timeCasa
		self.golsTimeCasa = golsTimeCasa
		self.timeVisitante = timeVisitante
		self.golsTimeVisitante = golsTimeVisitante
		self.rodada = rodada
		data_dividida = data.split("/")
		self.ano = int(data_dividida[2])
		self.mes = int(data_dividida[1])
		self.dia = int(data_dividida[0])