def init_matrix(rows: int, cols: int) -> list[list[int]]:
    """
    Creates a 2D array (matrix) based on the input rows and columns.

    Parameter(s):
    - rows (int): Specifies the rows of the 2D array to be created.
    - cols (int): Specifies the columns of the 2D array to be created.

    Returns:
    - 2D array (int): This is the 2D array that is created using the input rows and cols.
    """
    return [[None for _ in range(cols)] for _ in range(rows)]

def kernel_ind(row, col, size) -> int:
    return size*col+row

def filter_image(image: list[list[int]], kernel: list[int]) -> list[list[int]]:
    """
    Perform the convolution operation by applying the kernel over the input image.

    Parameter(s):
    - 2D array (int): This is the image on which you have to apply the kernel/filter and perform convolution. 
    - 1D array (int): The first entry in this array is the width of the kernel and the remaining entries are the values of the kernel.

    Returns:
    - 2D array (int): This is the matrix that is obtained after performing convolution.
    """
    image_height = len(image)           # image_height = m = no. of rows
    image_width = len(image[0])         # image_width  = n = no. of columns 

    result = init_matrix(image_height, image_width)
    k_n = kernel.pop(0)             # kernel size

    for i in range(image_height):              # for image pixels
        for j in range(image_width):          # for image pixels
            masked_sum = 0
            for x in range(k_n):
                valid_row = (i - k_n//2) + x                # valid row for calculation of masking at particalur pixel
                if (valid_row >= 0 and valid_row < image_height):
                    for y in range(k_n):
                        valid_col = (j - k_n//2) + y
                        if (valid_col >= 0 and valid_col < image_width):
                            masked_sum += kernel[kernel_ind(x, y, k_n)]*image[valid_row][valid_col]

            result[i][j] = masked_sum

    return result


def main(file_name: str) -> list[list[int]]:
    """
    The main driver function that will run the entire program. 
    It should extract the image and the kernel from the file and pass them to filter_image(...).

    Parameter(s):
    - file_name (.txt file): Path to a text file that contains the image (2D array) and the kernel (1D array).

    Returns:
    - 2D array (int): This is the matrix that is obtained after executing filter_image(...)
    """

    with open (file_name) as f :
        lines = f.readlines()
    # print("lines", lines)
    img_m, img_n = lines.pop(0).strip().split()
    img_m = int(img_m)
    img_n = int(img_n)

    image = init_matrix(img_m, img_n)               # image
    for i in range(img_m):
        line = lines.pop(0).strip().split()
        for j in range(img_n):
            image[i][j] = int(line[j])

    lines = lines.pop().strip().split()
    kernel = [int(x) for x in lines]                # kernel

    return filter_image(image, kernel)
    
