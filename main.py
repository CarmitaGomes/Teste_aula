print("Olá turma do Python!")
print("Tudo bem!")
nome: str = input("Qual é o seu nome? ")
print(f"\nOlá, {nome}!")
idade: int = int(input("Qual é a sua idade? "))
print(f"Tu tens {idade} anos...")

if idade < 18:
    print("Tu ainda és menor de idade!")
else:
    print("Tu já és maior de idade!")

cidade: str = input("\nEm que cidade vives? ")
pais: str = input("Em que país fica essa cidade? ")

if cidade.lower() == "lisboa" and pais.lower() == "portugal":
    print(f"Bom saber que vives em {cidade.title()}, capital de Portugal!")
elif pais:
    print(f"Bom saber que vives em {cidade.title()}, {pais.title()}!")
else:
    print(f"Bom saber que vives em {cidade.title()}!")

print("\nMuito obrigado por responder as perguntas!")

