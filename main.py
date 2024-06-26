CONSTANTE_BONUS = 1000

# 01) Solicite ao usuário que digite seu nome

nome = input("Digite seu nome: ")

if nome.isdigit():
    print("Voce digitou o seu nome errado")
    exit()
elif len(nome) == 0:
    print("Voce nao digitou nada")
    exit()
elif nome.isspace():
    print("Voce digitou so espaço")
    exit()

#print(nome)

# 02) Solicita ao usuário que digite o valor do seu salário
# COnverte a entrada para um número de ponto flutuante

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()


# 03) Solicita ao usuário que digite o valor do bonus recebido 
# Converte a entrada para um número de ponto flutuante


try:
    bonus = float(input("Digite o valor do seu bônus: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bonus")
except ValueError:
    print("Entrada inválida para salário. Por favor digite um numero")
    exit()

#print(bonus)

# 04) Calcule o valor do bônus final 

bonus_final = CONSTANTE_BONUS + salario * bonus

#print(bonus_final)

# 05) Imprima cálculo do KPI para o usuário

print(bonus_final)

# 06) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O usuario {usuario} possui o salario {salario} e o bonus {bonus} com o bonus final {bonus_final}")

# Bônus: Quantos bugs e riscos voce consegue indentificar nesse programa?


