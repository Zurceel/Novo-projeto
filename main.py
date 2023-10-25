def somar(numero1, numero2):
    print(f'Realizanado soma de {n1} + {n2}')
    resultado = numero1 + numero2
    return resultado

def subtrair(numero1, numero2):
    print(f'Realizanado subtraçãp de {n1} - {n2}')
    resultado = numero1 - numero2
    return resultado

def multiplicacao(numero1, numero2):
    print(f'Realizanado multiplicação de {n1} * {n2}')
    return numero1 * numero2

def divisao(numero1, numero2):
    print(f'Realizanado divisão de {n1} / {n2}')
    return numero1 / numero2

if __name__ == '__main__':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    op = input('Qual operação matemática deseja realizar? (+, -, /, *)')

    resultado = 0

    if op == '+':
        resultado = somar(n1, n2)
    elif op == '-':
        resultado = subtrair(n1, n2)
    elif op == '*':
        resultado = multiplicacao(n1, n2)
    elif op == '/':
        resultado = divisao(n1, n2)

    else:
        print('Operador incorreto')

    print(f'O resultado da operação é {resultado}')

