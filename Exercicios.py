#1.	Escreva um programa que peça dois números ao usuário e exiba a soma deles.
print ('Digite 2 Numeros para Somar')
numeros1 = int(input('digite o primeiro numero:   '))
numeros2 = int(input('digite o segundo numero:   '))
soma = numeros1 + numeros2
print('sua soma é',soma)


#2.	Solicite dois números e mostre o resultado da multiplicação entre eles.
print ('Digite 2 Numeros para Multiplicar')
numeros1 = int(input('digite o primeiro numero:   '))
numeros2 = int(input('digite o segundo numero:   '))
resultado = numeros1 * numeros2
print('sua multipicação é',resultado)


#3.	Peça ao usuário um número e mostre o dobro desse número.
print ('Digite um Numeros para saber o dobro')
numeros1 = int(input('digite o primeiro numero:   '))
resultado = numeros1 * 2
print('sua multipicação é',resultado)


#4.	Solicite três números e exiba a média deles.
print ('Media')
print ('digite seus numeros para ter uma media')
nota1 = float(input('digite a primeira nota:   '))
nota2 = float(input('digite a segunda nota:   '))
nota3 = float(input('digite a terceira nota:   '))
soma = nota1 + nota2 + nota3
media = soma / 3
print('a media é',media)


#5.	Peça ao usuário dois números e informe qual é o maior e qual é o menor.
print ('digite 2 numeros para saber qual é maior e qual é menor')
numeros1 = int(input('digite o primeiro numero:   '))
numeros2 = int(input('digite o segundo numero:   '))
if numeros1 > numeros2:
    print('o primeiro numero é maior')
elif numeros2 > numeros1:
    print('o segundo numero é maior')
else:
    print('os numeros são iguais')


#6.	Solicite um número e verifique se ele é par ou ímpar.
print ('digite um numero para saber se é par ou impar')
numeros1 = int(input('digite o primeiro numero:   '))
if numeros1 % 2 == 0:
    print('o numero é par')
else:
    print('o numero é impar')

    
#7.	Peça ao usuário três números e verifique se eles podem formar um triângulo (a soma de dois lados deve ser maior que o terceiro lado).
print ('digite 3 numeros para saber se podem formar um triangulo')
numeros1 = int(input('digite o primeiro numero:   '))
numeros2 = int(input('digite o segundo numero:   '))
numeros3 = int(input('digite o terceiro numero:   '))
if numeros1 + numeros2 > numeros3 and numeros1 + numeros3 > numeros2 and numeros2 + numeros3 > numeros1:
    print('os numeros podem formar um triangulo')
else:
    print('os numeros não podem formar um triangulo')


#8.	Verifique se um número digitado pelo usuário está entre 10 e 50.
print ('digite um numero para saber se esta entre 10 e 50')
numeros1 = int(input('digite o numero:   '))
if numeros1 >= 10 and numeros1 <= 50:
    print('o numero esta entre 10 e 50')
else:
    print('o numero não esta entre 10 e 50')


#9.	Peça dois números e verifique se são iguais ou diferentes.
print ('digite dois numeros para saber se são iguais ou diferentes')
numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero:'))
if numero1 == numero2:
    print('os numeros são iguais')
else:
    print('os numeros são diferentes')


#10.	Solicite um número e informe se ele é positivo, negativo ou zero.
print ('digite um numero para saber se é positivo ou negativo ou zero')
numero1 = int(input('digite o numero'))
if numero1 > 0:
    print('o numero é positivo')
elif numero1 < 0:
    print('o numero é negativo')
else:
    print('o numero é zero')


#11.	Escreva um programa que peça a idade do usuário e verifique se ele pode votar (idade ≥ 16).
print ('Digite sua idade para saber se pode votar ou não')
idade = int(input('digite sua idade'))
if idade >= 16:
    print('Você pode votar')
else:
    print('Você não pode votar')


#12.	Solicite ao usuário um número e verifique se ele é múltiplo de 5.
print ('Digite um numero para saber se é multiplo de 5')
numero5 = int(input('digite o numero:'))
if numero5 % 5 == 0:
    print(f'{numero5} é multiplo de 5')
else:
    print(f'{numero5} não é multiplo de 5')


#13.	Peça um número ao usuário e verifique se ele está dentro da faixa de 1 a 100.
print ('digite um numero para saber se esta entre 1 e 100')
numero1 =int(input('digite um numero:'))
if numero1 >=1 and numero1 <=100:
    print (f'{numero1} está entre 1 e 100')
else:
    print(f'{numero1} não está entre 1 e 100')


#14.	Solicite três números e exiba-os em ordem crescente.
print ('digite 3 numeros para serem exibidos em ordem crescente')
numero1 = int(input('digite o primeiro numero:'))
numero2 = int(input('digite o segundo numero'))
numero3 = int(input('digite o terceiro numero'))
if numero1 > numero2 > numero3:
    print('os numeros em ordem crescente são:', numero1, numero2, numero3)
elif numero1 > numero3 > numero2:
    print('os numeros em ordem crescente são:', numero1, numero3, numero2)
elif numero2 > numero1 > numero3:
    print('os numeros em ordem crescente são:', numero2, numero1, numero3)
elif numero2 > numero3 > numero1:
    print('os numeros em ordem crescente são:', numero2, numero3, numero1)
elif numero3 > numero1 > numero2:
    print('os numeros em ordem crescente são:', numero3, numero1, numero2)
elif numero3 > numero2 > numero1:
    print('os numeros em ordem crescente são:', numero3, numero2, numero1)
else:
    print('os numeros são iguais')


#15.	Peça ao usuário o valor do salário e calcule um aumento de 10% se for menor que R$2000, senão, o aumento será de 5%.
print('Digite seu salário para saber o aumento:')
salario = float(input('Digite seu salário:'))
if salario < 2000:
    salario_aumento = salario * 1.10
    print(f'Seu salário teve um aumento de 10%, indo para R${salario_aumento:.2f}')
else:
    salario_aumento = salario * 1.05
    print(f'Seu salário teve um aumento de 5%, indo para R${salario_aumento:.2f}')


#16.	Desenvolva um programa que pergunte a altura e o peso de uma pessoa e calcule o IMC. Informe se está abaixo do peso, peso ideal ou sobrepeso.
print('Cálculo de IMC')
peso = float(input('Digite seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Seu IMC atual é {imc:.2f} e sua classificação atual é Abaixo do Peso')
elif 18.5 <= imc <= 24.9:
    print(f'Seu IMC atual é {imc:.2f} e sua classificação atual é Peso Normal')
elif 25 <= imc <= 29.9: 
    print(f'Seu IMC atual é {imc:.2f} e sua classificação atual é Sobrepeso')
elif 30 <= imc <= 34.9: 
    print(f'Seu IMC atual é {imc:.2f} e sua classificação atual é Obesidade Classe I')
elif 35 <= imc <= 39.9:
    print(f'Seu IMC atual é {imc:.2f} e sua classificação atual é Obesidade Classe II')
else:
    print(f'Seu IMC atual é {imc:.2f} e sua classificação atual é Obesidade Classe III')


#17.	Crie um programa que receba a nota de um aluno e exiba "Aprovado" se for maior ou igual a 7, "Recuperação" se estiver entre 5 e 6.9 e "Reprovado" se for menor que 5.
print ('Digite sua nota para saber se foi aprovado, reprovado ou se está de recuperação')
nota = float(input('Digite sua nota:'))
if nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('Recuperação')
else:
    print('Reprovado')


#18.	Solicite um ano ao usuário e informe se ele é bissexto (divisível por 4 e não por 100, exceto se for divisível por 400). 
print ('Digite um ano para saber se é bissexto')
ano = int(input('Digite o ano:'))
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')


#19.	Peça ao usuário para escolher um número de 1 a 7 e exiba o dia da semana correspondente (1 = Domingo, 2 = Segunda...).
print ('digite um numero de 1 a 7 para saber o dia da semana')
dia = int(input('digite o numero:'))
if dia == 1:
    print('Domingo')
elif dia == 2:
    print('Segunda')
elif dia == 3:
    print('Terça')
elif dia == 4:
    print('Quarta')
elif dia == 5:
    print('Quinta')
elif dia == 6:
    print('Sexta')
elif dia == 7:
    print('Sabado')
else:
    print('o numero não esta entre 1 e 7')


#20.	Crie um sistema simples de login: peça um nome de usuário e senha e verifique se correspondem a um usuário cadastrado no programa.
print ('Sistema de Login')
print ('Usuario: Admin')
print ('Senha: Admin123')
usuario = input('Digite seu usuario:')
senha = input('Digite sua senha:')
if usuario == 'Admin' and senha == 'Admin123':
    print('Login realizado com sucesso')
else:
    print('Usuario ou senha incorretos')









#Desafio
#Desafio
#Desafio
#Desafio
#Desafio
#Desafio





'''Desafio
História:
Um hacker invadiu seu sistema e bloqueou um cofre digital contendo informações valiosas. Para destravá-lo, você precisa resolver uma sequência de desafios de programação em Python.
Cada desafio correto fornecerá um número do código final para abrir o cofre.
Desafios:
Os alunos devem completar os trechos de código abaixo e obter a senha final (formada pelos números das respostas corretas).
🔢 Desafio 1: O primeiro número do cofre (Operadores)
Complete o código para calcular a senha correta:

# O hacker deixou esta equação incompleta. Resolva e descubra o número.
senha1 = (10 + 5) * 2 / 5  # Complete a equação corretamente
print(int(senha1))  # O resultado deve ser um número inteiro


📥 Desafio 2: Entrada e saída de dados
O hacker escondeu um número secreto e deu uma dica. Peça ao usuário para inserir um número e verifique se está correto:

# O hacker diz que a senha é igual ao dobro de um número escolhido menos 4.
num = int(input("Digite um número: "))
senha2 = (num-4)*2  # Complete a fórmula
print("A senha parcial é:", senha2)



🔍 Desafio 3: Condicional – Encontrando a chave certa
Agora você precisa verificar se a chave inserida está correta para destravar a última parte do cofre:

# A chave correta deve ser maior que 50 e múltipla de 7.
chave = int(input("Digite a chave de acesso: "))

if chave > ____ == 0:  # Complete a condição correta
    print("Chave aceita! Pegue o último número da senha: 9")
else:
    print("Chave incorreta! Tente novamente.")'''


#669







#Exercícios com While
#Exercícios com While
#Exercícios com While
#Exercícios com While
#Exercícios com While





#1.	Contagem de 1 a 10 Escreva um programa que exiba os números de 1 a 10 usando um loop while.
contagem = 1
while contagem <= 10:
    print(contagem)
    contagem += 1


#2.	Soma de números até zero Peça ao usuário para digitar números inteiros. Some esses números até que ele digite 0. No final, exiba a soma total.
print('Soma de números, digite 0 para parar e ver o resultado')
numero = int(input('Digite o primeiro número: '))
soma = 0
while numero != 0:
    soma += numero
    numero = int(input('Digite o próximo número: '))
print(f'A soma total é {soma}')


#3.	Adivinhe o número Escolha um número secreto (ex: 7). O usuário deve tentar adivinhar, e o programa só para quando ele acertar.
print('Adivinhe o numero secreto de 1 a 10')
ns = 7
while True:
    numero = int(input('digite um numero:'))
    if numero > 10:
        print ('O numero esta acima do pormitido')
    elif numero < 1:
        print ('O numero esta abaixo do permitido')
    elif numero == ns:
        print(f'O numero esta correto')
        break
    else:
        print ('O numero esta incorreto')


#4.	Tabuada do 5 Utilize while para imprimir a tabuada do 5 (de 5×1 até 5×10).
print('Tabuada do 5')
tabuada = 5
contador = 1
while contador <= 10:
    resultado = tabuada * contador
    print(f'(Tabuada do 5) {tabuada} x {contador} = {resultado}')
    contador += 1                                          


#5.	Contagem regressiva Peça um número ao usuário e faça uma contagem regressiva até 0.
print('Digite um numero para ter uma ordem regressiva até 0')
numero = int(input('Numero:'))
contador = numero
while contador >= 0:
    print(contador)
    contador -= 1
print('Contagem finalizada')


#6.	Senha correta Peça para o usuário inserir uma senha. Enquanto ele não digitar "1234", continue pedindo.
print('Para logar digite a senha')
senha = 1234
while True:
    numero = int(input('Senha:'))
    if  numero == senha:
        print(f'Logado com Sucesso')
        break
    else:
        print ('Senha incorreta tente novamente')



#7.	Soma dos pares de 1 a 100 Utilize while para somar todos os números pares de 1 a 100 e exiba o resultado.
print('Soma dos pares de 1 a 100')
numero = 2
soma = 0
while numero <= 100:
    soma += numero  
    numero += 2
print(f'A soma de todos os números pares de 1 a 100 é: {soma}')



#8.	Invertendo um número Peça um número inteiro ao usuário e exiba ele ao contrário (ex: 1234 → 4321).
print('Digite um numero para inverte-lo')
num = int(input('Numero:'))
i = 0
while num > 0:
    un = num % 10
    i = (i*10) + un
    num //= 10
print(f'Seu numero ao contrario é {i}')


#9.	Número primo Peça um número ao usuário e verifique se ele é primo usando while.
print('Digite um numero para saber se é primo ou não')
num = int(input('numero:'))
if num <=1:
    print (f'{num} não é primo')
elif num == 2 or num == 3:
    print (f'{num} é primo')
else:
    i = 2
    while i < num:
        if num % i == 0:
            print (f'{num} não é primo')
            break
        i += 1
    else:
        print (f'{num} é primo')
    









#Desafio
#Desafio
#Desafio
#Desafio
#Desafio
#Desafio


#Crie um programa que mostre, na tela, um contador. O contador deve ser inicializado com zero. 
#O usuário deve ter a opção de incrementar uma unidade ao contador ou de encerrar o programa.
#Enquanto o usuário continuar escolhendo incrementar o contador, o programa não deve ser encerrado.
#O programa será encerrado somente quando o usuário decidir
#Utilize os comandos continue e break
#Exiba o contador 

print('Contagem de 10 Números a partir do 0 e pulando a quantidade escolhida')
contagem = 0  
n1 = int(input('Número a ser pulado: '))
while True:  
    for _ in range(10):  
        print(contagem)
        contagem += n1  
    print('Deseja continuar?')
    print('1 para continuar com o mesmo salto')
    print('2 para mudar o salto')
    print('3 para parar')
    continuar = int(input('Digite 1, 2 ou 3: '))
    if continuar == 1:
        continue  
    elif continuar == 2:
        n1 = int(input('Digite o novo número a ser pulado: ')) 
    elif continuar == 3:
        print('Fim do Programa')
        break
    else:
        print('Opção inválida, encerrando programa.')
        break












#Exercícios com For
#Exercícios com For
#Exercícios com For
#Exercícios com For
#Exercícios com For
#Exercícios com For




#1.Faça um programa que faça uma Contagem de 1 a 10 e outra de 10 a 1

#De 1 a 10
contagem = 1
for i in range (10):
    print(contagem)
    contagem += 1

#De 10 a 1
contagem = 10
for i in range (10):
    print(contagem)
    contagem -= 1


#2.Soma dos primeiros 10 números inteiros
soma = 0
for i in range (11):
    soma += i
    print(f'sua soma é {soma}')


#3. Iterar sobre uma string e imprimir cada caractere Exemplo: 
#palavra = "Python"
#P
#y
#t
#h
#o
#n

palavra = "Python"
for letra in palavra:
    print(letra)



#4. Contar vogais em uma frase
#frase = "A tecnologia está mudando o mundo"
#vogais = "aeiouAEIOU"
vogais = "aeiouAEIOU"
frase = input('Digite a frase para saber as vogais:')
for letra in frase:
    if letra in vogais:
        print(letra)



#5. Exibir os números pares de 1 a 20
contagem = 2
for i in range (10):
    print(contagem)
    contagem += 2




#6. Soma de números ímpares de 1 a 50
soma = 0
for i in range (1 ,51):
    if i % 2 != 0:
        soma += i
        print(i)
    print(f'sua soma é {soma}')











#Criando uma lista
#Criando uma lista
#Criando uma lista
#Criando uma lista
#Criando uma lista



#criando uma lista com alguns elementos e Exibindo a Lista
frutas = ['maçã', 'banana', 'laranja', 'uva']
print (frutas)


#criando uma lista com alguns elementos e Exibindo o segundo item da Lista
frutas = ['maçã', 'banana', 'laranja', 'uva']
print (frutas[2])


#criando uma lista com inteiro, float, string e booleano e exibindo a lista
itens = [1, 1.2, 'teste', 1 < 2 ]
print(f'os itens são {itens}')

#puxando um elemento especifico da lista
minha_lista = [1, 2, 3, 4]
print(minha_lista[0]) #saida: 1
print(minha_lista[2]) #saida: 3


#modificando elementos:
minha_lista = [1, 2, 3, 4]
minha_lista[2] = 10 #modificando o terceiro elemento da lista para 10
print(minha_lista[0]) #saida: 0
print(minha_lista[1]) #saida: 1
print(minha_lista[2]) #saida: 2
print(minha_lista[3]) #saida: 3

#substituindo o 5° item
minha_lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
minha_lista[4] = 'Jabuticaba'
print(minha_lista[0]) #saida: 0
print(minha_lista[1]) #saida: 1
print(minha_lista[2]) #saida: 2
print(minha_lista[3]) #saida: 3
print(minha_lista[4]) #Saída: 4

#adiciona um elemento apos o ultimo
carros = ['Chevrolet', 'Fiat', 'Wolksvagen', 'Toyota']
carros.append('fusca')
print(carros) #saida: [1,2,3,4,5]


#Criando uma lista vazia
lanche = []   #lista vazia
#adicionando lanches com .append ()
lanche.append('batata')
lanche.append('pizza')
lanche.append('hamburger')
#Exibindo lanches da lista
print(lanche)


#Criando uma lista vazia
lanches = []
#Pedindo o usuario para adicionar 3 lanches
for i in range(3):
    lanche = input(f'digite o {i+1}° lanche:')
    lanches.append(lanche)
#Exibindo lanches da lista
print('seus lanches são:', lanches)

#Notas, Media, Aprovação, Recuperação e Reprovado
#Criando uma lista vazia
Notas = []
situacao = ''
#Pedindo o usuario para adicionar 5 notas
print('Digite duas 5 notas para saber a media e a situação escolar')
for i in range(5):
    nota = float(input(f'Digite o {i+1}° Nota: '))
    Notas.append(nota)
#Somando e fazendo a media
soma = Notas[0] + Notas[1] + Notas[2] + Notas[3] + Notas[4]
media = soma / 5
#Situação
if media >= 6:
    situacao = 'Aprovado'
elif media <= 5:
    situacao = 'Recuperação'
else:
    situacao = 'Reprovado' 
#Exibindo lanches da lista
print('Suas notas são:', Notas)
print('Sua media é:', media)
print('E sua situação escolar é: ', situacao)


#criando uma lista com alguns produtos e inserinddo Sabão em Pó na posição 2
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista.insert(2, 'Sabão em Pó') #Inserindo na posição 2
print(lista) #Saída: ['Sabonete', 'Shampoo', 'Sabão em Pó', 'Pasta de Dente', 'Esponja', 'Papel Higienico']


#criando uma lista com alguns produtos e inserindo em um lugar espefico
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista[2:1] = ['Sabão em Pó', 'Desinfetante'] #Inserindo na posição 2 de 1
print(lista) #Saída: ['Sabonete', 'Shampoo', 'Sabão em Pó', 'Desinfetante', 'Pasta de Dente', 'Esponja', 'Papel Higienico']

#criando uma lista e removendo 'Shampoo' da lista
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista.remove('Shampoo') #Removendo string 
print(lista) #Saída: ['Sabonete', 'Sabão em Pó', 'Pasta de Dente', 'Esponja', 'Papel Higienico']

#criando uma lista e removendo 'Shampoo' da lista
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista.pop(2) #Remove o item na posição 2 (Shampoo)
print(lista) #Saída: ['Sabonete', 'Sabão em Pó', 'Pasta de Dente', 'Esponja', 'Papel Higienico']

#criando duas listas e unindo ambas
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista2 = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
lista_combinada = lista + lista2 #Unindo as listas
print(lista_combinada) #Saída: ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico', 'Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
print(lista_combinada[1:4]) #Saída ['Shampoo', 'Pasta de Dente', 'Esponja']

#criando duas listas, unindo ambas e exibindo quantos itens tem na lista
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista2 = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
lista_combinada = lista + lista2
print(len(lista_combinada)) #Saída 10

#criando duas listas, unindo ambas e exibindo em ordem numerica ou alfabetica
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista2 = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
lista_combinada = lista + lista2
lista_combinada.sort()#ordena a lista
print (lista_combinada)

#criando duas listas, unindo ambas e exibindo em ordem reversa numerica ou reversa alfabetica
lista = ['Sabonete', 'Shampoo', 'Pasta de Dente', 'Esponja', 'Papel Higienico']
lista2 = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
lista_combinada = lista + lista2
lista_combinada.sort()#odena a lista
lista_combinada.reverse()#inverte a lista
print (lista_combinada)

#sorteio
import random
#lista dos alunos
nomes = ['Lucas', 'Ana', 'Pedro', 'Maria', 'João']
#sorteio
escolhido = random.choice(nomes)
print(f'O aluno escolhido foi: {escolhido}')

#pedir os nomes do usuario e quando digitar sim para o programa e sorteia
import random
try:
    n1 = int(input('Quantos participantes irão participar do sorteio? '))   
    if n1 > 0:
        sorteio = []
        for i in range(n1):
            nome = input(f'Digite o nome do {i+1}° participante: ')
            sorteio.append(nome)
        print('O sorteio foi realizado e o ganhador é:')
        ganhador = random.choice(sorteio)
        print(ganhador)
    else:
        print('O programa suporta apenas números inteiros positivos.')
except ValueError:
    print('O programa suporta apenas números inteiros. Caracteres não são permitidos.')

#list.copy()
#faz uma cópia independente da lista (util para não alterar a lista original)
lista1 = [1, 2, 3]
lista2 = lista1.copy()
lista2.append(4)
print(lista1) #[1, 2, 3]
print(lista2) #[1, 2, 3, 4]

#list.clear()
#Remove todos os itens da lista (Deixa ela vazia)
carrinho = ['camisa', 'calça', 'sapato']
carrinho.clear()
print(carrinho)  # Saída: []
#list.reverse()
nomes = ['Ana', 'Carlos', 'Beatriz']
nomes.reverse()
print(nomes)  # Saída: ['Beatriz', 'Carlos', 'Ana']















#Exercicios Lista

'''✅ 1. Coloque itens nessa lista, modifique a estrutura do menu deixe o sistema do seu jeito.

compras = []

while True:
    print("\n===== LISTA DE COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Ver posição de um item")
    print("5 - Contar quantas vezes um item aparece")
    print("6 - Limpar lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        compras.append(item)
        print(f'"{item}" foi adicionado à lista.')
    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in compras:
            compras.remove(item)
            print(f'"{item}" foi removido.')
        else:
            print("Item não encontrado.")
    elif opcao == "3":
        print("\nSua lista de compras:")
        print(compras)
    elif opcao == "4":
        item = input("Digite o nome do item: ")
        if item in compras:
            print(f"O item '{item}' está na posição {compras.index(item)}.")
        else:
            print("Item não encontrado.")
    elif opcao == "5":
        item = input("Digite o item para contar: ")
        qtd = compras.count(item)
        print(f"O item '{item}' aparece {qtd} vezes na lista.")
    elif opcao == "6":
        compras.clear()
        print("Lista de compras esvaziada!")
    elif opcao == "0":
        print("Saindo... Até a próxima!")
        break
    else:
        print("Opção inválida. Tente novamente.")'''

compras = []

while True:
    print("\n===== LISTA DE COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Ver posição de um item")
    print("5 - Contar quantas vezes um item aparece")
    print("6 - Limpar lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        compras.append(item)
        print(f'"{item}" foi adicionado à lista.')

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in compras:
            compras.remove(item)
            print(f'"{item}" foi removido.')
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        if not compras:
            print('\nSua lista está vazia')
        else:
            print("\nSua lista de compras:")
            print(compras)

    elif opcao == "4":
        item = input("Digite o nome do item: ")
        if item in compras:
            print(f"O item '{item}' está na posição {compras.index(item)}.")
        else:
            print("Item não encontrado ou não existe.")

    elif opcao == "5":
        item = input("Digite o item para contar: ")
        qtd = compras.count(item)
        if qtd > 0:
            print(f"O item '{item}' aparece {qtd} vezes na lista.")
        else:
            print(f"O item '{item}' não existe na lista ou não foi encontrado.")

    elif opcao == "6":
        compras.clear()
        if not compras:
            print('A lista já está vazia')
        else:
            print("Lista de compras esvaziada!")

    elif opcao == "0":
        print("Saindo... Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")


#✅ 2. Criando uma lista com append()
#Enunciado:
# Peça ao usuário para digitar 5 nomes e adicione cada nome à lista usando .append().
# Depois, imprima a lista completa.

nomes = []
print ('Digite 5 nomes para serem exibidos na lista de forma alfabetica:')
for i in range(5):
    nome = (input(f'Digite o {i+1}° Nome: '))
    nomes.append(nome)
    nomes.sort()
print (nomes)

#✅ 3. Inserindo em posição específica
#Enunciado:
# Crie uma lista com 3 frutas.
# Depois use .insert() para adicionar uma fruta na posição 1.
# Mostre a nova lista.

lista = ['Uva', 'Banana', 'Maçã']
lista.insert(1, 'Morango')
print(lista)

#✅ 4. Removendo com remove()
#Enunciado:
# Crie uma lista de 4 cores.
# Peça ao usuário para digitar uma cor para remover da lista.
# Use .remove() e mostre a lista atualizada.

cor = ['Verde', 'Azul', 'Vermelho', 'Amarelo']
print (cor)
cor_remov = input('Digite uma cor Da lista para ser removida: ')
if cor_remov in cor:
    cor.remove(cor_remov)
    print(cor)
else:
    print('Cor não encontrada na lista')

#✅ 5. Removendo com pop()
#Enunciado:
# Crie uma lista com 5 números.
# Use .pop(2) para remover o número da terceira posição.
# Mostre o número removido e a lista atualizada.

Lista_num = [10, 20, 30, 40, 50]
print(f'Lista Completa', Lista_num)
print(f'O numero {Lista_num[2]} na terceira posição será removido')
Lista_num.pop(2)
print('Número removido! \nSua lista atual é: ', Lista_num)

#✅ 6. Verificando se um item está na lista
#Enunciado:
# Crie duas listas: uma de frutas e outra de legumes.
# Peça ao usuário para digitar o nome de um alimento.
# Use if e elif para verificar em qual lista ele está e imprima a resposta.

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
legumes = ["cenoura", "batata", "brócolis", "beterraba", "abobrinha"]
print ('Digite o nome de um alimento para verificar em qual lista está:')
alimento = (input('Alimento: '))
if alimento in frutas:
    print (f'{alimento}, está na lista frutas')
elif alimento in legumes:
    print (f'{alimento}, está na lista legumes')
else:
    print (f'{alimento}, não está em nenhuma das listas ou foi digitado incorretamente')

#✅ 7. Sorteando um nome com random.choice()
#Enunciado:
# Crie uma lista com nomes de 5 alunos.
# Use random.choice() para sortear um aluno e imprimir o nome sorteado.

import random
nomes = ['Rafael', 'Roger', 'Henrique', 'Arthur', 'Kayk']
escolhido = random.choice(nomes)
print(f'O aluno escolhido foi: {escolhido}')

#✅ 8. Contando repetições com count()
#Enunciado:
# Crie uma lista com vários números repetidos.
# Peça ao usuário para digitar um número e diga quantas vezes ele aparece na lista.

Numeros = [1, 2 ,3, 5, 6, 8 ,5 ,6, 9, 14, 24, 35, 1, 2, 9, 3, 2, 1]
print('Digite um número para saber quantas vezes ele aparece na lista:')
numero = int(input('Número escolhido: '))
quantidade = Numeros.count(numero)
print(f'O número {numero} repetiu {quantidade} vezes.')

#✅ 9. Encontrando a posição com index()
#Enunciado:
# Crie uma lista com nomes de cidades.
# Peça ao usuário para digitar o nome de uma cidade e diga qual a posição dela na lista usando .index().

cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Curitiba', 'Fortaleza', 'Recife']
print('Digite o nome de uma cidade para saber a posição dela na lista: ')
cidade = input('Cidade escolhida: ')
if cidade in cidades:
    posicao = cidades.index(cidade)
    print(f'A cidade "{cidade}" está na posição {posicao} da lista')
else:
    print(f'A cidade "{cidade}" não foi encontrada na lista')

#✅ 10. Limpando uma lista com .clear()
#Enunciado:
# Crie uma lista com qualquer conteúdo (animais, objetos, etc).
# Mostre a lista, depois use .clear() para esvaziá-la.
# Mostre a lista novamente.

objetos = ['celular', 'caderno', 'caneta', 'mochila', 'óculos']
print('Lista original de objetos:')
print(objetos)
objetos.clear()
print('\nLista após usar .clear():')
print(objetos)

#✅ 11. Mini menu interativo
#Enunciado:
# Monte um menu com input() onde o usuário pode:
#•	Adicionar um item
#•	Ver a lista
#•	Remover um item
#•	Sair do programa
#Use um while True: com if, elif e break.

compras = []

while True:
    print("\n===== LISTA DE COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        compras.append(item)
        print(f'"{item}" foi adicionado à lista.')

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in compras:
            compras.remove(item)
            print(f'"{item}" foi removido.')
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        if not compras:
            print('\nSua lista está vazia')
        else:
            print("\nSua lista de compras:")
            print(compras)
    elif opcao == "0":
        print("Saindo... Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")











#Tupla
#Tupla
#Tupla
#Tupla
#Tupla
#Tupla
#Tupla
#Tupla


#Tupla Simples
tupla = (10, 20, 30, 'teste')
a, b, c, d = tupla
print(a,b,c,d) #Saída: 10 20 30 teste


#Junção de duas ou mais Tuplas
tupla1 = (1, 'Tup1', 2)
tupla2 = (3, 'Tup2', 4)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada) #Saída: (1, 'Tup1', 2, 3, 'Tup2', 4)


#Repetindo a tupla
tupla = (1,2)
tupla_repetida = tupla * 3
print(tupla_repetida) #Saída: (1,2,1,2,1,2)


#Retornando o Maior valor da tupla
tupla = (1,5,3,7,2)
print(max(tupla)) #Saída: 7


#Retorna o Valor minimo da tupla
tupla = (1,5,3,7,2)
print(min(tupla)) #Saída: 1


#Retorna a soma dos numeros da tupla
tupla = (1,2,3,4)
print(sum(tupla)) #Saída: 10


#Count e Index
tupla = (1,2,3,2,4,2)
#Count
print(tupla.count(2))#Saída: 3 (o numero 2 aparece 3 vezes)
#Index
print(tupla.index(3))#Saída: 2 (posição do primeiro 3 da tupla)


#Puxa um local exato da tupla
minha_tupla = (1,2,3)
print(minha_tupla[0]) #Saída: 1
print(minha_tupla[-1])#Saída: 3 (último elemento) Numeros negativos contam na lista de tras pra frente


#Tupla dentro de Tupla
tupla_pessoas = (('Alice', 25), ('Bruno', 30), ('Carla', 22))
#Acessando a idade do segundo elemento (índice 1)
idade_segundo = tupla_pessoas[1][1]
print(f'A idade do segundo elemento é: {idade_segundo}')

#outro exemplo:
loc = (('Casa', -21.119574, -44.224794), ('Trabalho', -21.129347, -44.162196), ('Senac', -21.134943, -44.261105 ), ('Sitio', -21.048978, -44.200247))
latitude = loc[1][1]
longitude = loc[1][2]
dados = loc[1][0]
print(f'Seu local é: {dados}')
print(f'A latitude do {dados} o é: {latitude}')
print(f'A longitude do {dados} é: {longitude}')


#converter lista em tupla
lista = [1,2,3,4,5]
tupla = tuple(lista) #convertendo lista para tupla
print('Tupla convertida:', tupla)


#convertedo tupla em lista
tupla = (1,2,3,4,5)
lista = list(tupla) #convertendo  tupla para lista
print('Lista conveertida:', lista)


#ciar uma tupla com 8 nomes, converter em lista, criar estrutura de repetição pra digitar nomes  ,para continuar ou parada, voltar para tupla
tupla = ('Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena')
lista = list(tupla)
print('A Tupla é:', tupla)
print('Sua Tupla foi convertida para Lista')
print('A lista é:', lista) 
i=0 
while True:
    nome = (input(f'Digite o {i+1}° Nome: '))
    lista.append(nome)
    continuar = int(input('Digite 1 para continuar e 2 para parar : '))
    if continuar == 1:
        i += 1
    elif continuar == 2:
        print('A lista final é:', lista)
        print('Convertendo a lista para tupla')
        tupla = tuple(lista)
        print('A Tupla final é:', tupla)
        break
    else:
        print('Opção inválida, encerrando programa.')
        break














    #conjutos
    #conjutos
    #conjutos
    #conjutos
    #conjutos

#criação de conjunto
meu_conjunto = {1,2,3,4,5}
#ou 
meu_conjunto = set([1,2,3,4,5])

#Conjunto Vazio: Para criar um conjunto vazio, é necessário usar a função set().
#Usar {} cria  um dicionario vazio, não um conjunto vazio

conjunto_vazio = set()

#Acessando os elementos de um conjunto:
#como os conjuntos são não ordenados, não podemos acessar os elementos diretamente por indice. Para iterar sobre os elementos de um conjunto, usamos loops, como o for:

meu_conjunto = {1,2,3,4,5}
for item in meu_conjunto:
    print(item)

#adicionando elemento
meu_conjunto = {1,2,3,4,5}
meu_conjunto.add(6)
print(meu_conjunto) #saida {1,2,3,4,5,6}

#removendo elementos (se o elemento não existir será gerado um erro)
meu_conjunto = {1,2,3,4,5,6}
meu_conjunto.remove(3)
print(meu_conjunto) #saida {1,2,4,5,6}

#use discard() para remover um elemento, mas sem gerar erro caso o elemento não exista
#elemento não exista:
meu_conjunto = {1,2,3,4,5}
meu_conjunto.discard(10) #Não gera erro, mesmo que o 10 não esteja no conjunto
print(meu_conjunto) #saida {1,2,3,4,5}


#União de conjuntos
conj1 = {1,2,3,4}
conj2 = {3,4,5,6}
print('primeiro conjunto', conj1)
print('segundo conjunto', conj2)
uniao = conj1.union(conj2)
intersec = conj1.intersection(conj2)
difer= conj1.difference(conj2)
difer_simetrica = conj1.symmetric_difference(conj2)
print(uniao)
print(intersec)
print(difer)
print(difer_simetrica)


#Verificando se um elemento está no conjunto
frutas = {'maçã', 'banana', 'laranja'}
print('banana' in frutas) #Saída: True
print('uva' in frutas) #Saída: False


#Verificar se todos os elementos de A estão em B
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b)) #Saída: True (A é subconjunto de B)







#Dicionario
#Dicionario
#Dicionario
#Dicionario
#Dicionario
#Dicionario
#Dicionario

#voce pode criar um dicionario usando chaves {} ou a função dict {}
meu_dict = {'nome': 'joão', 'idade': 25, 'cidade': 'são paulo'}
#usando a função dict
meu_dict = dict(nome='joão', idade=25, cidade='são paulo')


#acessando elemento
meu_dict = dict(nome='joão', idade=25, cidade='são paulo')
print(meu_dict['nome']) #Saída: João
print(meu_dict['idade']) #Saída: 25
print(meu_dict['cidade']) #Saída: São Paulo


#adicionando ou alterando um valor
meu_dict = dict(nome='joão', idade=25, cidade='são paulo')
meu_dict['idade'] = 26 #modifica o valor da chave "idade"
meu_dict['profissao'] = 'Engenheiro' #adiciona um novo par de chav-valor
print(meu_dict)


#removendo elementos de um Dicionario
#Removendo uma chave com Del
meu_dict = dict(nome='joão', idade=25, cidade='são paulo')
del meu_dict['cidade']
print(meu_dict) #Saída: {'nome': 'joão', 'idade': 25}


#copiar um dicionario
novo_dict = meu_dict.copy()


#mesclar dois dicionarios
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2) 
print(dict1) #dict1 agora é {'a': 1, 'b': 2, 'c': 3, 'd': 4}


#verificar se uma chave existe
meu_dict = dict(nome='joão', idade=25, cidade='são paulo')
if 'nome' in meu_dict:
    print('nome está presente')


#dicionario aninhado
meu_dict = {
    'pessoa1': {'nome': 'João', 'idade': 25},
    'pessoa2': {'nome': 'Maria', 'idade': 30}
}
print(meu_dict['pessoa1']['nome']) #Saída: João


#Iterando sobre um dicionario
pessoa = {
    'nome': 'Ana',
    'idade': 30,
    'cidade': 'Belo Horizonte'
}

for chave in pessoa(): #interar somente a chave aqui no retorno do valor
    print(chave)
for valor in pessoa.values():  #aqui ja retorna somente o valor pois usamos o .values()
    print(valor)