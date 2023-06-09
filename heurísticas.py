# -*- coding: utf-8 -*-
"""Heurísticas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10IEF6ja0H0A0DluUTi-CA-M4gB0LrqSf

Prática de Heurísticas Computacionais
"""

import random
import time

# Classe dos Jogadores
class Jogadores:
  def __init__(self, nome, aptidao, num_partidas):
    self.name = nome
    self.aptidao = aptidao
    self.num_partidas = num_partidas
  def getName(self):
    return self.name
  def getAptidao(self):
    return self.aptidao
  def getNumPartidas(self):
    return self.num_partidas

# Solução Inicial com objetos da classe Jogador
jogador1 = Jogadores('Lúcio', 3, 2)
jogador2 = Jogadores('Mauro', 5, 4)
jogador3 = Jogadores('Filho', 6, 2)
jogador4 = Jogadores('Luan', 9, 8)
jogador5 = Jogadores('Podeisso', 4, 2)
jogador6 = Jogadores('Arnaldo', 3, 4)
jogador7 = Jogadores('Ronaldo', 3, 3)
jogador8 = Jogadores('Neymar', 7, 6)
jogador9 = Jogadores('Theus', 5, 1)
jogador10 = Jogadores('Fenômeno', 8, 7)
TIME = [jogador1, jogador2, jogador3, jogador4, jogador5, jogador6, jogador7, jogador8, jogador9, jogador10]

# Classe responsavel por escalar os jogadores selecionados em binario
class Binario:
  def __init__(self):
    self._dados = []
  def atribuir_jogadores(self, lista_jogadores, solucao):
    self._indice = 0    
    for valor in solucao:
      self._dados.append([lista_jogadores[self._indice], valor])
      self._indice += 1
  def alterar_valores(self, indice, valor):
    del self._dados[indice][1]
    self._dados[indice].append(valor)
  def get_dados(self):
    return self._dados

# Solução Inicial em Binário
solucao_inicial = [0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
jogadores_selecionados = []
jogadores_nao_selecionados = []
solucao = Binario()
solucao.atribuir_jogadores(TIME, solucao_inicial)

# Apresenta o nome e se o jogador foi escalado ou não
# Insere em jogadores_selecionados os que foram escalados
def situacao_jogadores():
  print('\n--> Situacao dos Jogadores: \n')
  cont = 0
  a = solucao.get_dados()
  for i in a:
    print('Jogador:', i[0].getName(), '  \t | ', ' Escalado: ', i[1], '\n')  
    if i[1] == 1:
      jogadores_selecionados.append(i[0])
    cont+=1

class Controller: 
  def checar_totalPartidas(self, jogadores, penalidade):
    self._sum = 0
    self._aptidao = 0
    self._nome = " "
    for ind in jogadores:
      self._sum += ind.getNumPartidas()
      self._nome = self._nome + ind.getName()+", " 
      self._aptidao += ind.getAptidao()    
    # Caso a solucao tenha Penalidade (se o número de partidas for maior que 20)
    if(penalidade):
      return self.calcular_penalidade(self._sum, self._aptidao, self._nome)

    self.imprimir_info(self._nome, self._sum, self._aptidao)
    return self.checar_limitePartidas(self._sum, False)

  def calcular_penalidade(self, sum, aptidao, nome):    
    if(sum>20):     
      aptidao = aptidao - (aptidao * sum - 20)
      self.imprimir_info(nome, sum, aptidao)
      self.checar_limitePartidas(sum, True)      
    return [aptidao, sum]

  def imprimir_info(self, nome, total, aptidao):
    print('\n--> Jogadores Selecionados: ', nome)
    print('\n--> Total Partidas: ', total)    
    print('\n--> Aptidao: ', aptidao)

  def checar_limitePartidas(self, total, penalidade):
    texto = '\nLimite de Partidas Superior a 20 partidas \nNão é possível selecionar esses jogadores!'
    if penalidade:
      texto += 'A penalidade foi atribuida!'   
    if total > 20:
      print(texto)
      return False
    return True
util = Controller()

"""Heurística Construtiva Aleatória"""

# Heurística Construtiva de Busca Aleatoria para criar outra solucao inicial
def rand_key(): 
    s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    nums = []
    num1 = random.randint(0, 9)
    for i in range(0, 5):           
        num1 = random.randint(0, 9)
        while s[num1] == 1:
          num1 = random.randint(0, 9)
          # print('Posicao escolhida: ', num1)
        s[num1] = 1         
    return s
while True:
  # Variavel global sendo reiniciada
  jogadores_selecionados = []
  # Criando uma solucao inicial randomicamente em binario
  solucao_inicial=[]
  solucao_inicial = rand_key() 

  # Converter o numero binario gerado para a situacao dos jogadores existentes
  solucao = Binario()
  solucao.atribuir_jogadores(TIME, solucao_inicial)
  
  # Imprime as informações dos jogadores selecionados
  situacao_jogadores()

  util = Controller() 
  if util.checar_totalPartidas(jogadores_selecionados, False):
    print ("Finalizado")    
    break

"""Heurística de Refinamento de busca local utilizando o Método Best Improvement"""

# Gerando os Vizinhos
solucao_inicial = [0, 0, 0, 0, 1, 1, 0, 1, 1, 1]
def Vizinhos(solucao):     
    vetorSolucoes = []    
    for x in range(5):
      copySolucao = solucao.copy()
      ordemZero=0
      ordemUm=0
      valor = x + 1      
      for i,num in enumerate(copySolucao):
        if num == 0 :  
          ordemZero+=1
          if valor == ordemZero : 
            copySolucao[i] = 1 
        if num == 1:
          ordemUm+=1
          if valor == ordemUm : 
            copySolucao[i] = 0 
      vetorSolucoes.append(copySolucao)
    return vetorSolucoes
callVizinhos = Vizinhos(solucao_inicial)

# Faz a busca entre os vizinho da solução inicial e mostra a aptidão de cada um
# Mostra o melhor Vizinho(Maximo local) e sua aptidão

maximo_local = 0
for i in range (5):   
  jogadores_selecionados=[]
  solucao = Binario()
  solucao.atribuir_jogadores(TIME,callVizinhos[i])
  
  situacao_jogadores()
  
  aptidao_jogos = util.checar_totalPartidas(jogadores_selecionados, True)  
  
  if(aptidao_jogos[0] > maximo_local and aptidao_jogos[1]<=20):
    maximo_local = aptidao_jogos[0]
    best = callVizinhos[i]

print("\n\nMelhor Vizinho: ",(best))
print("Aptidão: ", maximo_local)

# Pega o maximo local encontrado, gera seus vizinhos e verifica se existe um novo maximo local
callVizinhos = Vizinhos(best)

maximo_localT = 0
for i in range (5):
  jogadores_selecionados=[]  
  solucao = Binario()
  solucao.atribuir_jogadores(TIME,callVizinhos[i])  
  situacao_jogadores()
  
  util=Controller()  
  
  aptidao_jogos = util.checar_totalPartidas(jogadores_selecionados, True)
  
  if(aptidao_jogos[0] > maximo_local and aptidao_jogos[1]<= 20):
    maximo_localT = aptidao_jogos[0]
    bestT = callVizinhos[i]

print("\n\nMelhor Vizinho: ",(bestT))
print("Aptidão: ",(maximo_localT))

# Pega o maximo local encontrado e gera seus vizinhos

callVizinhos = Vizinhos(bestT)
maximo_localJ = 0

for i in range (5): 
  jogadores_selecionados=[]  
  solucao = Binario()
  solucao.atribuir_jogadores(TIME,callVizinhos[i])
  situacao_jogadores()
  
  util=Controller()  
  aptidao_jogos = util.checar_totalPartidas(jogadores_selecionados, True)
  
  if(aptidao_jogos[0] > maximo_localJ and aptidao_jogos[1]<= 20):
    maximo_localJ = aptidao_jogos[0]
    bestJ = callVizinhos[i]

print("\n\nMelhor Vizinho: ",(bestJ))
print("Aptidão: ",(maximo_localJ))

# Mostra o maximo Local encontrado
if(maximo_localT > maximo_localJ):  
  print("O maximo local é" ,maximo_localT)