def dividir(numerador, denominador):
    try:
        if denominador == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return numerador / denominador
    except ZeroDivisionError as erro:
        return erro

print(dividir(10, 2))
print(dividir(10, 0))


try:
    print(minha_variavel)
except NameError as erro:
    print(f"Erro: A variável não foi definida. Detalhes do erro: {erro}")


class ErroIdadeInvalida(Exception):
    def __init__(self, message):
        super().__init__(message)

def idade_valida(idade):
    try:
        if idade < 0 or idade > 120:
            raise ErroIdadeInvalida("Idade inválida. A idade deve estar entre 0 e 120.")
        return "Idade válida."
    except ErroIdadeInvalida as erro:
        return erro

print(idade_valida(25))
print(idade_valida(130))
print(idade_valida(-5))


def solicitar_numero():
    try:
        numero = float(input("Digite um número: "))
        return numero
    except ValueError:
        return "Erro: O valor digitado não é um número válido."

resultado = solicitar_numero()
print(resultado)