from colorama import Fore, Style

print("Controle de Níveis de água".center(40, "-"))
print(f"\n nível de reservatorio vai de 1 a 5"  )

# Lista com as situações e cores de cada nível
niveis = [
    None,
    {"situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"situacao": "Baixo", "cor": Fore.YELLOW},
    {"situacao": "Médio", "cor": Fore.GREEN},
    {"situacao": "Alto", "cor": Fore.CYAN},
    {"situacao": "Muito alto (alerta)", "cor": Fore.BLUE}
]

# Função responsável por exibir a situação
def exibir_nivel(nivel):
    if nivel < 1 or nivel > 5:
        print("Nível inválido! Informe um valor de 1 a 5.")
        return

    situacao = niveis[nivel]["situacao"]
    cor = niveis[nivel]["cor"]

    print(f"{cor}Nível {nivel}: {situacao}{Style.RESET_ALL}")

try:
    nivel = int(input("Qual o nível do reservatório (1 a 5)? "))
    exibir_nivel(nivel)
except ValueError:
    print("Entrada inválida! Digite um número inteiro.")