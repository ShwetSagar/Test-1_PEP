import math
import os
import random
import re
import sys

def create_paginator(items, pageSize):
    for i in range(0, len(items), pageSize):
        yield items[i:i + pageSize]


if __name__ == '__main__':

    n = int(input())

    items = []

    for _ in range(n):
        items.append(int(input()))

    pageSize = int(input())

    paginator = create_paginator(items, pageSize)

    for page in paginator:
        print(page)
