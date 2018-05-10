class Partida(object):
	"""docstring for Partida"""
	def __init__(self, timeCasa, golsTimeCasa, golsTimeVisitante, timeVisitante, rodada, stadio, data):
		super(Partida, self).__init__()
		self.timeCasa = timeCasa
		self.golsTimeCasa = golsTimeCasa
		self.timeVisitante = timeVisitante
		self.golsTimeVisitante = golsTimeVisitante
		self.rodada = rodada
		self.data = data