import math
from numpy import absolute

def trimmed_mean(lst, p):
    trim = int( len(lst) * p )
    trimmed_lst = lst[1:-1]
    return mean(*trimmed_lst) 

def mean(*args):
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

def mode(*args):
    # Count how many times values show up in
    # the list and put it in a dictionary
    dict_vals = {i: args.count(i) for i in args}
    # Create a list of keys that have the maximum
    # number of occurrence in the list
    max_list = [k for k, v in dict_vals.items() if v == max(dict_vals.values())]
    return max_list
 
def variance(*args):
    mean_val = mean(*args)
    numerator = 0
    for i in args:
        numerator += (i - mean_val) ** 2
    denominator = len(args) - 1
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

