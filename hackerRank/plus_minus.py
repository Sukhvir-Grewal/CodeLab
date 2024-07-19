"""
Given an array of integers, calculate the ratios of its elements that are
positive, negative, and zero. Print the decimal value of each fraction
on a new line with places after the decimal.
"""


def plusMinus(arr):
    # Write your code here
    positive_numbers = 0
    negative_numbers = 0
    zeros = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        if arr[i] > 0:
            positive_numbers += 1
        if arr[i] < 0:
            negative_numbers += 1
    print(round(positive_numbers/len(arr), 6))
    print(round(negative_numbers/len(arr), 6))
    print(round(zeros/len(arr), 6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
