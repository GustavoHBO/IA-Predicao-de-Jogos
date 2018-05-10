class Estadio(object):
	"""docstring for Estadio"""

	idEstadio = 0

	def __init__(self, nome):
		super(Estadio, self).__init__()
		self.nome = nome
		self.id = idEstadio + 1
		