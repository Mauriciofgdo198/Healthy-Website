import random
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto aluno? '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('Os alunos são: {}, {}, {} e {}.'.format(a1, a2, a3, a4, ))
print('A ordem sera: ')
print(lista)
