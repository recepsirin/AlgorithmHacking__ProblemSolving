import math


def euclidean_distance(x: tuple, y: tuple) -> float:
    """Calculates euclidean distance from x to y"""
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
