class Stock:
  def __init__(self, id, marca, ref, specs, custosFabrico, custoVenda, stock, qV):
    self.id = id
    self.marca = marca
    self.ref = ref
    self.specs = specs
    self.custoFabrico = custosFabrico
    self.custoVenda = custoVenda
    self.stock = stock
    self.quantidadeVendida = qV


  def __str__ (self):
    return f"id: {self.id}, marca: {self.marca}, ref: {self.ref}, specs: {self.specs}, custoFabrico: {self.custoFabrico}, custoVenda: {self.custoVenda}, stock: {self.stock}, qV: {self.quantidadeVendida}"

def set_cV(self, cV):
  if valor > 0:
    self.custoVenda = Valor
  else:
    print("Preço tem de ser positivo")

  custoVenda = property(set_CV)


#exercicio 101
  def valorTotal(self):
    return self.quantidadeVendida * self.custoVenda

#exercicio 102

  def margemmaior(self, lista):
    lista = sorted(lista, reverse=True)
    for i in lista:
        print(i)
#11.103.Cria uma lista com 3 computadores e testa os métodos criados.
Listacomp = [Stock(1, "ASUS", "uid", "i7, 16GB RAM, 512GB SSD", 800, 1200, 10, 5),
             Stock(2, "HP", "Naosei", "i5, 32GB RAM, 960GB SSD", 600, 900, 15, 8),
             Stock(3, "Apple", "MacBook Air", "M1, 64GB RAM, 1000GB SSD", 2000, 4500, 12, 6)]


#Testes
def Menu(self, lista, Listacomp):
  print("Menuzao: \n[1] Setar Custo de venda \n[2]Total Vendido Individual \n [3] Mostrar Maior Margem")
  opcao = int(input("Escreve a opcao: "))
  if opcao == 1:
    for i in Listacomp:
      print(i)
    id = int(input("Escreve o Id do produto: "))
    valor = int(input("Escreve o valor do produto: "))
    for i in Listacomp:
      if i.id == id:
        i.custoVenda = valor
        print(f"Custo de venda atualizado, atualmente {valor}")
      elif opcao == 2:
        for i in Listacomp:
          print(i)
        id = int(input("Escreve o Id do produto: "))
        for i in Listacomp:
          if i.id == id:
            print(f"Total vendido individual: {i.valorTotal()}")
      elif opcao == 3:
        for i in Listacomp:
          print(i)
        id = int(input("Escreve o Id do produto: "))
        for i in Listacomp:
          if i.id == id:
            print(f"Maior margem: {i.margemmaior()}")
      else:
        print("Erro numero mal")