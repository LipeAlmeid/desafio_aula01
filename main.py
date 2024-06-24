CONSTANTE_BONUS = 1000

# 01) Solicite ao usuário que digite seu nome

nome = input("Digite seu nome: ")

#print(nome)

# 02) Solicita ao usuário que digite o valor do seu salário
# COnverte a entrada para um número de ponto flutuante

salario = float(input("Digite o seu salário: "))

#print(salario)


# 03) Solicita ao usuário que digite o valor do bonus recebido 
# Converte a entrada para um número de ponto flutuante

bonus = float(input("Digite o valor do seu bônus: "))

#print(bonus)

# 04) Calcule o valor do bônus final 

bonus_final = CONSTANTE_BONUS + salario * bonus

#print(bonus_final)

# 05) Imprima cálculo do KPI para o usuário

print(bonus_final)

# 06) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

print(f"O usuario {usuario} possui o salario `{salario} e o bonus {bonus} com o bonus final {bonus_final}")

# Bônus: Quantos bugs e riscos voce consegue indentificar nesse programa?