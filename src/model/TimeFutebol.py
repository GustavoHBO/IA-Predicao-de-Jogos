class TimeFutebol(object):
    """docstring for TimeFutebol"""

    idTime = 0

    def __init__(self, nome):
        super(TimeFutebol, self).__init__()
        TimeFutebol.idTime = TimeFutebol.idTime + 1
        self.id = TimeFutebol.idTime
        self.nome = nome
        