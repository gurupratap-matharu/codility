# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    """Finds the minimum absolute difference between an arbitrarily partitioned array."""
    if not A:
        return 0

    else:

        A.sort(reverse=True)
        length = len(A)
        left, right = A[0], sum(A[1:])
        answer = abs(left - right)

        for i in range(1, length):
            left += A[i]
            right -= A[i]
            answer = min(answer, abs(left - right))

    return answer


lst = [x for x in range(1000)]
print(solution(lst))
