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
    'cidade': 'Belo Horizonte'}
for chave in pessoa(): #interar somente a chave aqui no retorno do valor
    print(chave)
for valor in pessoa.values():  #aqui ja retorna somente o valor pois usamos o .values()
    print(valor)


#interar chaves e valores juntos
pessoa = {
    'nome': 'Ana',
    'idade': 30,
    'cidade': 'Belo Horizonte'}
for chave, valor in pessoa.items():
    print({chave}, {valor}) #Saída: nome: Ana, idade: 30, cidade: Belo Horizonte


#input com dicts
pessoa = {}
pessoa['nome'] = input('digite o seu nome: ')
pessoa['idade'] = int(input('digite sua idade: '))
pessoa['cidade'] = input('digite a sua cidade: ')
print(pessoa)

#desafio
#desafio
#desafio
#desafio
#desafio
#desafio


#um dicionario de inicio com pre definido "nome, idade, cidade, peso" , pedir print pra mostar o dicionario, alterar os dados pelos meus dados.
print('======'*20)
pessoa = {'nome': '_', 'idade': '_', 'cidade': '_', 'peso': '_'}

print('Seu Dicionario atual é:', pessoa, '\n')
pessoa['nome'] = 'Thauã'
pessoa['idade'] = '21'
pessoa['cidade'] = 'Santa Cruz'
pessoa['peso'] = '79'

print('Dicionario Thauã: ', pessoa, '\n')

print('Agora vamos atualizar com seus dados: ', pessoa, '\n')
pessoa['nome'] = input('Digite o seu nome: ')
pessoa['idade'] = int(input('Digite sua idade: '))
pessoa['cidade'] = input('Digite a sua cidade: ')
pessoa['peso'] = float(input('Digite o seu peso: '))
print('Dicionario Atualizado: ', pessoa)
print('======'*20)





#input com dicts:
pessoas = []
while True:
    pessoa = {}
    pessoa['nome'] = input('digite o seu nome: ')
    pessoa['idade'] = int(input('digite sua idade: '))
    pessoa['cidade'] = input('digite a sua cidade: ')

    pessoas.append(pessoa)

    continuar = input('deseja adicionar outra pessoa? (s/n) \n')
    if continuar.lower == 's':
        continue
    elif continuar.lower == 'n':
        print('Fim do Programa')
        break
    else:
        print('Opção inválida, encerrando programa.')
        break

print('\nLista de pessoas cadastradas:')
for p in pessoas:
    print(p)


#chamando um dicionario dentro de outro dicionario
alunos = {}
while True:
    matricula = input('Digite a matrícula do aluno: ')

    nome = input('Digite o nome do aluno: ')
    idade = int(input('Digite a idade do aluno: '))
    curso = input('Digite o curso do aluno: ')

    alunos[matricula] = {'nome': nome, 'idade': idade, 'curso': curso} #criando o dicionario dentro do dicionario
    continuar = input('Deseja adicionar outro aluno? (s/n) ')
    if continuar.lower() != 's':
        break
    #exibindo os alunos cadastrados
print('Lista de alunos cadastrados:')
for mat, dados in alunos.items():
    print(f'matricular: {mat}')   
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')
    



#TUPLA, CONJUNTO e  DICIONARIO 
#TUPLA, CONJUNTO e  DICIONARIO 
#TUPLA, CONJUNTO e  DICIONARIO 
#TUPLA, CONJUNTO e  DICIONARIO 
#TUPLA, CONJUNTO e  DICIONARIO 
#TUPLA, CONJUNTO e  DICIONARIO 


#1.	Crie uma tupla com 5 números inteiros e exiba o maior e o menor valor.

tupla = (10, 20, 30, 40, 50)
maior = max(tupla)
menor = min(tupla)
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')

#2.	Solicite ao usuário 5 nomes e armazene-os em uma tupla. Em seguida, exiba os nomes em ordem alfabética.

tupla = ()
i=0
for i in range(5):
    nome = (input(f'Digite o {i+1} nome: '))
    tupla += (nome,)
print(sorted(tupla))

#3.	Dada a tupla numeros = (10, 20, 30, 40, 50), crie uma nova tupla com os valores ao quadrado.(sem fazer de forma manual)

tupla = (10, 20, 30, 40, 50)
tupla_quadrada= tuple(x**2 for x in tupla)
print(f'Os valores, {tupla} ao quadrado são respectivamentes, {tupla_quadrada}')

#4.	Crie uma tupla de números e retorne a média dos valores.

tupla = ()
print("Digite 10 números para fazer uma media:")
for i in range(10):
    num = int(input(f"Digite o número {i+1}: "))
    tupla += (num,)
media = sum(tupla) / len(tupla)
print(f"A média dos números é: {media}")

#5.	Verifique se um elemento informado pelo usuário está presente dentro de uma tupla predefinida.

tupla = (1,2,3,2,4,2)
n1 = int(input('Digite o numero que seseja saber se esta na tupla: \n'))
n2 = tupla.count(n1)
if n2 != 0: 
    print('O numero não aparece na lista')
else:
    print('O numero aparece na lista')

#6.	Crie dois conjuntos com números de 1 a 10 e de 5 a 15. Exiba a união, interseção e diferença entre eles.

tupla1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
tupla_uni = set(tupla1) | set(tupla2)
print("União:", sorted(tupla_uni))
tupla_inter = set(tupla1) & set(tupla2)
print("Interseção:", sorted(tupla_inter))
tupla_diff = set(tupla1) ^ set(tupla2)
print("Diferença:", sorted(tupla_diff))

#7.	Peça ao usuário para digitar 10 números (permitindo repetições). Armazene em um conjunto e exiba apenas os números únicos.

tupla = []
print('Digite 10 numeros para serem exibidos sem repetição:')
for i in range(10):
    num = int(input(f'Digite o {i+1}° numero: '))
    if num not in tupla:
        tupla += (num,)
print(f'Seus numeros sem repetição são: {sorted(tupla)}')

#8.	Verifique se dois conjuntos têm ao menos um elemento em comum. Caso positivo, mostre os elementos comuns.

tupla1 = [25, 96, 33, 58, 67, 15]
tupla2 = [25, 66, 56, 27, 36, 18]
print(tupla1)
print(tupla2)
tupla_comum = set(tupla1) & set(tupla2)
print("As duas listas tem em comum o numero:", sorted(tupla_comum))

#9.	Remova elementos repetidos de uma lista utilizando um conjunto.

tupla1 = [25, 96, 33, 58, 67, 15]
tupla2 = [25, 66, 56, 27, 36, 18]
tupla_uni = set(tupla1) | set(tupla2)
tupla_comum = set(tupla1) & set(tupla2)
tupla_remov = set(tupla_uni) - set(tupla_comum) #Resultado removerá o 25
print(sorted(tupla_remov))

#10.	Dado um conjunto de palavras, conte quantas palavras únicas ele contém.

palavras = ['mamão, abacate, morango, morango, maçã, abacaxi, abacate, abacaxi']
palavras_lista = palavras[0].split(', ')
palavras_unicas = set(palavras_lista)
print(f'Quantidade de palavras únicas: {len(palavras_unicas)}')

#11.	Crie um dicionário com 5 alunos e suas respectivas notas. Calcule e exiba a média de cada aluno.

notas = {
    'Lucas': [8, 7, 9],
    'Ana': [10, 9, 8],
    'Pedro': [6, 7, 5],
    'Maria': [9, 10, 9],
    'João': [7, 8, 6]
}
for aluno, notas_aluno in notas.items():
    media = sum(notas_aluno) / len(notas_aluno)
    print(f'A média de {aluno} é: {media:.2f}')

#12.	Solicite ao usuário nome e idade de 5 pessoas e armazene em um dicionário. Em seguida, exiba apenas as pessoas maiores de idade.

pessoas = []
print('Digite o nome e a idade de 5 pessoas:')
for i in range(5):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    idade = int(input(f'Digite a idade de {nome}: '))
    pessoas.append({'nome': nome, 'idade': idade})
print('\nPessoas maiores de idade:')
maiores = [p for p in pessoas if p['idade'] >= 18]
if maiores:
    for p in maiores:
        print(f'{p["nome"]} - {p["idade"]} anos')
else:
    print('Não há pessoas maiores de idade.')

#13.	Crie um dicionário com os meses do ano como chave e a quantidade de dias como valor. Depois, permita que o usuário digite um mês e informe a quantidade de dias.

meses = {
    'janeiro': 31,
    'fevereiro': 28,
    'março': 31,
    'abril': 30,
    'maio': 31,
    'junho': 30,
    'julho': 31,
    'agosto': 31,
    'setembro': 30,
    'outubro': 31,
    'novembro': 30,
    'dezembro': 31
}
mes = input('Digite o mês: ').strip().lower()
if mes in meses:
    print(f'O mês de {mes} tem {meses[mes]} dias.')
else:
    print('Mês inexistente ou digitado incorretamente.')

#14.	Cadastro de produtos (com while) (Até o usuário digitar Sair deve ser cadastro os produtos)

produtos = {}
codigo = 1
while True:
    nome = input('Digite para cadastar os proutos: \n')  
    produtos[codigo] = {'nome': nome} 
    codigo += 1

    continuar = input('Deseja adicionar outro produto? (s/n): ')
    if continuar.lower() != 's':
        break
print('Lista dos produtos cadastrados: ')
for cod, info in produtos.items():
    print(f'Código: {cod} - Nome: {info["nome"]}')

#15.	Soma dos valores do dicionário (com while) Crie um Carrinho de compras aonde você insere os produtos no dicionário por input e seu preço no final você deve calcular o valor de todos os produtos.

produtos = {}
item = 1
valor_total_compra = 0
while True:
    nome = input('Digite o nome do prouto: \n')  
    valor = float(input('Digite o valor do produto: \n'))
    quantidade = int(input('Digite a quantidade do produto: \n'))
    produtos[item] = {'nome': nome, 'valor': valor, 'quantidade': quantidade}
    valor_total_produto = valor * quantidade 
    valor_total_compra += valor_total_produto    
    item += 1
    print(f'Produto {nome} adicionado com sucesso!')
    continuar = input('Deseja adicionar outro produto? (s/n): ')
    if continuar.lower() != 's':
        break
print('Lista dos produtos cadastrados:\n ')
for ite, info in produtos.items():
    print(f'Item: {ite} - Nome: {info["nome"]}, Quantidade: {info["quantidade"]}, Valor: R${info["valor"]:.2f}')
print(f'Valor total da compra: R${valor_total_compra:.2f}')






#Orientação Objeta
#Orientação Objeta
#Orientação Objeta
#Orientação Objeta
#Orientação Objeta






class Produto: # Definição da classe Produto

  def __init__(self, nome, preco, quantidade,): # Método construtor da classe, que inicializa os atributos nome, preco e quantidade
    self.nome = nome
    self.preco = preco
    self.quantidade = quantidade

  def mostrar_info(self): # Método para mostrar as informações do produto
    print(f"Nome: {self.nome}")
    print(f"Preço: R${self.preco}")
    print(f"Quantidade: {self.quantidade}")

  def mostrar_valor_total_estoque(self): # Calcula a multiplicação do preço pela quantidade e mostra o valor total de estoque do produto
    valor_total = self.preco * self.quantidade
    print(f"O valor total de estoque deste produto é R${round(valor_total, 2)}")

print('=='*30) # Separador para melhor visualização

p1 = Produto("Água", 1.99, 20) # Criação de uma instância da classe Produto, chamada produto1.
p1.mostrar_info() # Saída: Nome: Água , Preço: R$1.99 , Quantidade: 20
p1.mostrar_valor_total_estoque() # Saída: O valor total de estoque deste produto é R$39.8

print('=='*30) # Separador para melhor visualização

p2 = Produto("Refrigerante", 4.99, 25) # Criação de outra instância da classe Produto, chamada produto2.
p2.mostrar_info() # Saída: Nome: Refrigerante , Preço: R$4.99 , Quantidade: 25
p2.mostrar_valor_total_estoque() # Saída: O valor total de estoque deste produto é R$124.75

print('=='*30) # Separador para melhor visualização

#Pilares da programação orientada a objetos:
# - Abstração: A classe Produto abstrai as características de um produto, como nome, preço e quantidade.
# - Encapsulamento: Os atributos e métodos da classe Produto estão encapsulados dentro da classe, protegendo os dados e a lógica de implementação.
# - Herança: Poderíamos criar subclasses de Produto, como ProdutoPerecivel ou ProdutoDuravel, que herdam os atributos e métodos da classe Produto.
# - Polimorfismo: Poderíamos ter métodos com o mesmo nome em diferentes classes, mas com implementações diferentes, permitindo que objetos de diferentes classes sejam tratados de forma intercambiável.



#Continuar 
#Cadastro de Alunos

'''class Alunos:

  def __init__(self, nome ,matricula, ano):
    self.matricula = matricula
    self.nome = nome
    self.ano = ano

  def mostrar_info(self):
    print(f'Matricula: {self.matricula}')
    print(f'Aluno :{self.nome}')
    print(f'Sala: {self.ano}')

class Dados:  
  
  def __init__(self):
        self.lista_alunos = []
  i=0   
  print('Digite os Seguintes dados para cadastro:\n')
  for i in range(1):
    matricula = i+1
    print('Matricula:', matricula)
    nome = input(f'Digite o nome do aluno:\n')
    ano = int(input('Digite o ano escolar do aluno:\n'))
    if continuar.lower() == 's':
      aluno = Alunos(nome, matricula, ano)
      aluno.mostrar_info()
      lista_alunos.append(aluno)
    else:
      print('Cadastro encerrado.')
      break'''


#Professor

class Professor:
    def __init__(self, nome,):
        self.nome = nome
        self.metaprofessor = 0

    def definir_meta (self, meta):
        self.metaprofessor = meta
            
    def metabatida(self, batida):
        if batida >= self.metaprofessor:
            print(f"Meta do professor {self.nome} atingida!\n")
        else:
            print(f"Meta do professor {self.nome} não atingida!\n")

professor1 = Professor("Ricardo")
professor1.definir_meta(10)
professor1.metabatida(12)

professor2 = Professor("Saulo")
professor2.definir_meta(10)
professor2.metabatida(8)

#livraria

class Livro:
    def __init__(self, nome, autor, edicao, quantidade):
        self.nome = nome
        self.autor = autor
        self.edicao = edicao
        self.quantidade= quantidade
        
    def exibir_livros(self):
        print(f"O {self.nome} do {self.autor} da {self.edicao}º edição.\n")
        
class Registro:
    def __init__(self):
        self.livros = []
        
    def cadastro_livro(self):
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o nome do autor: ")
        edição = int(input("Digite a edição do seu livro sem °, apenas numeros "))
        quantidade= int(input("Digite quantos livros iram ser registrados: "))
        
        novo_livro= Livro(nome, autor, edição, quantidade)
        self.livros.append(novo_livro)
        print(f"O livro {nome} foi cadastrado. \n")
    
    def disponibilidade(self):
        disponivel = input("Digite o nome do livro que voce quer verificar a disponibilidade: ")
        for disponivel in self.livros:
        
             print(f"O livro {disponivel.nome} esta disponivel com {disponivel.quantidade}")
            
sistema =  Registro()
for i in range(2):
    print("Vamos registrar um livro ")
    sistema.cadastro_livro()
    print("O livro cadastrado é: ")
for livro in sistema.livros:
    livro.exibir_livros()
sistema.disponibilidade()







#Exercicios POO
#Exercicios POO
#Exercicios POO
#Exercicios POO
#Exercicios POO
#Exercicios POO







#🚀Exercício 1 – Classe Carro
#Crie uma classe chamada Carro com os atributos:
#• marca, modelo, ano, velocidade.
#Crie os seguintes métodos:
#• acelerar(): aumenta a velocidade em 10 km/h.
#• frear(): diminui a velocidade em 10 km/h, sem deixar negativa.
#• mostrar_dados(): exibe todos os dados do carro e a velocidade atual.

class Carro:
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        
    def acelerar(self):
        self.velocidade += 10
        print(f"\nVelocidade atual: {self.velocidade} km/h")

    def frear(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = 0
        print(f"\nVelocidade atual: {self.velocidade} km/h")

    def velocidade_atual(self):
        print(f"\nVelocidade atual: {self.velocidade} km/h")
    
marca = input ('Marca do carro: \n')
modelo = input ('Modelo do carro: \n')
ano = input ('Ano do carro: \n')

Carro = Carro(marca, modelo, ano)

while True:
    print('\n')
    print('Digite um dos numeros para prosseguir:')
    print('1 - Aceler:')
    print('2 - Frear')
    print('3 - Velocidade atual')
    print('4 - Sair')

    opcao = input('Escolha uma opção:')

    if opcao == '1':
        Carro.acelerar()
    elif opcao == '2':
        Carro.frear()
    elif opcao == '3':
        Carro.velocidade_atual()
    elif opcao == '4':
        break
    else:
        print('\nOpção invalida, Tente novamente')


#🎓Exercício 2 – Classe Aluno
#Crie uma classe chamada Aluno com os atributos:
#• nome, idade, notas (lista de 3 notas).
#Crie os métodos:
#• media(): retorna a média das 3 notas.
#• situacao(): retorna “Aprovado” se a média for maior ou igual a 7, senão
#“Reprovado”.
#• apresentar(): imprime nome, idade e média.

class Aluno:
    def __init__(self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def media(self):
        return sum(self.notas) / 3
    

    def situacao(self):
        if self.media() >= 7:
            return(f"{self.nome} foi Aprovado")
        else:
            return(f"{self.nome} foi Reprovado")

    def apresentar(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Média atual é: {self.media():.1f}")
        print(f"Situação: {self.situacao()}")

nome = input('Nome do Aluno: \n')
idade = input('Idade do Aluno: \n')
nota1 = float(input('Nota 1: \n'))
nota2 = float(input('Nota 2: \n'))
nota3 = float(input('Nota 3: \n'))
notas = [nota1, nota2, nota3]

aluno = Aluno(nome, idade, notas)
aluno.apresentar()

#Exercício 3 – Classe Produto
#Crie uma classe Produto com:
#• nome, preco, quantidade.
#Métodos:
#• comprar(qtd): aumenta a quantidade em estoque.
#• vender(qtd): reduz a quantidade (se houver estoque suficiente).
#• mostrar_estoque(): imprime nome, quantidade e valor total em estoque.

class Produto:
    def __init__(self, nome, preco, quantidade=0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def comprar(self, qtd):
        
        self.quantidade += qtd
        print(f"Quantidade comprada: {qtd}")
        
    def vender(self, qtd):
        
        if qtd > self.quantidade:
            print("Quantidade insuficiente em estoque.")
            return
        self.quantidade -= qtd
        valor_total = self.preco * qtd
        print(f"Nome do produto: {self.nome}")
        print(f"Quantidade em estoque: {self.quantidade}")
        print(f"Quantidade vendida: {qtd}")
        print(f"Valor total da venda: R$ {valor_total:.2f}")
        
    def mostrar_estoque(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Quantidade em estoque: {self.quantidade}")
        valor_total = self.preco * self.quantidade
        print(f"Valor total em estoque: R$ {valor_total:.2f}")

nome = input("Digite o nome do produto: ")

while True:
    try:
        preco = float(input("Digite o preço do produto: "))
        if preco < 0:
            print("O preço não pode ser negativo.")
            continue
        break
    except ValueError:
        print("Por favor, insira um valor numérico válido.")

while True:
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
        if quantidade < 0:
            print("A quantidade não pode ser negativa.")
            continue
        break
    except ValueError:
        print("Por favor, insira um número inteiro válido.")


produto = Produto(nome, preco, quantidade)
produto.mostrar_estoque()

while True:
    print("\n--- Menu ---")
    print("1 - Comprar")
    print("2 - Vender")
    print("3 - Mostrar estoque")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")
    print('\n')

    if opcao == '1':
        try:
            qtd = int(input("Quantidade a comprar: "))
            produto.comprar(qtd)
        except ValueError:
            print("Digite um número inteiro válido.")
    elif opcao == '2':
        try:
            qtd = int(input("Quantidade a vender: "))
            produto.vender(qtd)
        except ValueError:
            print("Digite um número inteiro válido.")
    elif opcao == '3':
        produto.mostrar_estoque()
    elif opcao == '4':
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")

#🕒Exercício 4 – Classe Relógio
#Crie uma classe Relogio com:
#• hora, minuto.
#Métodos:
#• ajustar(h, m): define a hora e o minuto.
#• avancar_minuto(): avança 1 minuto, ajustando a hora se passar de 60.
#• mostrar_hora(): imprime a hora formatada (ex: 14:05).

class Relogio:
    def __init__(self, dia=0, hora=0, minuto=0):
        self.dia = dia
        self.hora = hora
        self.minuto = minuto

    def avancar_minuto(self):
        self.minuto += 1
        if self.minuto >= 60:
            self.minuto = 0
            self.hora += 1
            self.avancar_hora()

    def avancar_hora(self):
        if self.hora >= 24:
            self.hora = 0
            self.dia += 1

    def mostrar(self):
        print(f'\nDia: {self.dia}, {self.hora}:{self.minuto:02d}')



dia = input ('Digite a quantidade de Dias : \n')
hora = input ('Digite a Hora : \n')
minuto = input('Digite o Minuto : \n')

relogio = Relogio(dia, hora, minuto)

while True:
    print('\n')
    print('Digite um dos numeros para prosseguir:')
    print('1 - Mudar Data:')
    print('2 - Mudar Hora')
    print('3 - Mudar Minuto')
    print('4 - Mostrar Hora')
    print('5 - Sair')

    opcao = input('Escolha uma opção:')

    if opcao == '1':
        Relogio.Dia()
    elif opcao == '2':
        Relogio.Hora()
    elif opcao == '3':
        Relogio.Minuto()
    elif opcao == '4':
        relogio.mostrar()
    elif opcao == '5':
        break
    else:
        print('\nOpção invalida, Tente novamente')
