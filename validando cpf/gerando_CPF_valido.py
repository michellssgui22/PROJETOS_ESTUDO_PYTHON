import re

def validacpf():
    cpf = input("Digite 9 números aleatórios: ")

    cpf = re.sub(
        r'[^0-9]',
        '',
        str(cpf)
    )

    cpf_clear = cpf
    #Verificando se não se trata de caracteres repetidos
    caracter_1 = cpf_clear[0]
    teste = len(cpf_clear) * caracter_1
    if cpf_clear == teste:
        print()
        print('Caracteres repedidos não são válidos!')
        print()
        return validacpf()
    elif len(cpf_clear) > 9 or len(cpf_clear) < 9:
        print()
        print('É necessário que sejam informado 9 números exatamente!')
        print()
        return validacpf()
    else:
        c = 10
        n = []
        for i in cpf_clear :
            n.append(int(i) * c)
            c = c -1

        digito_1 = int((sum(n) * 10) % 11)
        digito_1 = digito_1 if digito_1 <=9 else 0

        cpf_clear_2 = cpf_clear + str(digito_1)
        cpf_clear_2

        c = 11
        n = []
        for i in cpf_clear_2 :
            n.append(int(i) * c)
            c = c -1
        digito_2 = int((sum(n) * 10) % 11)
        digito_2 = digito_2 if digito_2 <=9 else 0

        print()
        print(f"O CPF criado é:  {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{str(digito_1)}{str(digito_2)}")

validacpf()            