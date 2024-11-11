import numpy as np
from numpy import ndarray

def add(arr1: ndarray, arr2: ndarray) -> ndarray:
    return np.add(arr1, arr2)

def subtract(arr1: ndarray, arr2: ndarray) -> ndarray:
    return np.subtract(arr1, arr2)

def multiply(arr1: ndarray, arr2: ndarray) -> ndarray:
    return np.multiply(arr1, arr2)

def divide(arr1: ndarray, arr2: ndarray) -> ndarray:
    return np.divide(arr1, arr2)

def power(arr1: ndarray, arr2: ndarray) -> ndarray:
    return np.power(arr1, arr2)

def sqrt(arr: ndarray) -> ndarray:
    return np.sqrt(arr)

def log(arr: ndarray) -> ndarray:
    return np.log(arr)

def exp(arr: ndarray) -> ndarray:
    return np.exp(arr)

def sin(arr: ndarray) -> ndarray:
    return np.sin(arr)

def cos(arr: ndarray) -> ndarray:
    return np.cos(arr)

def tan(arr: ndarray) -> ndarray:
    return np.tan(arr)

def abs(arr: ndarray) -> ndarray:
    return np.abs(arr)