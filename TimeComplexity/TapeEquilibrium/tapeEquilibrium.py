# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    """Finds the minimum absolute difference between an arbitrarily partitioned array."""

    A.sort()
    length = len(A)
    midpoint = length // 2
    left = sum(A[:midpoint])
    right = sum(A[midpoint:])

    answer = abs(left - right)  # we initialise the answer approximately

    for i in range(length):
        left = sum(A[:i])
        right = sum(A[i:])

        diff = abs(left - right)
        if diff < answer:
            answer = diff
    return answer


print(solution([1, 2, 3, 4, 5, 6]))
