# Importando bibliotecas necessárias
import datetime

class Hamburgueria:
    def __init__(self):
        self.setores = {
            "cozinha": {"checklist": [], "deadline": None},
            "delivery": {"checklist": [], "deadline": None},
            "salao": {"checklist": [], "deadline": None},
            "limpeza": {"checklist": [], "deadline": None},
            "estoque": {"checklist": [], "deadline": None},
            "compras": {"checklist": [], "deadline": None},
            "financeiro": {"checklist": [], "deadline": None},
            "mkt": {"checklist": [], "deadline": None}
        }

    def adicionar_item(self, setor, item):
        if setor in self.setores:
            self.setores[setor]["checklist"].append(item)
        else:
            print(f"Erro: Setor '{setor}' não existe.")

    def remover_item(self, setor, item):
        if setor in self.setores:
            if item in self.setores[setor]["checklist"]:
                self.setores[setor]["checklist"].remove(item)
            else:
                print(f"Erro: Item '{item}' não existe no setor '{setor}'.")
        else:
            print(f"Erro: Setor '{setor}' não existe.")

    def imprimir_checklist(self, setor=None):
        if setor is None:
            for s in self.setores:
                print(f"Checklist do setor {s}:")
                for item in self.setores[s]["checklist"]:
                    print(item)
                if self.setores[s]["deadline"] is not None:
                    print(f"Deadline: {self.setores[s]['deadline']}")
                print()
        else:
            if setor in self.setores:
                print(f"Checklist do setor {setor}:")
                for item in self.setores[setor]["checklist"]:
                    print(item)
                if self.setores[setor]["deadline"] is not None:
                    print(f"Deadline: {self.setores[setor]['deadline']}")
            else:
                print(f"Erro: Setor '{setor}' não existe.")

    def adicionar_deadline(self, setor, deadline):
        if setor in self.setores:
            self.setores[setor]["deadline"] = datetime.datetime.strptime(deadline, "%Y-%m-%d")
        else:
            print(f"Erro: Setor '{setor}' não existe.")

# Criando uma instancia da classe Hamburgueria
hamburgueria = Hamburgueria()

# Adicionando itens ao checklist de cada setor
hamburgueria.adicionar_item("cozinha", "Fazer lavagem das mãos")
hamburgueria.adicionar_item("cozinha", "Preparar ingredientes para a próxima refeição")
hamburgueria.adicionar_item("delivery", "Entregar entrega ao cliente")
hamburgueria.adicionar_item("salao", "Limpar mesa e banheiro")
hamburgueria.adicionar_item("limpeza", "Fazer a limpeza do estabelecimento")
hamburgueria.adicionar_item("estoque", "Reabastecer estoque de ingredientes")
hamburgueria.adicionar_item("compras", "Realizar compras para o dia seguinte")
hamburgueria.adicionar_item("financeiro", "Fazer a contabilidade do mês")
hamburgueria.adicionar_item("mkt", "Realizar marketing e publicidade")

# Removendo um item do checklist
hamburgueria.remover_item("cozinha", "Fazer lavagem das mãos")

# Impressão do checklist de cada setor
hamburgueria.imprimir_checklist()

# Adicionando deadline ao checklist de cada setor
hamburgueria.adicionar_deadline("limpeza", "2023-03-15")
hamburgueria.adicionar_deadline("estoque", "2023-03-17")

# Impressão do checklist de cada setor com deadline
hamburgueria.imprimir_checklist()