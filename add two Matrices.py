def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices have different dimensions and cannot be added"
    
    result = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat1[0])):
            temp.append(mat1[i][j] + mat2[i][j])
        result.append(temp)
    return result

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
resultant_matrix = add_matrices(matrix1, matrix2)
print(resultant_matrix)
