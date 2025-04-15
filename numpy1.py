import numpy as np
# a=np.array([1,2,3,4])
# b=np.array([5,6,7,8])
# print(np.concatenate((a,b)))

# x = np.array([[1,2],[3,4]])
# y= np.array([[5,6]])
# print(np.concatenate((x,y), axis=0))

# array_examples = np.array([[[0,1,2,3], [4,5,6,7]], [[0,1,2,3], [4,5,6,7]], [[0,1,2,3],[4,5,6,7]]])
# print(array_examples.ndim)
# print(array_examples.size)

# c = np.arange(6)
# print(c)
# d = c.reshape(3,2)
# print(d)

aarray1 = np.arange(1, 11).reshape(2, 5)
print("1. Reshaped Array:\n", aarray1)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("2. Element-wise Addition:", a + b)
print("2. Element-wise Subtraction:", a - b)
print("2. Element-wise Multiplication:", a * b)
print("2. Element-wise Division:", a / b)

array2d = np.ones((3, 3))
array1d = np.array([1, 2, 3])
broadcasted = array2d + array1d
print("3. Broadcasting Result:\n", broadcasted)

rand_array = np.random.randint(0, 11, (5, 5))
diagonal_elements = np.diag(rand_array)
print("4. Random 5x5 Array:\n", rand_array)
print("4. Diagonal Elements:", diagonal_elements)

A = np.random.rand(3, 2)
B = np.random.rand(2, 4)
matrix_product = np.dot(A, B)
print("5. Matrix A:\n", A)
print("5. Matrix B:\n", B)
print("5. Matrix Product:\n", matrix_product)

agg_array = np.random.rand(4, 4)
print("6. Aggregation Array:\n", agg_array)
print("6. Total Sum:", np.sum(agg_array))
print("6. Mean:", np.mean(agg_array))
print("6. Standard Deviation:", np.std(agg_array))
print("6. Sum Along Axis 0:", np.sum(agg_array, axis=0))
print("6. Sum Along Axis 1:", np.sum(agg_array, axis=1))

