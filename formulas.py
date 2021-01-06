import math
from numpy import absolute

def trimmed_mean(lst, p):
    '''
    Calculo de média aparada
    '''
    trim = int( len(lst) * p )
    trimmed_lst = lst[1:-1]
    return mean(*trimmed_lst) 

def mean(*args):
    '''
    Calculo de média,
    Somam todos os args
    dividem pela quantidade deles
    '''
    val_sum = sum(args)
    return val_sum / len(args)
 
def median(*args):
    if len(args) % 2 == 0:
        i = round((len(args) + 1) / 2)
        j = i - 1
        return (args[i] + args[j]) / 2
    else:
        k = round(len(args) / 2)
        return args[k]

def mad(*args):
    dataset_median = median(*args)
    return median(*[ absolute(arg - dataset_median) for arg in args ])

def standard_deviation(*args):
    return math.sqrt(variance(*args))

def variance(*args):
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
    return numerator / denominator

