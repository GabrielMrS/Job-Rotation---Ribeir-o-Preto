# Inserir o numero para verificar se ele está na sequencia
num = int(input("Digite um número inteiro: "))

# Indicando quais os numeros onde se inicia
a, b = 0, 1

# Loop para gerar a sequência de Fibonacci até o valor máximo
while b < num:
    # Calcula o próximo valor da sequência
    a, b = b, a + b

# Verifica se o numero inserido faz parte da sequencia
if b == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
