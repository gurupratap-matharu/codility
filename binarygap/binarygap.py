def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:]

    binary = binary.split('1')
    if binary[-1].endswith('0'):
        binary.remove(binary[-1])

    return len(max(binary))

    
