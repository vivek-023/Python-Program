import numpy as np

def main():
    # Create a NumPy array
    array = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

    # Check type of array
    array_type = type(array).__name__

    # Check axes of array
    array_axes = array.ndim

    # Check shape of array
    array_shape = array.shape

    # Check type of elements in array
    array_element_type = array.dtype

    # Print the results
    print("1. Type of array:", array_type)
    print("2. Axes of array:", array_axes)
    print("3. Shape of array:", array_shape)
    print("4. Type of elements in array:", array_element_type)

if __name__ == "__main__":
    main()
