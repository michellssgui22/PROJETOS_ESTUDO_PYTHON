import re

cpf = input("Informe o CPF para validação: ")

cpf = re.sub(
    r'[^0-9]',
    '',
    str(cpf)
)
#cpf= cpf_clear[::-1]
cpf_clear = cpf[:9]
cpf_clear 

#Verificando se não se trata de caracteres repetidos
caracter_1 = cpf_clear[0]
teste = len(cpf_clear) * caracter_1
if cpf_clear == teste:
    print('CPF inválido')
else:
    c = 10
    n = []
    for i in cpf_clear :
        n.append(int(i) * c)
        c = c -1

    digito_1 = (sum(n) * 10) % 11
    digito_1 = digito_1 if digito_1 <=9 else 0

    cpf_clear_2 = cpf_clear + str(digito_1)
    cpf_clear_2

    c = 11
    n = []
    for i in cpf_clear_2 :
        n.append(int(i) * c)
        c = c -1
    digito_2 = (sum(n) * 10) % 11
    digito_2 = digito_2 if digito_2 <=9 else 0

    valida_cpf = cpf_clear + str(digito_1) + str(digito_2)

    if cpf == valida_cpf:
        print()
        print(f"O CPF informado, {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{str(digito_1)}{str(digito_2)}, é válido!")
    else:
        print()
        print(" >>>> CPF inválido! <<<<")