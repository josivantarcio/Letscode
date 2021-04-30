def relacao(lista):
    """Crie uma função que recebe uma lista de números reais e retorna uma outra lista de tamanho 3 em que 
    (i) o primeiro elemento é a quantidade de números maiores que zero, 
    (ii) o segundo elemento é a quantidade de números menores que zero e 
    (iii) o último elemento é a quantidade de zeros da lista inicial.

    Args:
        lista (list): lista recebida para ser processada pela funcao

    Returns:
        list: lista com tamanho três na ordem (maiores, menores e iguais a zero)
    """
    maior = menor = igual = 0
    for i in lista:
        if i > 0:
            maior += 1
        elif i < 0:
            menor += 1
        else:
            igual += 1
    return f'[{maior},{menor},{igual}]'


lista = []
relacao(lista)
print(relacao(lista))