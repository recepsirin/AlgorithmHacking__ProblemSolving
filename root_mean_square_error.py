import math


def solution(predicted, observed):
    n_list = list()

    square = 0
    mean = 0.0
    root = 0.0

    for i in range(0, len(predicted)):
        n_list.append(predicted[i] - observed[i])  # combining values within new list

    for n in range(0, len(n_list)):
        square += (n_list[n] ** 2)  # squaring each n value

        mean = (square / float(len(n_list)))  # dividing by each n value for mean

        root = math.sqrt(mean)  # lastly, square mean

    return root

