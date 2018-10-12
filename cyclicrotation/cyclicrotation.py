
def solution(A, K):
    # write your code in Python 3.6
    # We simply split the matrix A and concatenate it again.
    for i in range(K):
        leftRotatebyOne(A)
    return A
# Function to left Rotate arr[] of size n by 1*/


def leftRotatebyOne(arr):
    temp = arr[0]
    length = len(arr)
    for i in range(length - 1):
        arr[i] = arr[i + 1]
    arr[length - 1] = temp


print(solution([1, 2, 3, 4], 4))
