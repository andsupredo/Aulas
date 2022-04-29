from associação import Caneta
from associação import Escritor
from associação import MaquinaDeEscrever

escritor = Escritor('Freire')
caneta = Caneta('BIC')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()