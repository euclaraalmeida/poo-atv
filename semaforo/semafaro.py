class Ciclo:

    def __init__(self):

        self.semaforo = []

    @staticmethod
    def tempo(semaforo, verde, laranja, vermelho):

        # Adiciona os tempos de cada cor como um dicionário na lista de semáforos

        semaforo.append({"verde": verde, "laranja": laranja, "vermelho": vermelho})

    def percorrendo(self, ciclo):

        if not self.semaforo:

            print("Nenhum semáforo foi adicionado!")

        for i in range(ciclo):

            for cores in self.semaforo:
                print()

                print(f"{i + 1}° ciclo")

                print(
                    f"Verde: {cores['verde']}\nlaranja:{cores['laranja']}\nVermelho:{cores['vermelho']}"
                )
