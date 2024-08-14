frase = input('Digite uma frase:  ') #Saída
d = {}
for letra in frase: #Para letra em frase
    #Se letra não existir no dicionário, retorna 0
    #Se existir, retorna o valor anterior
    d[letra] = d.get(letra, 0) + 1 #Função get do dicionário
    print(d)