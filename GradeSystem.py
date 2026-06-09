# ==========================================
# SISTEMA DE GESTÃO DE NOTAS E FALTAS
# ==========================================

# Função para escolher o nível de ensino
def escolher_nivel():

    print("\nNÍVEIS DA EDUCAÇÃO BÁSICA")
    print("1 - Educação Infantil")
    print("2 - Ensino Fundamental I")
    print("3 - Ensino Fundamental II")
    print("4 - Ensino Médio")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        return "Educação Infantil", [
            "Linguagem",
            "Matemática Básica",
            "Artes"
        ]

    elif opcao == "2":
        return "Ensino Fundamental I", [
            "Português",
            "Matemática",
            "Ciências"
        ]

    elif opcao == "3":
        return "Ensino Fundamental II", [
            "Português",
            "Matemática",
            "História",
            "Geografia",
            "Ciências"
        ]

    elif opcao == "4":
        return "Ensino Médio", [
            "Português",
            "Matemática",
            "Física",
            "Química",
            "Biologia"
        ]

    else:
        print("\nOpção inválida!")
        return escolher_nivel()


# Função para verificar situação do estudante
def verificar_situacao(nota_final, frequencia):

    if frequencia < 75:
        return "Reprovado por falta"

    elif nota_final < 6:
        return "Reprovado por nota"

    else:
        return "Aprovado"


# Função para cadastrar dados das disciplinas
def cadastrar_disciplinas(disciplinas):

    dados = []

    for disciplina in disciplinas:

        print(f"\n===== {disciplina} =====")

        nota1 = float(input("Digite a nota da Prova 1: "))
        nota2 = float(input("Digite a nota da Prova 2: "))
        trabalho = float(input("Digite a nota do Trabalho: "))

        faltas = int(input("Digite o total de faltas: "))
        total_aulas = int(input("Digite o total de aulas: "))

        # Nota final é a SOMA das avaliações
        nota_final = nota1 + nota2 + trabalho

        # Frequência em percentual
        frequencia = ((total_aulas - faltas) / total_aulas) * 100

        situacao = verificar_situacao(
            nota_final,
            frequencia
        )

        disciplina_dados = {
            "disciplina": disciplina,
            "nota_final": nota_final,
            "faltas": faltas,
            "frequencia": frequencia,
            "situacao": situacao
        }

        dados.append(disciplina_dados)

    return dados


# Função para gerar relatório
def gerar_relatorio(nome, nivel, dados):

    print("\n")
    print("=" * 50)
    print("RELATÓRIO FINAL")
    print("=" * 50)

    print(f"Aluno: {nome}")
    print(f"Nível da Educação Básica: {nivel}")

    print("\nDISCIPLINAS")

    for item in dados:

        print("\n------------------------------")
        print("Disciplina:", item["disciplina"])
        print("Nota Final:", item["nota_final"])
        print("Total de Faltas:", item["faltas"])
        print(
            "Percentual de Frequência:",
            round(item["frequencia"], 2),
            "%"
        )
        print("Situação:", item["situacao"])

    print("\n" + "=" * 50)

    aprovados = 0
    reprovados_nota = 0
    reprovados_falta = 0

    for item in dados:

        if item["situacao"] == "Aprovado":
            aprovados += 1

        elif item["situacao"] == "Reprovado por nota":
            reprovados_nota += 1

        else:
            reprovados_falta += 1

    print("RESUMO")
    print("Aprovados:", aprovados)
    print("Reprovados por Nota:", reprovados_nota)
    print("Reprovados por Falta:", reprovados_falta)

    print("=" * 50)


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

print("=" * 50)
print("SISTEMA DE GESTÃO DE NOTAS E FALTAS")
print("=" * 50)

nome_aluno = input("Digite o nome do estudante: ")

nivel, disciplinas = escolher_nivel()

dados_disciplinas = cadastrar_disciplinas(
    disciplinas
)

gerar_relatorio(
    nome_aluno,
    nivel,
    dados_disciplinas
)
