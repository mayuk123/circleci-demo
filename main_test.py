import pytest
from main import SparseMatrix

def test_set_and_get_value():
    # Create a SparseMatrix, set a value, and test if get returns the expected value
    matrix = SparseMatrix()
    matrix.set(0, 0, 5)
    assert matrix.get(0, 0) == 5

def test_recommendation():
    # Create a SparseMatrix, set values, and test if recommendations are calculated correctly
    matrix = SparseMatrix()
    matrix.set(0, 0, 2)
    matrix.set(1, 1, 3)
    vector = [1, 2]
    recommendations = matrix.recommend(vector)
    assert recommendations == [2, 6]

def test_add_movie():
    # Create two SparseMatrices, add one to the other, and check if values are correctly added
    matrix1 = SparseMatrix()
    matrix1.set(0, 0, 2)
    matrix2 = SparseMatrix()
    matrix2.set(0, 1, 3)
    matrix1.add_movie(matrix2)
    assert matrix1.get(0, 0) == 2
    assert matrix1.get(0, 1) == 3

def test_to_dense():
    # Create a SparseMatrix, set values, and test if it converts to a dense matrix correctly
    matrix = SparseMatrix()
    matrix.set(0, 0, 2)
    matrix.set(1, 2, 3)
    dense_matrix = matrix.to_dense()
    assert dense_matrix == [[2, 0, 0], [0, 0, 3]]

def test_get_nonexistent_value():
    # Create a SparseMatrix and test if getting a value at a non-existent position returns 0
    matrix = SparseMatrix()
    assert matrix.get(2, 2) == 0

def test_invalid_input():
    # Create a SparseMatrix and test if it raises a ValueError for invalid input
    matrix = SparseMatrix()
    with pytest.raises(ValueError):
        matrix.set(-1, 0, 5)

def test_empty_matrix_recommendation():
    # Create an empty SparseMatrix and test if recommendations are all zeros
    matrix = SparseMatrix()
    vector = [1, 2, 3]
    recommendations = matrix.recommend(vector)
    assert recommendations == [0, 0, 0]  # No interactions, so recommendations should be all zeros

def test_add_movie_with_empty_matrix():
    # Create two SparseMatrices, add one to the other, and check if values are correctly added
    matrix1 = SparseMatrix()
    matrix2 = SparseMatrix()
    matrix2.set(0, 0, 2)
    matrix1.add_movie(matrix2)
    assert matrix1.get(0, 0) == 2  # Result should be the same as matrix2

def add_movie_with_invalid_input(self, matrix):
    # Check if the provided matrix is empty
    if not matrix.data:
        raise ValueError("Matrix to be added is empty.")
    
    # Add another sparse matrix, simulating the addition of a new movie
    for (row, col), value in matrix.data.items():
        # Set non-zero values from the new matrix into the current matrix
        self.set(row, col, value)


if __name__ == "__main__":
    # This block will be executed only if the script is run directly, not when imported as a module
    # You can include additional logic or run specific tests here if needed
    pass
