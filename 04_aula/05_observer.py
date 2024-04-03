class Mensageiro:
    def __init__(self):
        self.observadores = []

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def remover_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, remetente, mensagem):
        for observador in self.observadores:
            observador.receber_notificacao(remetente, mensagem)


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def receber_notificacao(self, remetente, mensagem):
        print(f"[{self.nome}] Nova mensagem de {remetente}: {mensagem}")


class Grupo:
    def __init__(self, nome):
        self.nome = nome
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def receber_notificacao(self, remetente, mensagem):
        print(f"Grupo {self.nome}: Nova mensagem de {remetente}: {mensagem}")


mensageiro = Mensageiro()

# Criando usuários
usuario1 = Usuario("Alice")
usuario2 = Usuario("Bob")
usuario3 = Usuario("Charlie")

# Criando grupos
grupo1 = Grupo("Família")
grupo2 = Grupo("Trabalho")

# Adicionando observadores ao mensageiro
mensageiro.adicionar_observador(usuario1)
mensageiro.adicionar_observador(usuario2)
mensageiro.adicionar_observador(usuario3)

# Adicionando membros ao grupo
grupo1.adicionar_membro(usuario1)
grupo1.adicionar_membro(usuario2)

grupo2.adicionar_membro(usuario2)
grupo2.adicionar_membro(usuario3)

# Enviando mensagens
mensageiro.notificar_observadores("Admin", "Bem-vindos ao nosso aplicativo de mensagens!")
grupo1.receber_notificacao("Admin", "Nova reunião marcada para amanhã.")
usuario3.receber_notificacao("Alice", "Oi, tudo bem?")
