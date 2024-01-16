
print(        )
concatenacao = '2' + '2' + '2'
print(concatenacao)

a_dez_vezes = 'A' * 10
print(a_dez_vezes)
tres_vezes_amor = 'amor' * 3
print(tres_vezes_amor)
print(        )


# ordem de execução:
# 1. (1 + 1)
# 2. **
# 3. * /  //  %
# 4. + -

conta_1 = 1 + 1 ** 2 + 2  
print(conta_1)

nome = 'Samara'
idade = 19
peso = 52
altura = 1.60
imc = peso / altura ** 2

print(          )
print('Nome: ' , nome)
print('idade: ', idade)
print('peso: ', peso)
print('altura: ', altura)
print(imc)

print(    )

linha_1 = f'{nome} tem {altura: .2f} de altura'
linha_2 = f'{nome} pesa {peso: .2f}'
linha_3 = f'{imc: .2f}'
print(linha_1)
print(linha_2)
print(linha_3)
print('Seu imc é: ' , linha_3, end = '')