from semafaro import *


gerenciador = Ciclo()


tempo_verde = input("tempo verde: ")

tempo_laranja = input("tempo laranja: ")

tempo_vermelho = input("tempo vermelho: ")


Ciclo.tempo(gerenciador.semaforo, tempo_verde, tempo_laranja, tempo_vermelho)


ciclo = int(input("quantos ciclos voce deseja realizar?"))


gerenciador.percorrendo(ciclo)
