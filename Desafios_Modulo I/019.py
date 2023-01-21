#um professor quer sortear um dos seus quat
# ro alunos para apgar o quadro. faça um programa que ajude ele,
#  lendo o deles e escrevendo o nome do escolhido
import random
nome1 = str(input('Aluno 1: '))
nome2 = str(input('Aluno 2: '))
nome3 = str(input('Aluno 3: '))
nome4 = str(input('Aluno 4: '))
n = random.randint(1,4)
if(n == 1):{
    print(nome1)
}
if(n == 2):{
    print(nome2)
}
if(n == 3):{
    print(nome3)
}
if(n == 4):{
    print(nome4)
}

