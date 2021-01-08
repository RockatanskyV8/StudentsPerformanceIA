import math
from numpy import absolute

def trimmed_mean(lst, p):
    trim = int( len(lst) * p )          # multiplica o comprimento de lst por um valor entregue pelo usuário
    trimmed_lst = lst[trim:trim * (-1)] # remove o primeiro(s) e ultimo(s) emementos da lista de acordo com a quantidade
    return mean(*trimmed_lst)           # retorna a média dos args restantes

def mean(*args):
    val_sum = sum(args)         # soma todos os valores
    return val_sum / len(args)  # divide o resultado da soma pela quantidade de elementos
 
def median(*args):
    if len(args) % 2 == 0: # se o numero de args for impar
        i = round((len(args) + 1) / 2)  # divide numero de args por 2, arredonda e atribui ao i
        j = i - 1                       # subtrai um da variável i
        return (args[i] + args[j]) / 2  # soma os args da posição i e j e divide por 2
    else:
        k = round(len(args) / 2)        # divide numero de args por 2
        return args[k]                  # retorna o arg na posição k'

def mad(*args):
    # Tira a mediana de todos os args
    dataset_median = median(*args)
    # tira a meidana do valor absoluto de cada arg menos a dataset_median
    return median(*[ absolute(arg - dataset_median) for arg in args ])

def standard_deviation(*args):
    #tira a raiz quadrada da variancia dos args
    return math.sqrt(variance(*args))

def variance(*args):
    #Tira a média dos argumentos
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        # atribuido a variavel numerador
        # (valor - média) ² 
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
    # divide numerador para denominador
    return numerator / denominator

def correlation_coefficient(*args):
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their standard deviations
    list_1_sd = standard_deviation(*list_1[0])
    list_2_sd = standard_deviation(*list_2[0])
    # print(f"L1 SD : {list_1_sd}")
    # print(f"L2 SD : {list_2_sd}")
    denominator = list_1_sd * list_2_sd
    # Get the covariance
    numerator = covariance(*args)
    return numerator / denominator

def standard_deviation(*args):
    return math.sqrt(variance(*args))

def coefficient_variation(*args):
    return standard_deviation(*args) / mean(*args)

def covariance(*args):
    # Use a list comprehension to get all values
    # stored in the 1st & 2nd list
    list_1 = [i[0] for i in args]
    list_2 = [i[1] for i in args]
    # Pass those lists to get their means
    list_1_mean = mean(*list_1[0])
    list_2_mean = mean(*list_2[0])
    numerator = 0

    # We must have the same number of elements
    # in both lists
    if len(list_1[0]) == len(list_2[0]):
        for i in range(len(list_1[0])):
            # FInd xi - x mean * yi - y mean
            numerator += (list_1[0][i] - list_1_mean) * (list_2[0][i] - list_2_mean)
        denominator = len(list_1[0]) - 1
        return numerator / denominator
    else:
        print("Error : You must have the same number of values in both lists")
