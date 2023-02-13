import sys

class Vector:
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), len(values[0]))

    def __repr__(self): # Es para representar el objeto
        return str(self.values)
     
    def __str__(self): # Es para representar el objeto
        return str(self.values)
    
    def __len__(self): # Es para calcular el tamaño del objeto
        return len(self.values) * len(self.values[0])   
    
    def __add__(self, other): # Es para sumar dos vectores
        if self.shape == other.shape:
            result = []
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    result.append([self.values[i][j] + other.values[i][j]])
            return Vector(result)
        else:
            print("Vectors deben tener el mismo shape")
            sys.exit()

    def __radd__(self, other): # Es para sumar dos vectores
        if self.shape == other.shape:
            result = []
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    result.append([self.values[i][j] + other.values[i][j]])
            return Vector(result)
        else:
            print("Vectors deben tener el mismo shape")
            sys.exit()
    
    def __sub__(self, other): # Es para restar dos vectores
        if self.shape == other.shape:
            result = []
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    result.append([self.values[i][j] - other.values[i][j]])
            return Vector(result)
        else:
            print("Vectors deben tener el mismo shape")
            sys.exit()
    
    def __rsub__(self, other): # Es para restar dos vectores
        if self.shape == other.shape:
            result = []
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    result.append([self.values[i][j] - other.values[i][j]])
            return Vector(result)
        else:
            print("Vectors deben tener el mismo shape")
            sys.exit()
        
    def __mul__(self, other): # Es para multiplicar dos vectores
        if isinstance(other, (int, float)):
            resultColumn = []
            resultRow = []
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    resultRow.append(self.values[i][j] * other)
                resultColumn.append(resultRow)
                resultRow = []
            return Vector(resultColumn)
        else:
            print("El multiplicador debe ser un número")
            sys.exit()
    
    def __truediv__(self, other): # Es para dividir dos vectores
        if other == 0.0:
            print("No se puede dividir entre cero")
            sys.exit()
        elif isinstance(other, (int, float)):
            resultColumn = []
            resultRow = []
            for i in range(len(self.values)):
                for j in range(len(self.values[i])):
                    resultRow.append(self.values[i][j] / other)
                resultColumn.append(resultRow)
                resultRow = []
            return Vector(resultColumn)
        else:
            print("El divisor debe ser un número")
            sys.exit()
    
    def __rtruediv__(self, other): # Es para dividir dos vectores
        print("Division of a scalar by a Vector is not defined here.")
        sys.exit()

     
    def T(self):
        resultColumn = []
        resultRow = []
        for i in range(len(self.values[0])):
            for j in range(len(self.values)):
                resultRow.append(self.values[j][i])
            resultColumn.append(resultRow)
            resultRow = []
        return Vector(resultColumn)
    
    def dot(self, other): # Es para multiplicar dos vectores
        if self.shape == other.shape:
            result = []
            res = 0
            for i in range(len(self.values)):
                resultRow = []
                for j in range(len(other.values[0])):
                    resultRow.append(self.values[i][j] * other.values[i][j])
                result.append(resultRow)
            for i in range(len(result)):
                for j in range(len(result[i])):
                    res += result[i][j]
            return res
        else:
            print("Vectors deben tener el mismo shape")
            sys.exit()


''' 
# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)
print("Expected output: Vector([[0.0], [5.0], [10.0], [15.0]])")
# Row vector of shape 1 * n

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
print("Expected output: Vector([[0.0, 5.0, 10.0, 15.0]])")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 / 2.0
print(v2)
print("Expected output:")
print("Vector([[0.0], [0.5], [1.0], [1.5]])")

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v1 / 0.0
# Expected ouput
# ZeroDivisionError: division by zero.

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
2.0 / v1
# Expected output:
# NotImplementedError: Division of a scalar by a Vector is not defined here.

# Column vector of shape (n, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output
# (4,1)

print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Expected output
# [[0.0], [1.0], [2.0], [3.0]]

# Row vector of shape (1, n)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output
# (1,4)

print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
# Expected output
# [[0.0, 1.0, 2.0, 3.0]]

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
# Expected output:
(4,1)

v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.T())
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1.T().shape)
# Expected output:
# (1,4)

# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
# Expected output:
# (1,4)

v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(v2.T().shape)
# Expected output:
# (4,1)

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0

v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 13.0

v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v1
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
'''
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]


'''


Los "Special Methods" son métodos especiales que tienen un nombre precedido y seguido de dos guiones bajos. Estos métodos son especiales porque tienen un significado especial en Python y son utilizados para sobreescribir ciertas operaciones básicas.
__len__: Este método es llamado cuando se intenta obtener la longitud de un objeto, por ejemplo, cuando se usa la función len(). Este método debe devolver un entero que represente la longitud del objeto.

__add__: Este método es llamado cuando se intenta sumar dos objetos utilizando el operador +. Este método debe devolver un nuevo objeto que sea el resultado de la suma.
'''



