def  resgistro () :


    cadastro = list()
    pessoas = int(input ("quantas pessoas voce quer cadastrar??"))
    for p in range (pessoas):
        clientes = dict ()
        dados_nome = input ("qual o nome do usuario??")
        dados_idade = int(input ("qual é idade do usuario??") )
        dados_sexo = input ("qual é o sexo do usuario??")
        dados_DDN = input ("qual é a data de nascimento do usuario??")
        clientes["nome"]=  dados_nome
        clientes ["idade"]= dados_idade
        clientes ["sexo"]= dados_sexo
        clientes ["data de nascimento"]= dados_DDN
        cadastro.append(clientes)
    return cadastro
dados = resgistro()

maioridade = 0
menoridade = 0
maior_idade = 0

for clientes in dados : 
    if clientes ["idade"]>=18:
        maioridade += 1
    else:
        menoridade  += 1

    if clientes ["idade"] > maior_idade:
        maior_idade = clientes ["idade"]
        cliente_mais_velho =clientes["nome"]

print (dados)
print(f"Maiores de idade: {maioridade}, Menores de idade: {menoridade}")
print(f"O cliente mais velho é: {cliente_mais_velho}")







