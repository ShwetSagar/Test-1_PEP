import math
import os
import random
import re
import sys

def reverseSubarrays(arr, operations):
    for left, right in operations:
        arr[left:right + 1] = arr[left:right + 1][::-1]
    return arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    operations_rows = int(input().strip())
    operations_columns = int(input().strip())

    operations = []

    for _ in range(operations_rows):
        operations.append(list(map(int, input().rstrip().split())))

    result = reverseSubarrays(arr, operations)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
