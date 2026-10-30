"""
Calculadora Aritmética Básica em Python
Operações: Soma, Subtração, Multiplicação e Divisão
"""

def adicionar(a: float, b: float) -> float:
    """Retorna a soma de dois números (a + b)."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a subtração do segundo número em relação ao primeiro (a - b)."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto da multiplicação de dois números (a * b)."""
    return a * b


def dividir(a: float, b: float) -> float:
    """
    Retorna o quociente da divisão (a / b).
    Lança ZeroDivisionError se o divisor for zero.
    """
    if b == 0:
        raise ZeroDivisionError("Erro: Não é possível realizar divisão por zero!")
    return a / b


def exibir_menu() -> None:
    """Exibe o menu de opções para o usuário."""
    print("\n" + "=" * 40)
    print("        CALCULADORA EM PYTHON")
    print("=" * 40)
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("0 - Sair")
    print("=" * 40)


def executar_calculadora() -> None:
    """Função principal que gerencia o loop de execução da calculadora."""
    print("Bem-vindo à Calculadora em Python!")
    
    # Demonstração rápida de chamadas de funções
    num1 = 15.0
    num2 = 3.0
    
    print(f"\n--- Exemplos Práticos com os números {num1} e {num2} ---")
    print(f"Soma:          {num1} + {num2} = {adicionar(num1, num2)}")
    print(f"Subtração:     {num1} - {num2} = {subtrair(num1, num2)}")
    print(f"Multiplicação: {num1} * {num2} = {multiplicar(num1, num2)}")
    print(f"Divisão:       {num1} / {num2} = {dividir(num1, num2)}")
    
    # Teste de proteção contra divisão por zero
    try:
        print("\nTestando divisão por zero:")
        dividir(10, 0)
    except ZeroDivisionError as erro:
        print(f"Capturado com sucesso: {erro}")

    print("\nCalculadora pronta para uso!")


# Executa a demonstração
if __name__ == "__main__":
    executar_calculadora()
