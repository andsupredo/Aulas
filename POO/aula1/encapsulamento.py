'''
public, protected, private
'''

class BaseDeDados:

    def __init__(self):
        self._dados = {} #público

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados['clientes'] = {id: nome}
        else:
            self._dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self._dados['clientes'][id]

bd = BaseDeDados()
bd.inserir_cliente(1, 'Anderson')
bd.inserir_cliente(2, 'Pedro')
bd.inserir_cliente(3, 'Barbosa')
bd.lista_clientes()

#Convenção de python: 1 undeline é private fraco (ñ usar) e 2 underline é private frote (ñ utilizável)