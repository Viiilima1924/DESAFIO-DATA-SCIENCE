import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import statistics

# Dados fornecidos
dados = [
    {"Nome": "João", "Compra": 25, "Região": "Sudeste"},
    {"Nome": "Maria", "Compra": 30, "Região": "Sudeste"},
    {"Nome": "Pedro", "Compra": 22, "Região": "Sul"},
    {"Nome": "Ana", "Compra": 28, "Região": "Sul"},
    {"Nome": "Ana", "Compra": 28, "Região": "Nordeste"},
    {"Nome": "Ana", "Compra": 28, "Região": "Sudeste"},
    {"Nome": "Ana", "Compra": 28, "Região": "Norte"},
    {"Nome": "Ana", "Compra": 28, "Região": "Sul"},
    {"Nome": "Ana", "Compra": 28, "Região": "Centro-Oeste"}
]

# Criando listas separadas para análise
compras = [d["Compra"] for d in dados]
regioes = [d["Região"] for d in dados]

# Estatísticas
media = np.mean(compras)
moda = statistics.mode(compras)
mediana = np.median(compras)
desvio_padrao = np.std(compras)
amplitude = np.max(compras) - np.min(compras)

# Impressão das estatísticas
print(f"Média das compras: {media}")
print(f"Moda das compras: {moda}")
print(f"Mediana das compras: {mediana}")
print(f"Desvio padrão das compras: {desvio_padrao}")
print(f"Amplitude das compras: {amplitude}")

# Gráfico de barras por região
contagem_regioes = Counter(regioes)
regioes_nomes = list(contagem_regioes.keys())
regioes_quantidades = list(contagem_regioes.values())

plt.figure(figsize=(8, 5))
plt.bar(regioes_nomes, regioes_quantidades, color='skyblue')
plt.title('Quantidade de Compras por Região')
plt.xlabel('Região')
plt.ylabel('Quantidade de Compras')
plt.show()

# Gráfico de linhas com as vendas (compras)
nomes = [d["Nome"] for d in dados]
indices = np.arange(len(nomes))

plt.figure(figsize=(10, 6))
plt.plot(indices, compras, marker='o', linestyle='-', color='orange', label='Compras')
plt.xticks(indices, nomes, rotation='vertical')
plt.title('Compras por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Compras')
plt.legend()
plt.tight_layout()
plt.show()