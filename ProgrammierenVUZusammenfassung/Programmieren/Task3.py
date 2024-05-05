import numpy as np
import sys

lines = sys.stdin()

for line in lines:
    
    if 'q:' == line.rstrip():
        break
    print(f"Input: {line}")