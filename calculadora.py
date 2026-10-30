# ============================================================
# CALCULADORA PYTHON PERSONALIZADA
# ============================================================

def soma(a, b):
    # Fórmula: Soma
    return a + b

def subtracao(a, b):
    # Fórmula: Subtração
    return a - b

def multiplicacao(a, b):
    # Fórmula: Multiplicação
    return a * b

def divisao(a, b):
    # Fórmula: Divisão
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def main():
    print("--- CALCULADORA SIMPLES ---")
    print("1: Soma (+)")
    print("2: Subtração (-)")
    print("3: Multiplicação (*)")
    print("4: Divisão (/)")
    print("0: Sair")
    
    while True:
        opcao = input("\nEscolha a operação: ").strip()
        if opcao == "0":
            print("Encerrando...")
            break
            
        n1 = float(input("Digite o 1º número: "))
        n2 = float(input("Digite o 2º número: "))
        
        if opcao == "1":
            print("Resultado:", soma(n1, n2))
        elif opcao == "2":
            print("Resultado:", subtracao(n1, n2))
        elif opcao == "3":
            print("Resultado:", multiplicacao(n1, n2))
        elif opcao == "4":
            print("Resultado:", divisao(n1, n2))
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
