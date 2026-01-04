import sys
values = [1,2,3,4,5]
size_in_bytes = sum(sys.getsizeof(item) for item in values)/sys.getsizeof(values[0])
print(size_in_bytes)