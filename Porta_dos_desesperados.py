import random
class Porta:
    def __init__(self):
        self.porta_premiada = self.escolhida_porta()
        self.porta_selecionada = None
        self.porta_removida = None

    def escolhida_porta(self):
        return random.randint(1,3)
    
    def porta_selecionar(self):
        self.porta_selecionada = self.escolhida_porta()

    def porta_remover(self):
        d = self.escolhida_porta()  
        while d == self.porta_selecionada or d == self.porta_premiada:
            d  = self.escolhida_porta()
        self.porta_removida = d    

    def mudar_escolha(self):
        self.porta_selecionada = 6 - self.porta_selecionada - self.porta_removida

    def ganha(self):
        if self.porta_selecionada == self.porta_premiada:
            return True
        else:
            return False

    def run_game(self, mudar=True):
        self.porta_selecionar()
        self.porta_remover()
        if mudar:
            self.mudar_escolha() 
        return self.ganha()


ganhou, perdeu = 0, 0
    
for i in range(10):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("10 jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(10):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("10 jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(100):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("100 jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(100):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("100 jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(200):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("200 jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(200):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("200 jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(500):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("500 jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(500):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("500 jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(1000):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("1 mil jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(1000):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("1 mil jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(5000):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("5 mil jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(5000):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("5 mil jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(10000):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("10 mil jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(10000):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("10 mil jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)
ganhou, perdeu = 0, 0
    
for i in range(50000):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("50 mil jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(50000):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("50 mil jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)
ganhou, perdeu = 0, 0
    
for i in range(100000):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("100 mil jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(100000):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("100 mil jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

ganhou, perdeu = 0, 0
    
for i in range(500000):
    m = Porta()
    if m.run_game(mudar=True):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("500 mil jogos (com mudanças):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias" % perc_ganhou)


ganhou, perdeu = 0, 0
for i in range(500000):
    m = Porta()
    if m.run_game(mudar=False):
        ganhou += 1
    else:
        perdeu += 1

perc_ganhou = 100.0*ganhou / (ganhou + perdeu)

print("500 mil jogos (com porta original):")
print("ganhou:", ganhou, "jogos")
print("perdeu",perdeu, "jogos")
print("probabilidades: %2.f%% porcentagem de vitórias\n" % perc_ganhou)

