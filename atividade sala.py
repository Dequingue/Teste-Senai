import os

os.system("cls || clear")

media: float = 0
somar: float = 0
opcao: str
contador: int = 0


print("S - Inserir uma nota")
print("P - Ver quantas notas foram inscritas ")
print("N - Calcular a média aritimetica das notas informadas ")
print("l - finalizar programa ")

while True:

    opcao = str(input("Escolha uma opção: "))

    if(opcao == 's'):
        nota = float(input("Digite uma nota: "))
        somar = somar + nota
        contador = contador + 1
        
    elif(opcao == 'p'):
        print(f"\nquantas notas fora inseridas {contador}")    
        
    if(opcao == 'n'):
        media = somar / contador
        print(f"\nMedia da unidade {media}")
            
    if(opcao == 'l'):
        os.system("cls || clear")
        print("finalizando system.....")
        break
        
        
