import matplotlib.pyplot as plt

# Dados
paises = ['Portugal', 'Brasil', 'Angola', 'Moçambique', 'Cabo Verde', 'São Tomé e Príncipe', 'Timor-Leste', 'Guiné-Bissau', 'Macau']
valores = [36210, 13533, 7343, 1386, 6807, 4231, 5667, 1093, 82262]
moedas = [ ' EUR ' , ' BRL ' , 'AOA', 'MZN', 'CVE', 'STN', 'USD', 'XOF', ' MOP ']

# Criar o gráfico
plt.figure(figsize=(12, 7))
bars = plt.barh(paises, valores, color='skyblue')
plt.xlabel('Renda Per Capita (USD)')
plt.title('Renda Per Capita em Países de Língua Portuguesa (2022)')
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adicionar os valores nas barras e as moedas ao lado
for bar, valor, moeda in zip(bars, valores, moedas):
    plt.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2, f'${valor:,}', va='center')
    plt.text(bar.get_width() + 5000, bar.get_y() + bar.get_height()/2, moeda, va='center')

# Ajustar a margem direita para evitar sobreposição
plt.subplots_adjust(right=0.85)

# Mostrar o gráfico
plt.tight_layout()
plt.show()