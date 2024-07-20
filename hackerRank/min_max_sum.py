"""
Given five positive integers, find the minimum and maximum values that can be
calculated by summing exactly four of the five integers. Then print the
respective minimum and maximum values as a single line of two space-separated
long integers.
"""


def miniMaxSum(arr):
    # Write your code here
    max_number = float('-inf')
    min_number = float('inf')

    for i in range(len(arr)):
        current = 0
        for j in range(i, i + 4):
            index = j % len(arr)
            current += arr[index]
        if current > max_number:
            max_number = current
        if current < min_number:
            min_number = current
    print(str(min_number) + ' ' + str(max_number))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
