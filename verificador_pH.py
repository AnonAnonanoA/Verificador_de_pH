#aqui a variável "entrada" armazena a entrada de dados (input) do tipo int
entrada = int(input("Insira o pH da agua: \n"))
#abaixo, o comando if atribui uma resposta caso a água tenha ph abaixo de 6 ou acima de 9.5
if entrada < 6 or entrada > 9.5:
    print('A água não está propicia para consumo!')
#aqui estamos contrapondo o if, deixando a possibilidade de um valor entre 6 e 9.5
else:
    print('A água está propicia para consumo!')