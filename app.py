def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal (IMC)"""
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    """Classifica o IMC em categorias"""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau I"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

# Solicita que o usuário insira peso e altura
peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = calcular_imc(peso, altura)

# Classifica o IMC
classificacao = classificar_imc(imc)

# Exibe o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")