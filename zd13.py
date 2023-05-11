import numpy as np

# Wprowadzamy dane
x = np.array([0, 1.25, 2.5, 3.75, 5, 6.25, 7.5, 8.75, 10])
f_x = np.array([4, 3.29, 3.08, 3.02, 3, 3, 0, 3, 3])

# Definiujemy funkcję f(x) w postaci macierzowej
def f_matrix(x):
    return np.column_stack((np.ones(len(x)), np.exp(-c*x)))

# Wyznaczamy macierz A i wektor b
c = 0.1
A = f_matrix(x)
b = f_x.reshape(-1, 1)

# Wyznaczamy wektor parametrów a i b za pomocą metody najmniejszych kwadratów
params = np.linalg.inv(A.T @ A) @ A.T @ b

# Wypisujemy wyniki
a = params[0][0]
b = params[1][0]
print("a =", a)
print("b =", b)

