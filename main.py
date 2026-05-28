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

if pais:
    print(f"Bom saber que vives em {cidade}, {pais}!")
else:
    print(f"Bom saber que vives em {cidade}!")

print("\nMuito obrigado por responder as perguntas!")

