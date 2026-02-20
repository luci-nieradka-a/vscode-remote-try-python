import matplotlib.pyplot as plt 

# 1 - Construa um gráfico de barras que compare a nota de popularidade de séries em 2025
series = ['Stranger Things', 'It', 'Game of Thrones','Friends']
notas = [8.7, 9.8, 8.0,8.1]

plt.bar(series, notas)
plt.show()
plt.savefig('./exercicios/ex01.png')

# 2 - Construa um gráfico de barras que compare os celulares mais vendidos em 2026

#Ele limpa o grafico criando, para criar novos
plt.clf()

celulares = ['iPhone 17 Pro Max', 'iPhone 17', 'Xiaomi 17']
valor = [200000, 320000, 500000]

plt.bar(celulares, valor)
plt.show()
plt.savefig('./exercicios/ex02.png')

# 3 - Identifique na turma qual é o time de cada um e construa um gráfico de barras para mostrar a popularidade cada time
# Grẽmio: 3; Flamengo: 2; Palmeiras: 1; Internacional: 2; Vasco: 1
plt.clf()

times = ['Gremio', 'Flamengo', 'Palmeiras', 'Internacional', 'Vasco']
torcedores = [4, 2, 1, 2, 1]
cores = ['#0D80BF', '#C52613', '#006437', '#E5050F', '#000000']

plt.bar(times, torcedores, color=cores)
plt.xlabel('Times do campeonato brasileiro')
plt.ylabel('N° de torcedores')
plt.show()
plt.savefig('./exercicios/ex03.png')