# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    """Finds the unique element in an array which doesn't have a pair"""
    # for element in A:
    #     count = A.count(element)

    #     if count % 2 == 1:
    #         return element
    # return "All elements have unique pairs."



lst = [x for x in range(1003)] + [1004] + [x for x in range(1003)]
# print(lst)
print(solution(lst))
