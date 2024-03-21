import numpy as np

# Task 1: Create a random vector of size 15 with integers in the range 1-20
print("Task 1: Create a random vector of size 15 with integers in the range 1-20")
random_vector = np.random.randint(1, 21, size=15)
print("Random Vector:")
print(random_vector)

# Reshape the array to 3x5
reshaped_array = random_vector.reshape(3, 5)
print("\nReshaped Array:")
print(reshaped_array)

# Print array shape
print("\nArray Shape:", reshaped_array.shape)

# Replace the max in each row by 0
reshaped_array[np.arange(reshaped_array.shape[0]), np.argmax(reshaped_array, axis=1)] = 0
print("\nModified Array:")
print(reshaped_array)

# Task 2: Create a 4x3 array with 4-byte integer elements
print("Task 2: Create a 4x3 array with 4-byte integer elements")
array_4x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.int32)
print("\n2-D Array:")
print(array_4x3)
print("Shape:", array_4x3.shape)
print("Type:", array_4x3.dtype)

# Task 3: Compute eigenvalues and right eigenvectors of a given square array
print("Task 3: Compute eigenvalues and right eigenvectors of a given square array")
square_array = np.array([[3, -2], [1, 0]])
eigenvalues, eigenvectors = np.linalg.eig(square_array)
print("\nEigenvalues:", eigenvalues)
print("Right Eigenvectors:")
print(eigenvectors)

# Task 4: Compute the sum of diagonal elements of a given array
print("Task 4: Compute the sum of diagonal elements of a given array")
diagonal_array = np.array([[0, 1, 2], [3, 4, 5]])
diagonal_sum = np.trace(diagonal_array)
print("\nSum of Diagonal Elements:", diagonal_sum)

# Task 5: Reshape an array without changing its data
print("Task 5: Reshape an array without changing its data")
array_3x2 = np.array([[1, 2], [3, 4], [5, 6]])
reshaped_3x2 = array_3x2.reshape(3, 2)
reshaped_2x3 = array_3x2.reshape(2, 3)
print("\nReshaped 3x2:")
print(reshaped_3x2)
print("Reshaped 2x3:")
print(reshaped_2x3)
