#teste print
print("Olá, mundo")


#teste arredondamento
print(f'Preço: R${25.65879:.0f}')
print(f'Preço: R${25.65879:.1f}')
print(f'Preço: R${25.65879:.2f}')
print(f'Preço: R${25.65879:.3f}')
print(f'Preço: R${25.65879:.4f}')
print(f'Preço: R${25.65879:.5f}')


#teste digitar e exibir nome
nomes = input ('Qual o seu nome?   ')
print ('Olá' ,nomes)


#teste digitar e exibir idade
idades = int(input('Qual a sua idade?   '))
print(f'Sua idade é {idades} anos')


#teste digitar 2 numeros, somar e mostrar o resultado
print ('Digite 2 Numeros para Somar')
numeros1 = int(input('digite o primeiro numero:   '))
numeros2 = int(input('digite o segundo numero:   '))
soma = numeros1 + numeros2
print('sua soma é',soma)


#digitar nome e idade na mesma linha e exibir em uma mensagem
nome, idade =input('digite seu nome e idade, separadas por espaço:   ').split()
idade= int(idade)
print(f'Olá, {nome}! Você tem {idade} anos.')

#divisão de 2 numeros
print ('Divisão')
numerod1 = float(input('digite o numero para ser dividido:   '))
numerod2 = float(input('digite por quanto será dividido:   '))
divmod = numerod1 / numerod2
print('o Resultado da sua divisão é',divmod)

#media
print ('Media')
print ('digite seus numeros para ter uma media')
nota1 = float(input('digite a primeira nota:   '))
nota2 = float(input('digite a segunda nota:   '))
nota3 = float(input('digite a terceira nota:   '))
nota4 = float(input('digite a quarta nota:   '))
nota5 = float(input('digite a quinta nota:   '))
soma = nota1 + nota2 + nota3 + nota4 + nota5
media = soma / 5
print('a media é',media)

