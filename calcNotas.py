#=========================================================
# calcNotas.py
# O programa calcula a média de um aluno com base nas notas das avaliações bimestrais e continuada
# Clayton J A Silva
# 19mar2022

# Leitura dos dados de entrada e atribuição às variáveis do tipo ponto flutuante
ap1=float(input("Digite a nota da AP1: "))
ap2=float(input("Digite a nota da AP2: "))
ac=float(input("Digite a nota da AC: "))

# Calcula da nota do período
np=0.4*(ap1+ap2)+0.2*ac

# Escreve a nota do período
print("A nota do aluno é ",round(np,1)) # Aproxima o resultado em uma casa decimal

