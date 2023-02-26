import random

def validacpf():
    cont = 1
    for _ in range(100):
        cpf = ''
        for i in range(9):
            cpf += str(random.randint(0,9))

        c = 10
        n = []
        for i in str(cpf):
            n.append(int(i) * c)
            c = c -1

        digito_1 = int((sum(n) * 10) % 11)
        digito_1 = digito_1 if digito_1 <=9 else 0

        cpf_clear_2 = str(cpf) + str(digito_1)
        cpf_clear_2 

        c = 11
        n = []
        for i in cpf_clear_2:
            n.append(int(i) * c)
            c = c -1
        digito_2 = int((sum(n) * 10) % 11)
        digito_2 = digito_2 if digito_2 <=9 else 0

        print()
        print(f"{cont} - CPF criado:  {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{str(digito_1)}{str(digito_2)}")
        cont += 1
validacpf()            