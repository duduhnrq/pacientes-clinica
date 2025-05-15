# Desafio - Sistema de Gestão de Pacientes em Clínica Médica
def cadastrar_paciente():
    nome = str(input('Nome do paciente: '))
    idade = int(input('Idade do paciente: '))
    especMed = int(input('Especialidade Médica:\n\n1 - Cardiologia\n2 - Pediatria\n3 - Clínica geral\n\n'))

    match especMed: 
        case 1:
            especMed = 'Cardiologia'
            valor = 200
        case 2:
            especMed = 'Pediatria'
            valor = 150
        case 3:
            especMed = 'Clínica geral'
            valor = 100
        case _:
            print('Inválido')

    convenio = int(input('Convênio:\n\n1 - Sim\n2 - Não\n\n'))

    match convenio:
        case 1:
            convenio = 'Sim'
            valor = valor / 2
        case 2:
            convenio = 'Não'
            valor = valor / 2
        case _:
            print('Inválido')

def 

opcao = int(input('Desejar cadastrar um paciente?\n\n1 - Sim\n2 - Não\n\n'))

if opcao == 1:
    cadastrar_paciente()
else:
    exit()
    