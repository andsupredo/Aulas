class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def LogInfo(self, msg):
        self.write(f'Info: {msg}')

    def LogError(self, msg):
        self.write(f'ERROR: {msg}')

class ELetronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

class Smartphone(ELetronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = (f'{self._nome} não está ligado.')
            print(info)
            self.LogError(info)
            return

        if self._conectado:
            error = (f'{self._nome} já está conectado.')
            print(error)
            self.LogError(error)
            return

        info = f'{self._nome} agora está conectado.'
        print(info)
        self.LogInfo(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            print(error)
            self.LogError(error)
            return

        info = f'{self._nome} foi desligado com sucesso.'
        print(info)
        self.LogInfo(info)
        self._conectado = False