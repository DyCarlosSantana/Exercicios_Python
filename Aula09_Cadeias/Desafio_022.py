nome = str(input('Digite seu nome: '))
print(nome.upper()) #Maiusculas
print(nome.lower())#Minusculas
print(len(nome.strip())) #Contagem de caracters (sem espaço)
dividido = nome.split() # Dividindo o nome em uma lista.
print(dividido[0]) #selecionando o primeiro item da lista e imprimindo.