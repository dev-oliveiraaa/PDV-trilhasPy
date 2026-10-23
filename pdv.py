def descIdade(valor, idade):
    if(idade >= 65):
        return valor * 0.20
 

def menu():
    idade = 0;
    valor = 0.0;
    
while True:
    valor = float(input("Digite o valor da compra: (ou 0 para encerrar) \n"))
    if valor == 0:
        break;
    idade = int(input("Digite a idade do cliente: "))
    
    
    