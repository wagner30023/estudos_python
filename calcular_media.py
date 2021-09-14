print('==================================================== ')
print(' Bem vindo ao sistema de notas')
print('==================================================== ')

nome = input(" Nome do aluno: ")
materia = input('Materia: ')
# status = bool

nota1 = float(input('Nota 1 : '))
nota2 = float(input('Nota 2 : '))
nota3 = float(input('Nota 3 : '))
nota4 = float(input('Nota 4: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aluno: ", nome)
    print("Matéria: ", materia)
    print("Média: ", media)
    print("status: Aprovado")
else:
    print("Aluno: ", nome)
    print("Matéria: ", materia)
    print("Média: ", media)
    print("status: Reprovado")
